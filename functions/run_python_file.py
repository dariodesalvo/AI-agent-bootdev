import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
      
    working_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    
    if not target_path.startswith(working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_path):
        return f'Error: File "{file_path}" not found.'

    try:
        
        command = ["python", file_path] + args
        
        completed_process = subprocess.run(
        command, 
        cwd=working_path,
        capture_output=True,
        text=True,          
        timeout=30,
        check=False)
        
        stdout_output = completed_process.stdout.strip()
        stderr_output = completed_process.stderr.strip()
        
        output_parts = []

        if stdout_output:
            output_parts.append("STDOUT: " + stdout_output)

        if  stderr_output:
            output_parts.append("STDERR: " + stderr_output)

        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")
        
        if not output_parts:
            return "No output produced."

        final_output = "\n".join(output_parts)
        
        return final_output
    
    except Exception as e:
        return f"Error: executing Python file: {e}"