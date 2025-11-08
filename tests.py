from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
    
def _show(label, directory):
    print(f"get_files_info('calculator', '{directory}'):")
    print(get_files_info("calculator", directory))
    print()

def _showFile(label,file):
    print(get_file_content(label,file))
    print()


if __name__ == "__main__":
    #_show("current directory", ".")
    #_show("'pkg' directory", "pkg")
    #_show("'/bin' directory", "/bin")
    #_show("'../' directory", "../")
    _showFile('calculator', 'main.py')
    _showFile('calculator', 'pkg/calculator.py')
    _showFile('calculator', '/bin/cat')
    _showFile('calculator', 'pkg/does_not_exist.py')
