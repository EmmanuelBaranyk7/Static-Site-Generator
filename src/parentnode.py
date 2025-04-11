from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag attribute")
        if self.children is None:
            raise ValueError("ParentNode must have a children attribute")
        
        html_pre_str = ""

        for i in self.children:
                html_pre_str += i.to_html()
            
        return f"<{self.tag}>{html_pre_str}</{self.tag}>"

        
