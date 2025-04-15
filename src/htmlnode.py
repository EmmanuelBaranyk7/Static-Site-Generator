

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
 
    def props_to_html(self):
        if self.props is None:
            return ""
    
        props_str = ""
        for key, value in self.props.items():   #handels all key types
            props_str += f' {key}="{value}"'
        
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag attribute")
        if self.children is None:
            raise ValueError("ParentNode must have a children attribute")
        
        html_pre_str = ""

        for i in self.children:
                html_pre_str += i.to_html()
            
        return f"<{self.tag}>{html_pre_str}</{self.tag}>"
