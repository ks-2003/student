# Student Performance Tracker

A Python Flask web application for teachers to track student performance across multiple subjects. This project allows adding students, assigning grades, viewing individual student details, calculating average grades, and managing student information with persistent storage using SQLite.

---

## Features

- **Add Students:** Input student name and unique roll number.
- **Add Grades:** Assign grades for each subject per student (e.g., Math, Science, English).
- **View Student Details:** See student info along with grades and average grade.
- **Calculate Average Grades:** Compute average grades for individual students and class averages.
- **Persistent Storage:** Uses SQLite database via SQLAlchemy ORM for data persistence.
- **Web Interface:** User-friendly HTML forms and pages powered by Flask.

---

## Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite (local database)
- Gunicorn (production WSGI server)
- HTML/CSS (templates)

---

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` package manager

### Setup & Installation

1. Clone this repository:


2. Create and activate a virtual environment:


3. Install dependencies:


4. Run the Flask app locally:


5. Open your browser and visit:  
http://localhost:5000/

---

## Usage

- Navigate to `/add_student` to add new students.
- Use `/add_grade` to assign grades to existing students.
- View detailed student reports at `/display_student/<roll_number>`.
- See all students’ average grades at `/students_averages`.

---

## Future Improvements (Bonus Features)

- Subject-wise topper report.
- Class average by subject.
- Save and export data locally as text files.
- Editing and deleting students/grades.
- User authentication for secured access.

---

## Contributing

Feel free to fork the project and submit pull requests for enhancements or bug fixes.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or feedback, please open an issue or contact [kunalsingh915171@gmail.com].


