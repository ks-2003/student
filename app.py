import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'student_performance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.Integer, unique=True, nullable=False)
    grades = db.relationship('Grade', backref='student', lazy=True)

    def calculate_average(self):
        if not self.grades:
            return 0
        total = sum(grade.score for grade in self.grades)
        return total / len(self.grades)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

# Create all tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return "Welcome to Student Performance Tracker"

# Add student form (GET)
@app.route('/add_student', methods=['GET'])
def add_student_form():
    return render_template('add_student.html')

# Add student form submission (POST)
@app.route('/add_student', methods=['POST'])
def add_student_submit():
    name = request.form.get('name')
    roll_number = request.form.get('roll_number')
    if not name or not roll_number:
        return "Missing data", 400
    try:
        roll_number = int(roll_number)
    except ValueError:
        return "Invalid roll number", 400

    existing_student = Student.query.filter_by(roll_number=roll_number).first()
    if existing_student:
        return "Student with this roll number already exists", 400

    new_student = Student(name=name, roll_number=roll_number)
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('home'))

# Add grade form (GET)
@app.route('/add_grade', methods=['GET'])
def add_grade_form():
    students = Student.query.all()
    return render_template('add_grade.html', students=students)

# Add grade form submission (POST)
@app.route('/add_grade', methods=['POST'])
def add_grade_submit():
    roll_number = request.form.get('roll_number')
    subject = request.form.get('subject')
    score = request.form.get('score')

    if not roll_number or not subject or not score:
        return "Missing data", 400
    try:
        roll_number = int(roll_number)
        score = float(score)
    except ValueError:
        return "Invalid roll number or score", 400

    student = Student.query.filter_by(roll_number=roll_number).first()
    if not student:
        return "Student not found", 404

    new_grade = Grade(subject=subject, score=score, student=student)
    db.session.add(new_grade)
    db.session.commit()
    return redirect(url_for('home'))

# Display student details
@app.route('/display_student/<int:roll_number>')
def display_student(roll_number):
    student = Student.query.filter_by(roll_number=roll_number).first()
    if not student:
        return f"No student found with roll number {roll_number}", 404

    grades = {grade.subject: grade.score for grade in student.grades}
    average = student.calculate_average()
    return render_template('student_info.html', student={
        "name": student.name,
        "roll_number": student.roll_number,
        "grades": grades,
        "average": f"{average:.2f}"
    })

# Display average grades for all students
@app.route('/students_averages')
def students_averages():
    students = []
    all_students = Student.query.all()
    for s in all_students:
        students.append({
            "roll_number": s.roll_number,
            "name": s.name,
            "average": s.calculate_average()
        })
    return render_template('students_average.html', students=students)

# API Endpoints (for JSON requests) - similar modifications needed if desired

# Run app
if __name__ == '__main__':
    app.run(debug=True)
