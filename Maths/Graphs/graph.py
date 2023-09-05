class Vertices:
    def __init__(self, *args):
        self.data = {i for i in args}

class Edges:
    def __init__(self, *args):
        self.data = {i for i in args}
class Graph:
    def __init__(self, v, e):
        self.data = (v, e)


