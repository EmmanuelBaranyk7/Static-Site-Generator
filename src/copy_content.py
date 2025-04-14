import os
import shutil

def copy_content_to_destination(source_dir, destination_dir):
    os.path.rmtree(destination_dir)
    if not os.path.exists(source_dir):
        raise Exception(f"not a valid src directory: {source_dir}")
    
    current_dir = os.listdir(path=".")
    print(f"current directory: {current_dir}")
    
    for item in os.listdir(source_dir):
        print(f"item: {item}")
        path = os.path.join(current_dir, "", item)
        print(f"path: {path}")
        if os.path.isfile(item):
            print(f"copying item...")
            shutil.copy(item, path)
            print(f"copied item")
        else:
            try:
                copy_content_to_destination(current_dir, os.mkdir(path))
            except FileExistsError:
                print("directory already exists")
            except Exception as e:
                print(f"An error occurred: {e}")
   
