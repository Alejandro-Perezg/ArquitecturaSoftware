from flask import Blueprint, jsonify, request
from users.model.course_model import Course



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

 
    #JSON list
    course_list = repository.courses
    
    for element in course_list:
        if element.course == course.course and element.id != course.id:
            return jsonify({"message": "Course already exist!"}), 400
    
    repository.add(course)
    return jsonify(course)

@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    course = repository.get(course_id)

    if course is None:
        return jsonify({"message": "Course does not exist"}), 400
    
    return jsonify(course)


#  POST example
# {
#     "course":"enchant",
#     "description":"most important skill on skyrim"
# }