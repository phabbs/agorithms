class SquareGridWithWeight:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)
