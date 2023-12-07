class Trie:
    def __init__(self):
        self.root = {"*": "*"}

    def add_word(self, words):
        curr_node = self.root
        for word in words:
            for letter in word:
                if letter not in curr_node:
                    curr_node[letter] = {}
                curr_node = curr_node[letter]
            curr_node["*"] = "*"

    def print_nodes(self):
        def dfs(node, current_path):
            # Print the value of the current node
            print(current_path)

            # Recursively visit child nodes
            for letter, child_node in node.items():
                if letter != "*":
                    dfs(child_node, current_path + letter)

        dfs(self.root, "")

    def prefix(self, words):
        if not words:
            return ""

        # Sort the words to ensure that the common prefix is at the beginning
        words.sort()

        # Consider the first and last words in the sorted list
        first_word = words[0]
        last_word = words[-1]

        # Find the common prefix character by character
        common_prefix = ""
        for i in range(len(first_word)):
            if i < len(last_word) and first_word[i] == last_word[i]:
                common_prefix += first_word[i]
            else:
                break

        return common_prefix

trie = Trie()
words = ["apple", "apricot", "banana", "apex", "bat"]
for word in words:
    trie.add_word(word)
prefix_word = ["apple", "apricot", "apex"]
result = trie.prefix(prefix_word)
print("prefix of word massif " + str(prefix_word) + " is: " + result)
