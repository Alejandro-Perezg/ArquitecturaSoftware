from flask import Blueprint, jsonify, request
from users.model.course_model import Course
from users.repository.memoryRepository import CourseRepository



blueprint = Blueprint('course_controller',__name__)
repository = CourseRepository()


#Endpoints
@blueprint.route("/courses", methods = ["POST"])
def insert_course():
    course_data = request.get_json()

    course = Course(
        id = len(repository.courses) + 1,
        course = course_data["course"],
        description = course_data["description"]
    )

    # if course.course in repository:
    #     return jsonify({"message": "Course already exists!"}, 400)
    
    repository.add(course)
    return jsonify(course)

@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    course = repository.get(course_id)

    if course is None:
        return jsonify({"message": "Course does not exist"}, 400)
    
    return jsonify(course)