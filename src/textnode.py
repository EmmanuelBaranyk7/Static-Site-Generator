from enum import Enum

class TextType(Enum):
    Normal_text = "Normal text"
    BOLD = "**Bold text"
    Italic_text = "_Italic text_"
    Code_text = "'Code text'"
    Links = "[anchor text](url)"
    Images = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(textnode):
        return f"TextNode({textnode.text}, {textnode.text_type}, {textnode.url})"
