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


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        mrkd = f.read()  # with open... automatically closes the file block
    with open(template_path) as f:
        html_tem = f.read()

    content = markdown_to_html_node(mrkd).to_html()
    title = extract_title(mrkd)

    html_str = html_tem.replace("{{ Title }}", title)
    html_str = html_str.replace("{{ Content }}", content)
    html_str = html_tem.replace('href="/', f'href="{basepath}')
    html_str = html_str.replace('src="/', f'src="{basepath}')

    # Ensure the destination path has its parent directories created
    dir_name = os.path.dirname(dest_path)  # Extract just the directory part of the path
    if dir_name:  # Only create directories if there is one specified
        os.makedirs(dir_name, exist_ok=True)  # Recursively create the directory if it doesn't exist

    # Write the HTML file to the specified destination path
    with open(dest_path, "w") as f:
        f.write(html_str)

    #print(f"raw HTML:\n{html_str}")

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path_content):
        raise ValueError("invalid dir_path")
    if os.path.isfile(dir_path_content):
        return None
    
    print(f"looping through each entry in: {dir_path_content}")
    for entry in os.listdir(dir_path_content):
        source = os.path.join(dir_path_content, entry)
        print(f"source: {source}")
        dest = os.path.join(dest_dir_path, entry)
        print(f"dest: {dest}")

        if os.path.isfile(source):
            print(f"found md file, generating...")
            html_dest = dest.replace("md", "html")
            generate_page(source, template_path, html_dest, basepath)
        else:
            generate_page_recursive(source, template_path, dest, basepath)
