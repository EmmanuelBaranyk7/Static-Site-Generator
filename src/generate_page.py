from markdown_block import markdown_to_html_node
from htmlnode import HTMLNode
import os
import shutil

def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        lines = block.split("\n")
        for line in lines:
            if line:
                if line[0:2] == "# ":
                    return line[1:].strip()
            raise ValueError("Invalid markdown syntax")
    return None

def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    print(f"reading markdown from path: {from_path}...")
    with open(from_path) as f:
        mrkd = f.read()  # with open... automatically closes the file block
    print("markdown read successfully!")

    print(f"opening template from {template_path}...")
    with open(template_path) as f:
        html_tem = f.read()
    print("template read successfully!")

    print("creating content...")
    content = markdown_to_html_node(mrkd).to_html()
    print("success!")
    print("extracting title...")
    title = extract_title(mrkd)
    print("success!")

    print("modifing html...")
    html_str = html_tem.replace("<title>{{ Title }}</title>", f"<title>{ title }</title>")
    html_str = html_str.replace("<article>{{ Content }}</article>", f"<article>{ content }</article>")
    print("success!")

    print("writing new Html page...")
    target_path = ""
    if not os.path.exists(dest_path):
        paths = dest_path.split("/")
        print("still wrting...")
        for path in paths:
            target_path += f"/{path}"
            if not os.path.exists(target_path):
                print("STILL WRITING...")
                if not os.path.isfile(path):
                    os.mkdir(target_path)
                
    print(f"opening path at: {target_path}")
    with open(target_path, "w") as f:
        f.write(html_str)
    print("Html written successfully")



    