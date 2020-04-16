class Queue(object):
    def __init__(self, owner: User, password: str, comment: str = "", section_time: int = 5, open_time: int = 120):
        self.owner = owner
        self.password = password
        self.comment = comment
        self.section_time = section_time
        self.open_time = open_time

    
