import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.Boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.Boot.dev" target="_blank"')

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", children=None, props={"href": "https://www.Boot.dev"})
        self.assertEqual(repr(node), "HTMLNode(p, Hello, None, {'href': 'https://www.Boot.dev'})")

    def test_empty_initialization(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
if __name__ == "__main__":
    unittest.main()