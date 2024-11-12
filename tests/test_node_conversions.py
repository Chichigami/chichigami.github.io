import unittest

from htmlnode import LeafNode
from node_conversions import *
from textnode import TextNode

class TestNodeConversion(unittest.TestCase):
    def test_no_tag(self):
        node = TextNode("foo", None, "bar")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_not_possible_tag(self):
        node = TextNode("foo", "hello", "bar")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_text(self):
        node = TextNode("foo", text_type_text, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode(None, "foo")
        self.assertEqual(actual, expected)
        
    def test_bold(self):
        node = TextNode("foo", text_type_bold, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("b", "foo")
        self.assertEqual(actual, expected)
        
    def test_italic(self):
        node = TextNode("foo", text_type_italic, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("i", "foo")
        self.assertEqual(actual, expected)
    
    def test_code(self):
        node = TextNode("foo", text_type_code, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("code", "foo")
        self.assertEqual(actual, expected)
    
    def test_link(self):
        node = TextNode("Click me!", text_type_link, "https://www.google.com")
        actual = text_node_to_html_node(node)
        expected = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(actual, expected)
    
    def test_image(self):
        node = TextNode("foo", text_type_image, "https://www.someurl.com/")
        actual = text_node_to_html_node(node)
        expected = LeafNode("img", "", {"src": "https://www.someurl.com/", "alt": "foo"})
        self.assertEqual(actual, expected)

class TestSplitTextNode(unittest.TestCase):
    def test_default(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_default_back_to_back(self):
        node = TextNode("This is text with a `code block``code block2` word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode("", text_type_text),
                    TextNode("code block2", text_type_code),
                    TextNode(" word", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_default_every_other(self):
        node = TextNode("foo `code block` bar `code block2` foobar", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("foo ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" bar ", text_type_text),
                    TextNode("code block2", text_type_code),
                    TextNode(" foobar", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_default_with_bold(self):
        node = TextNode("foo `code block` bar **bold** foobar", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("foo ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" bar **bold** foobar", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_plain(self):
        node = TextNode("This is text with a word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a word", text_type_text),
                    ]
        self.assertEqual(actual, expected)

class TestRegexExtractionLinks(unittest.TestCase):
    def test_default(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual = extract_markdown_links(text)
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(actual, expected)
    
    def test_link_vs_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_links(text)
        expected = []
        self.assertEqual(actual, expected)

    def test_back_to_back_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)"
        actual = extract_markdown_links(text)
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(actual, expected)


class TestRegexExtractionImages(unittest.TestCase):
    def test_default(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)
    
    def test_images_vs_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual = extract_markdown_images(text)
        expected = []
        self.assertEqual(actual, expected)

    def test_back_to_back_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)

class TestSplitTextNodeImages(unittest.TestCase):
    def test_default(self):
        node = TextNode("First ![to boot dev](https://www.boot.dev) Middle ![to youtube](https://www.youtube.com/@bootdotdev) End", text_type_text,)
        actual = split_nodes_image([node])
        expected = [
                    TextNode("First ", text_type_text),
                    TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
                    TextNode(" Middle ", text_type_text),
                    TextNode("to youtube", text_type_image, "https://www.youtube.com/@bootdotdev"),
                    TextNode(" End", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_more_text(self):
        text = "Foo1 Foo2 ![alt1](link1) Bar1 Bar2 ![alt2](link2) Foo Bar3 Foo Bar3 ![alt3](link3) FooBar"
        node = TextNode(text, text_type_text)
        actual = split_nodes_image([node])
        expected = [
            TextNode("Foo1 Foo2 ", text_type_text),
            TextNode("alt1", text_type_image, "link1"),
            TextNode(" Bar1 Bar2 ", text_type_text),
            TextNode("alt2", text_type_image, "link2"),
            TextNode(" Foo Bar3 Foo Bar3 ", text_type_text),
            TextNode("alt3", text_type_image, "link3"),
            TextNode(" FooBar", text_type_text)
        ]
        self.assertEqual(actual, expected)


    def test_no_image(self):
        node = TextNode("First Middle End", text_type_text,)
        actual = split_nodes_image([node])
        expected = [node]
        self.assertEqual(actual, expected)
class TestSplitTextNodeLinks(unittest.TestCase):
    def test_default(self):
        node = TextNode("First [to boot dev](https://www.boot.dev) Middle [to youtube](https://www.youtube.com/@bootdotdev) End", text_type_text,)
        actual = split_nodes_link([node])
        expected = [
                    TextNode("First ", text_type_text),
                    TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                    TextNode(" Middle ", text_type_text),
                    TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
                    TextNode(" End", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_more_links(self):
        text = "Foo1 Foo2 [alt1](link1) Bar1 Bar2 [alt2](link2) Foo Bar3 Foo Bar3 [alt3](link3) FooBar"
        node = TextNode(text, text_type_text)
        actual = split_nodes_link([node])
        expected = [
            TextNode("Foo1 Foo2 ", text_type_text),
            TextNode("alt1", text_type_link, "link1"),
            TextNode(" Bar1 Bar2 ", text_type_text),
            TextNode("alt2", text_type_link, "link2"),
            TextNode(" Foo Bar3 Foo Bar3 ", text_type_text),
            TextNode("alt3", text_type_link, "link3"),
            TextNode(" FooBar", text_type_text),
        ]
        self.assertEqual(actual, expected)


    def test_no_link(self):
        node = TextNode("First Middle End", text_type_text,)
        actual = split_nodes_link([node])
        expected = [node]
        self.assertEqual(actual, expected)

class TestUltimateSplit(unittest.TestCase):
    def test_default(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        temp = text_to_textnodes(text)
        actual = ''.join([text_node_to_html_node(nodes).to_html() for nodes in temp])
        expected = 'This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan image"></img> and a <a href="https://boot.dev">link</a>'
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()