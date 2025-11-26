from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
    
def _show(label, directory):
    print(f"get_files_info('calculator', '{directory}'):")
    print(get_files_info("calculator", directory))
    print()

def _showFile(label,file):
    print(get_file_content(label,file))
    print()

def _writeFile(directory, file, content):
    print(write_file(directory, file, content))
    print()


if __name__ == "__main__":
    #_show("current directory", ".")
    #_show("'pkg' directory", "pkg")
    #_show("'/bin' directory", "/bin")
    #_show("'../' directory", "../")
    #_showFile('calculator', 'main.py')
    #_showFile('calculator', 'pkg/calculator.py')
    #_showFile('calculator', '/bin/cat')
    #_showFile('calculator', 'pkg/does_not_exist.py')
    #_writeFile("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #_writeFile("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #_writeFile("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    print(run_python_file("calculator", "lorem.txt"))