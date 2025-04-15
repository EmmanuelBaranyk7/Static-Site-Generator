from markdown_block import markdown_to_html_node
from htmlnode import HTMLNode
import os
import shutil

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
            if line.startswith("# "):
                return line[2:]
    raise ValueError("Invalid markdown syntax")


def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        mrkd = f.read()  # with open... automatically closes the file block
    print(f"markdonw file:\n{mrkd}")
    with open(template_path) as f:
        html_tem = f.read()

    content = markdown_to_html_node(mrkd).to_html()
    title = extract_title(mrkd)

    html_str = html_tem.replace("<title>{{ Title }}</title>", f"<title>{ title }</title>")
    html_str = html_str.replace("<article>{{ Content }}</article>", f"<article>{ content }</article>")

    # Ensure the destination path has its parent directories created
    dir_name = os.path.dirname(dest_path)  # Extract just the directory part of the path
    if dir_name:  # Only create directories if there is one specified
        os.makedirs(dir_name, exist_ok=True)  # Recursively create the directory if it doesn't exist

    # Write the HTML file to the specified destination path
    with open(dest_path, "w") as f:
        f.write(html_str)

    print(f"raw HTML:\n{html_str}")



    