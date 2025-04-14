import os, shutil
from copy_static import copy_content_to_destination
from generate_page import generate_page

def main():
    source_dir = "static"
    destination_dir = "public"

    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_content_to_destination(source_dir, destination_dir)
    generate_page("content/index.md", "template.html", "public/index.html")

main()