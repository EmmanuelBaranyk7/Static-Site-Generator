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

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[0:2] == "- ":
        return BlockType.UNORDEREDLIST
    elif block[0].isdigit() and block[1:3] == ". ":
        return BlockType.ORDEREDLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_final = ""

    for block in blocks:
        block_type = block_to_block_type(block)
        children = text_to_children(block)
        tag = block_type_to_tag(block_type, block)

        if block_type is BlockType.CODE:
            html_final += (block_type_code_to_html(block))
            continue

        if block_type is BlockType.UNORDEREDLIST or block_type is BlockType.ORDEREDLIST:
            html += (block_type_list_to_html(block, block_type, tag, children))
            continue

        html_final += ParentNode(tag, children).to_html()

    return f"<div>{html_final}</div>"



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

def block_type_code_to_html(block):
    block = block[3:-3]   # removing the "```" form the ends of the block
    text_node = TextNode(block, TextType.CODE)    
    html = text_node_to_html_node(text_node)
    return f"<pre>{html}</pre>"

def block_type_list_to_html(block, block_type, tag, children):
    if block_type is BlockType.UNORDEREDLIST:
        type = "ul"
    else:
        type = "ol"
    return f"<{type}>{ParentNode(tag, children).to_html()}</{type}>"
    

'''
#this is my implimentation
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    
    cleaned_blocks = []
    for block in blocks:
        block = block.strip()
        lines = block.split("\n")
        cleaned_lines = [line.strip() for line in lines]
        cleaned_block = "\n".join(cleaned_lines)
        if cleaned_block:
            cleaned_blocks.append(cleaned_block)
    
    return cleaned_blocks
'''