import os

def get_files_info(working_directory, directory="."):
    
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_path =os.path.abspath(working_directory)
    
    if not os.path.isdir(working_path):
        return f'Error: "{directory}" is not a directory'
    
    if not full_path.startswith(working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    content = os.listdir(full_path)
    
    files=""
    
    for file in content:
        file_path = os.path.join(full_path, file)
        try:
            files += f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isfile(file_path)}\n'
        except Exception as e:
                return f"Error: {e}"
            
    return files