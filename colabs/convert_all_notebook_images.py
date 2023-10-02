import base64
import re
import os

# Function to convert images in a Markdown file to base64
def convert_images_to_base64(file_path):
    with open(file_path, "r") as markdown_file:
        markdown_content = markdown_file.read()

    image_file_matches = re.findall(r'\!\[.*\]\((.*?)\)', markdown_content)

    for image_file_name in image_file_matches:
        with open(image_file_name, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            markdown_content = markdown_content.replace(f'![Alt text]({image_file_name})', f'![Alt text](data:image/png;base64,{encoded_string})')

    with open(file_path, "w") as markdown_file:
        markdown_file.write(markdown_content)

# Directory containing Jupyter notebooks
notebook_directory = os.getcwd()

# Iterate through all files in the directory
for root, dirs, files in os.walk(notebook_directory):
    for file in files:
        if file.endswith(".ipynb"):
            notebook_file_path = os.path.join(root, file)
            convert_images_to_base64(notebook_file_path)
