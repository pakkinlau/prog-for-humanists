"""
This script was created for converting attached images within a Jupyter notebook to base64. 
By doing that, the images will embedded into the notebook, instead of being attached as a separate file.

Use case: 

"""

import base64
import re
import os

# Function to convert images in a Markdown file to base64
def convert_images_to_base64(file_path):
    with open(file_path, "r") as markdown_file:
        markdown_content = markdown_file.read()

    # this matches use negative lookahead assertion to exclude matches with 'attachment:' prefix 
    image_file_matches = re.findall(r'\!\[.*\]\((?!attachment:)(.*?)\)', markdown_content)
    # The following matches is wrong:  
    # (It is because `![image.png](attachment:image.png)` already indicates the images are embedded in the notebook.)
    # image_file_matches = re.findall(r'\!\[.*\]\(attachment:(.*?)\)', markdown_content)

    for image_url in image_file_matches:
        # Check if the URL starts with 'data:image' indicating it's already in base64 format
        if not image_url.startswith('data:image'):
            with open(image_url, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                # Construct the data URL and replace the image URL in the Markdown content
                data_url = f'data:image/png;base64,{encoded_string}'
                markdown_content = markdown_content.replace(f'![]({image_url})', f'![]({data_url})')

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

