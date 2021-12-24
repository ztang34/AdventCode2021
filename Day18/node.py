class Node:
    def __init__(self, value = 0, layer =0, is_leaf_node = False, left_child = None, right_child = None):
        self.value = value
        self.layer = layer
        self.is_leaf_node = is_leaf_node
        self.left_child = left_child
        self.right_child = right_child
    
    def get_node_value(self):
        if self.is_leaf_node == True:
            return self.value
        else:
            return 3 * self.left_child.get_node_value() + 2 * self.right_child.get_node_value()
    
    