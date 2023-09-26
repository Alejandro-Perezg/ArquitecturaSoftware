import abc
from users.model import course_model

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, course: course_model.Course):
        raise NotImplementedError


    @abc.abstractmethod
    def get(self, reference) -> course_model.Course:
        raise NotImplementedError