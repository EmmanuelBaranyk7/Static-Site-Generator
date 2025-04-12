from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode, text_node_to_html_node
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
           new_nodes.append(old_node)
        else:
            pieces = old_node.text.split(delimiter)
            if len(pieces) % 2 == 0:                       
                raise Exception("invalid Markdown syntax")
            #print(f"This is the split text: {node}")
            for i in range(len(pieces)):
                if pieces[i] == "":
                    continue
                if i % 2 == 0:  
                    node_type = TextType.TEXT  
                else:
                    node_type = text_type                    

                new_nodes.append(TextNode(pieces[i], node_type))

    return new_nodes

def extract_markdown_images(text):
    #![alt text for image](url/of/image.jpg)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    #This is a paragraph with a [link](https://www.google.com).
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:   
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue        
        images = extract_markdown_images(old_node.text)  # extract all images
        text = old_node.text
        pieces = []

        for image in images:
            delimiter = f"![{image[0]}]({image[1]})"    # Markdwon Image
            parts = text.split(delimiter, 1)            # Split around it, at most once
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")

            # Add text before the image as a TextNode if it exists
            if parts[0]:
                pieces.append(TextNode(parts[0], TextType.TEXT))

            text = parts[1]

            pieces.append(TextNode(image[0], TextType.IMAGE, image[1]))

        if text:  # checks if string is empty
            pieces.append(TextNode(text, TextType.TEXT))   

        new_nodes.extend(pieces)         

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:   
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue        
        links = extract_markdown_links(old_node.text)  
        text = old_node.text
        pieces = []

        for link in links:
            delimiter = f"[{link[0]}]({link[1]})"    
            parts = text.split(delimiter, 1)    
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")        

            if parts[0]:
                pieces.append(TextNode(parts[0], TextType.TEXT))

            text = parts[1]

            pieces.append(TextNode(link[0], TextType.LINK, link[1]))

        if text: 
            pieces.append(TextNode(text, TextType.TEXT))   

        new_nodes.extend(pieces)         

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    splt1 = split_nodes_image([node])
    splt2 = split_nodes_link(splt1)
    splt3 = split_nodes_delimiter(splt2, "**", TextType.BOLD)
    splt4 = split_nodes_delimiter(splt3, "_", TextType.ITALIC)
    splt5 = split_nodes_delimiter(splt4, "`", TextType.CODE)
    return splt5

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


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

    #this is here because the method caused errors when it was placed her, but plcing it 
    # in its own file has fixed those errors somehow
'''