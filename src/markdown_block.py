from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from inline_markdown import text_node_to_html_node, text_to_textnodes 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"

def block_to_block_type(block):

    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDEREDLIST
    elif len(block) >= 3 and block[0].isdigit() and block[1:3] == ". ":
        return BlockType.ORDEREDLIST
    return BlockType.PARAGRAPH



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []  # This will hold all the block nodes

    for block in blocks:
        #block_type = block_to_block_type(block)
        html_node = block_to_htmlnode(block)
        children.append(html_node)

    return ParentNode("div", children)



def block_to_htmlnode(block):
    block_type = block_to_block_type(block)

    if block_type is BlockType.CODE:
        return code_block_to_html(block)            
    elif block_type is BlockType.UNORDEREDLIST:
        return unordered_list_block_to_html(block)
    elif block_type is BlockType.ORDEREDLIST:
        return ordered_list_block_to_html(block)
    elif block_type is BlockType.HEADING:
        return heading_block_to_html(block)
    elif block_type is BlockType.QUOTE:
        return quote_block_to_html(block)
    elif block_type is BlockType.PARAGRAPH:
        return paragraph_block_to_html(block)
    


def code_block_to_html(block):
    if not block.startswith("```") or not block.endswith("```"):
                raise ValueError("invalid code block")
    code_block = block[3:-3]  # Remove the ```
    text_node = TextNode(code_block, TextType.TEXT)  # Not parsed as markdown
    code_html = text_node_to_html_node(text_node)
    return ParentNode("pre", [code_html])

def unordered_list_block_to_html(block):
    # Handle unordered lists
    list_children = []
    items = block.split("\n")
    for item in items:
        if item.startswith("- "):
            item_content = item[2:]
            ch = text_to_children(item_content)
            list_element = ParentNode("li", ch)
            list_children.append(list_element)
    return ParentNode("ul", list_children)

def ordered_list_block_to_html(block):
    list_children = []
    items = block.split("\n")
    for item in items:
        if len(item) >= 3 and item[0].isdigit() and item[1:3] == ". ":
            item_content = item[3:]
            if item_content:
                ch = text_to_children(item_content)
                list_element = ParentNode("li", ch)
                list_children.append(list_element)
    return ParentNode("ol", list_children)

def heading_block_to_html(block):
    heading_level = 0
    for char in block:
        if char == '#':
            heading_level += 1
        else:
            break
    #heading_level = block.find(" ") + 1
    if heading_level >= len(block):
        raise ValueError(f"invalid heading level")
    heading_tag = f"h{heading_level}"
    text = block[heading_level:].strip()
    heading_children = text_to_children(text)
    return ParentNode(heading_tag, heading_children)

def quote_block_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if line[0] != ">": 
            raise ValueError("invalid quote syntax")
        
        new_lines.append(line[1:].strip())
    text = " ".join(new_lines)
    ch = text_to_children(text)
    return ParentNode("blockquote", ch)

def paragraph_block_to_html(block):
    text = block.split()
    paragraph = " ".join(text)
    if not paragraph:  # gets rid of empty paragraphs
        return HTMLNode(None, None)
    ch = text_to_children(paragraph)
    return ParentNode("p", ch)



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_n = text_node_to_html_node(node)
        html_nodes.append(html_n)
    return html_nodes
    
def block_type_to_tag(block_type, block):
    if block_type is BlockType.HEADING:  # could probably curry this later
        heading_index = block.find(" ") + 1  # for diffrent types of headings
        return f"h{heading_index}"
    elif block_type is BlockType.QUOTE:
        return "blockquote"
    elif block_type is BlockType.UNORDEREDLIST or block_type is BlockType.ORDEREDLIST:
            return "li" # implement <ul> tag in seperate func
    elif block_type is BlockType.CODE:
        return "code"  # cod blocks don't parse children, implement in separte func
    return "p" # paragraph block

    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block:
            filtered_blocks.append(block)
    return filtered_blocks
