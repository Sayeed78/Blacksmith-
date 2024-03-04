class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children else []

def create_tree_from_file(file_path):
    root = TreeNode(None)  # Create an empty root node
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            paragraphs = content.split(',')  # Split paragraphs by commas

            # Create tree nodes for each paragraph
            for paragraph in paragraphs:
                node = TreeNode(paragraph)
                root.children.append(node)  # Add paragraph node as a child of the root

        return root
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 'File not found'

# Replace 'your_file.txt' with the path to your file
file_path = './scholar_dialog.py'

# Create tree from file
tree_root = create_tree_from_file(file_path)

# Example traversal printing data in nodes
def traverse_tree(node):
    if node:
        print(node.data)
        for child in node.children:
            traverse_tree(child)

# Example traversal starting from the root
traverse_tree(tree_root)
