import os
import logging
from pathlib import Path

# Configure logging to display INFO level messages with a timestamp
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


class Template:

    def __init__(self, list_of_files):
        self.list_of_files = list_of_files

    def create_files(self):
        # Iterate over each file path in the list
        for filepath in self.list_of_files:
            # Convert the file path to a Path object for manipulation
            filepath = Path(filepath)
            filedir, filename = os.path.split(filepath)

            try:
                # Check if the directory is not empty (not root directory)
                if filedir and filedir not in ['.', '..']:
                    os.makedirs(filedir, exist_ok=True)
                    logging.info(f"Creating directory: {filedir} for the file: {filename}")

                # Check if the file doesn't exist or is empty
                if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
                    with open(filepath, "w") as f:
                        pass
                    logging.info(f"Creating empty file: {filepath}")

                else:
                    logging.info(f"{filename} already exists")
            except PermissionError:
                logging.error(f"Permission denied: Unable to create file/directory {filepath}")


# List of file paths to be created
files_to_create = [
    "src/__init__.py",
    "src/load_pdf.py",
    "src/chunk.py",
    "src/models.py",
    "src/vector_db.py",
    "src/prompt.py",
    "model/instruction.txt",
    "requirements.txt",
    "setup.py",
    "research/trials_notebook.ipynb",
    "chain.py",
]

# Create an instance of the Template class with the list of files
template_instance = Template(files_to_create)
# Call the create_files method to create the specified files
template_instance.create_files()
