import os
import shutil

def copy_content_to_destination(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        raise Exception(f"not a valid src directory: {source_dir}")
    if os.path.isfile(source_dir):
        return None
    
    dest_dir = os.path.join(destination_dir, "", "")
    if os.path.exists(destination_dir):          
        shutil.rmtree(destination_dir)
        print(f"removed directory: {dest_dir}")
    
    
    #current_dir = os.listdir(path=".")
    print(f"current directory: {source_dir}")

    
    for item in os.listdir(source_dir):
        print(f"item: {item}")
        c_path = os.path.join(source_dir, "", item)
        print(f"path: {c_path}")
        d_path = os.path.join(dest_dir, "", item)
        print(f"destination path: {d_path}")    

        try:
            os.mkdir(dest_dir)  
            print(f"Directory {dest_dir} created successfully!")
        except FileExistsError:
            print(f"Directory {dest_dir} already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        if os.path.isfile(c_path):      
            print(f"copying item: {item} to d_path: {dest_dir}")
            shutil.copy(c_path, d_path)
            print(f"copied item")
        else:
            print(f"trying recusion...")
            copy_content_to_destination(c_path, d_path)
            print(f"recursion successful!")
    
   
