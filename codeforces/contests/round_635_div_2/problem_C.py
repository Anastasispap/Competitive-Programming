class Node(object):
    def __index__(self, parent=None):
        self.set_parent(parent)
        self.children = set()

    def set_parent(self, parent):
        if self.parent and self.parent is not parent:
            self.parent.children.remove(self)
        self.parent = parent

    def siblings(self):
        if self.parent is None:
            return []
        return [_ for _ in self.parent.children if _ is not self]

    def add_child(self, node):
        self.children.add(node)
        node.set_parent(self)

    def add_sibling(self, node):
        assert self.parent, "root node can't have siblings"
        self.parent.add_child(node)

root = Node()
nodes = [Node(parent=root) for _ in range(3)]

#
# def main():
#     n, k = [int(x) for x in input().split()]
#
#     for i in range(n-1):
#         v, u = [int(x) for x in input().split()]
#
# if __name__ == '__main__':
#     main()