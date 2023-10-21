import os
import subprocess

def get_most_changed_text_file(repo_path):
    # Get the list of all text files in the repository
    text_files = []
    git_cmd = ["git", "ls-files", "--full-name", "--", "*.txt"]  # Change the pattern to match your text files
    git_process = subprocess.Popen(git_cmd, cwd=repo_path, stdout=subprocess.PIPE)
    output, _ = git_process.communicate()

    # Decode the output and split it into lines
    text_files = output.decode().splitlines()

    # Handle the case where no text files are found
    if not text_files:
        return None, 0

    # Calculate the number of commits that modified each text file
    commit_counts = {}
    for text_file in text_files:
        git_cmd = ["git", "log", "--oneline", "--", text_file]
        git_process = subprocess.Popen(git_cmd, cwd=repo_path, stdout=subprocess.PIPE)
        output, _ = git_process.communicate()
        commit_count = len(output.decode().splitlines())
        commit_counts[text_file] = commit_count

    # Find the most changed text file
    most_changed_file = max(commit_counts, key=commit_counts.get)
    return most_changed_file, commit_counts[most_changed_file]

# Example usage
repo_path = os.getcwd()
most_changed_file, commit_count = get_most_changed_text_file(repo_path)

if most_changed_file is not None:
    print(f"The most changed text file is '{most_changed_file}' with {commit_count} commits.")
else:
    print("No text files found in the repository.")
