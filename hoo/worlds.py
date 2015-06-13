class World:

    id = 3  # class (or static) variable

    def __init__(self):
        pass

    @classmethod
    def g(cls, arg):
        if arg > cls.id:
            cls.id = arg  # would the the same as  World.i = arg1
