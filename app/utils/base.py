import toml
import os

def get_version():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '../../'))
    pyproject_path = os.path.join(project_root, 'pyproject.toml')

    if not os.path.exists(pyproject_path):
        raise FileNotFoundError(f"No se encontró el archivo {pyproject_path}")

    with open(pyproject_path, 'r') as pyproject_file:
        pyproject_content = toml.load(pyproject_file)

    version = pyproject_content['tool']['poetry']['version']
    return version