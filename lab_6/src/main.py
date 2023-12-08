class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
            curr_node = curr_node.children[letter]
        curr_node.children["*"] = TrieNode()  # Mark the end of the word with "*"

    def print_nodes(self, node=None, current_path=""):
        if node is None:
            node = self.root

        # Print the current node
        print(current_path)

        # Recursively print child nodes
        for letter, child_node in node.children.items():
            if letter != "*":
                self.print_nodes(child_node, current_path + letter)

    def find_prefix_node(self, node):
        children_count = sum(1 for child in node.children.values() if child)
        if children_count >= 2 or "*" in node.children:
            return node
        for child_node in node.children.values():
            if child_node:
                result = self.find_prefix_node(child_node)
                if result:
                    return result
        return None

    def prefix(self):
        current_node = self.root
        prefix = ""

        while len(current_node.children) == 1 and "*" not in current_node.children:
            letter, child_node = current_node.children.popitem()
            prefix += letter
            current_node = child_node

        return prefix if prefix else None
