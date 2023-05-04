from db.MongoTools import MongoTools


class MessageRepo:
    @staticmethod
    def create():
        result = MongoTools().get()
        return result

    @staticmethod
    def get():
        result = MongoTools().get()
        return result

    @staticmethod
    def remove():
        ...
