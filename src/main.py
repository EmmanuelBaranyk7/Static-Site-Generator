import os, shutil
from copy_static import copy_content_to_destination
from generate_page import generate_page

def main():
    source_dir = "static"
    destination_dir = "public"

    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    
    copy_content_to_destination(source_dir, destination_dir)

    # Walk through all files in the `content/` directory.
    for subdir, _, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                # Construct source and destination paths
                source_path = os.path.join(subdir, file)  # Full path to the markdown file
                relative_path = os.path.relpath(os.path.join(subdir, file), "content")
                destination_path = os.path.join(destination_dir, relative_path.replace(".md", ".html"))

                # Ensure the output directory exists
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                # Generate the HTML file
                generate_page(source_path, "template.html", destination_path)
    generate_page("content/index.md", "template.html", "public/index.html")

main()