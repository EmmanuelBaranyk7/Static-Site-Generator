import unittest

from leafnode import LeafNode

class TestLeadNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(f"test_leaf_to_html_p props: {node.props}")
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    #Test a node with no tag (raw text)
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    #Test a node with no value (should raise ValueError):
    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    #Test a different HTML tag (like span, div, etc.):
    def test_leaf_span_tag(self):
        node = LeafNode("span", "Span content")
        self.assertEqual(node.to_html(), "<span>Span content</span>")

    #Test multiple properties:
    def test_leaf_multiple_props(self):
        node = LeafNode("a", "Link text", {"href": "https://example.com", "class": "link-class", "id": "unique-id"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" class="link-class" id="unique-id">Link text</a>')

    #Test empty properties dictionary:
    def test_leaf_empty_props(self):
        node = LeafNode("p", "Paragraph text", {})
        self.assertEqual(node.to_html(), "<p>Paragraph text</p>")


    #tests examples
    #nodes with no tag
    #nodes with no value
    #different HTML tags
    #multiple properties
    #empty properties dictionary