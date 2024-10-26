# ast_node.py

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value  # The condition for operands (e.g., age > 30)
        self.left = left  # Left child node
        self.right = right  # Right child node

    def __repr__(self):
        if self.type == 'operator':
            return f"({self.left} {self.value} {self.right})"
        return f"{self.value}"
