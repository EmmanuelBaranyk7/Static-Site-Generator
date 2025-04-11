import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode


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


    # Test ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    #Empty children list - What happens when you pass an empty list as children?
    def test_to_html_with_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    #Deep nesting - Test with multiple levels of nesting
    # Create a structure several levels deep
    # Assert the properly nested HTML result
    
    def test_deep_nesting(self):
        greatgrandchild1 = LeafNode("b", "greatgrandchild")
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        grandchild_node3 = LeafNode(None, "grandchild3")
        grandchild_node4 = ParentNode("IDKwhatgoeshere", [greatgrandchild1])
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3, grandchild_node4])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i>grandchild3<IDKwhatgoeshere><b>greatgrandchild</b></IDKwhatgoeshere></span></div>"                  
        )


    # test LeafNode
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
        
if __name__ == "__main__":
    unittest.main()