class Node:
    def __init__(self, token):
        self.token = token
        self.children = []

    def add_child(self, node):
        self.children.append(node)
