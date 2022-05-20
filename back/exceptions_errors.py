class NonexistentItemError(Exception):
    def __init__(self, msg):
        self.message = msg

class DependencyConflict(Exception):
    def __init__(self, msg):
        self.message = msg