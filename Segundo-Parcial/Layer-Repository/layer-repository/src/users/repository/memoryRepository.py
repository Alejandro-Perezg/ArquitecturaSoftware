from users.repository.abstractRepository import AbstractRepository
from users.model import user_model


class UserRepository(AbstractRepository):

    def __init__(self):
        self.users = []

 
    def add(self, user: user_model.User):
        self.users.append(user)


    def get(self, user_id) -> user_model.User:
        user = next((user for user in self.users if user.id == int(user_id)), None)
        return user