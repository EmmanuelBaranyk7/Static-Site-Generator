import os
import shutil

def copy_content_to_destination(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        raise Exception(f"not a valid src directory: {source_dir}")
    
    if os.path.isfile(source_dir):  # base case
        return None
    
    if os.path.exists(destination_dir):          
        shutil.rmtree(destination_dir)  

    os.mkdir(destination_dir)  
  
    for item in os.listdir(source_dir):  # iteratethrough items in source dir
        c_path = os.path.join(source_dir, item)
        d_path = os.path.join(destination_dir, item)   
        
        if os.path.isfile(c_path):      # if file, copy directly
            shutil.copy(c_path, d_path)
            print(f"copied path: {c_path} to: {d_path}")
        else:
            copy_content_to_destination(c_path, d_path)    # if dir, copy contents recursively
    
   
