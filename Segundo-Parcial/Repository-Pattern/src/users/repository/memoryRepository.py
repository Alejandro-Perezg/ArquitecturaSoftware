from users.repository.abstractRepository import AbstractRepository
from users.model import course_model


class CourseRepository(AbstractRepository):

    def __init__(self):
        self.courses = []

 
    def add(self, course: course_model.Course):
        self.courses.append(course)


    def get(self, course_id) -> course_model.Course:
        course = next((course for course in self.courses if course.id == int(course_id)), None)
        return course
    
    
    #retrieve course name
    # def get(self, course_name) -> course_model.Course:
    #     course = next((course for course in self.courses if course.course == int(course_name)), None)
    #     return course