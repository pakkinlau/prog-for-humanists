import base64
import re

# Read the Markdown content from a file or a string (replace 'your_markdown_file.md' with your actual file path)
with open("your_markdown_file.md", "r") as markdown_file:
    markdown_content = markdown_file.read()

# Extract the image file name from the Markdown content using regular expression
image_file_name = re.search(r'\!\[.*\]\((.*)\)', markdown_content).group(1)

# Read and encode the image file to base64
with open(image_file_name, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Replace the original Markdown content with the base64 encoded image
new_markdown_content = re.sub(r'\!\[.*\]\((.*)\)', f'![Alt text](data:image/png;base64,{encoded_string})', markdown_content)

# Write the updated Markdown content back to the file
with open("your_markdown_file.md", "w") as markdown_file:
    markdown_file.write(new_markdown_content)
