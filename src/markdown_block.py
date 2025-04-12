from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    for block in blocks:
        block_type = block_to_block_type(block)





def block_to_html_heading(self):
    
    

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