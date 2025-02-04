import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.someurl.com/")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.someurl.com/")
        self.assertNotEqual(node, node2)
    
    def test_default_url(self):
        node = TextNode("URL is None", text_type_bold)
        self.assertEqual(node.url, None)
    

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.someurl.com/")
        expected = "TextNode(This is a text node, bold, https://www.someurl.com/)"
        actual = repr(node)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()