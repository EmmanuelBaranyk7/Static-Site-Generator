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
        pieces = old_node.text.split("[").split("]").split("(").split(")")
        if len(pieces) % 2 != 0:                       
                raise Exception("invalid Markdown syntax")
        #for i in range(len(pieces)):
        #if len(pieces) % 4 == 0:
        new_nodes.append(TextNode(pieces[0], TextType.TEXT))
        new_nodes.append(TextNode(pieces[1], TextType.LINK, pieces[2]))
        new_nodes.append(TextNode(pieces[3], TextType.TEXT))
        new_nodes.append(TextNode(pieces[4], TextType.LINK, pieces[5]))


            
        image = extract_markdown_images(old_node.text)
        link = extract_markdown_links(old_node.text)
    



def split_nodes_link(old_nodes):
    pass




