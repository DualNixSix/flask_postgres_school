# We import the `Flask` and `jsonify` classes from the Flask library.
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql+psycopg://postgres:postgres@localhost/school'
)

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(1))

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(1))

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    
@app.route('/', methods=['GET'])
def root():
    return "<h1><div>Backend Directory</div><a href = /students>Students</a><br><a href = /teachers>Teachers</a><br><a href = /subjects>Subjects</a><h1>"

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = [
        {
            'id': student.id, 
            'first_name': student.first_name, 
            'last_name': student.last_name, 
            'age': student.age, 
            'subject': student.subject
            }
        for student in students
    ]
    return jsonify(student_list)

# We define a route `/teachers` that responds to GET requests.
@app.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    teacher_list = [
        {
            'id': teacher.id, 
            'first_name': teacher.first_name, 
            'last_name': teacher.last_name, 
            'age': teacher.age, 
            'subject': teacher.subject
            }
        for teacher in teachers
    ]
    return jsonify(teacher_list)

# We define a route `/subjects` that responds to GET requests.
@app.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    subject_list = [
        {
            'id': subject.id, 
            'subject': subject.subject, 
            }
        for subject in subjects
    ]
    return jsonify(subject_list)

if __name__ == '__main__':
    app.run(debug=True, port=8000) # Flask tries to run on port 5000 by default but it's sometimes occupied by a different function. Let's tell flask to utilize port 8000 instead