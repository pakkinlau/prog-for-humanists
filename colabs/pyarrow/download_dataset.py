import datasets

dataset_id = "alturing/gutenberg-texts"

# Load the dataset by name
dataset = datasets.load_dataset(dataset_id)

# Download the dataset files
print(dataset)

""" 
DatasetDict({
    train: Dataset({
        features: ['title', 'author', 'text', 'language'],
        num_rows: 2951
    })
})

"""

# Save the dataset to a local folder
local_folder_path = r"C:\Users\kinla\Documents\All_github_repo\datasets\gutenberg"
dataset.save_to_disk(local_folder_path)

