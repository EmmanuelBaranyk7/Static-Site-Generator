import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
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
        


    #Error cases
    #Test with None tag
    #Test with None children
    #Test with children that aren't a list