from htmlnode import HTMLNode
#from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if self.tag is None:
            return self.value
        self_props = self.props_to_html()
        #print(f"self.props passed to to_html: {self_props}")
        return f"<{self.tag}{self_props}>{self.value}</{self.tag}>"

