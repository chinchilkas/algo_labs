import unittest
import src.main as main

class TrieTest(unittest.TestCase):

    def test_no_word_for_prefix(self):
        trie = main.Trie()
        words = []
        for word in words:
            trie.add_word(word)
        result = trie.prefix()
        self.assertIsNone(result)

    def test_one_word(self):
        trie = main.Trie()
        word = ['apple']
        trie.add_word(word)
        result = trie.prefix()
        self.assertEqual(result, word[0])

    def test_empty_string_prefix(self):
        trie = main.Trie()
        words = ["apple", "apricot", "banana", "apex", "bat"]
        for word in words:
            trie.add_word(word)
        result = trie.prefix()
        self.assertIsNone(result)

    def test_prefix(self):
        trie = main.Trie()
        words = ["apple", "apricot", "apex"]
        for word in words:
            trie.add_word(word)
        result = trie.prefix()
        expected_result = "ap"
        self.assertEqual(result, expected_result)

    def test_word_in_trie(self):
        trie = main.Trie()
        words = ["apple", "apricot", "apex"]
        for word in words:
            trie.add_word(word)
        result = trie.search_word("apple")
        self.assertTrue(result)