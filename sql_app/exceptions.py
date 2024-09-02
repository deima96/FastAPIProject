class UserException(Exception):
    pass


class UserNotFoundError(UserException):
    def __init__(self):
        self.status_code=404
        self.status_detail="User not found."

class UseralreadyExistError(UserException):
    def __init__(self):
        self.status_code=409
        self.status_detail="User already exists"