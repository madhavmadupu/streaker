from datetime import datetime
from git import Repo

# Path to your local repository
repo_path = '/path/to/your/repo'

# Initialize a repository object
repo = Repo(repo_path)

# Get the current branch
branch = repo.active_branch

# Make changes and commit
with open(f'{repo_path}/example_file.txt', 'a') as file:
    file.write('Adding content to file\n')

# Stage changes
repo.index.add(['example_file.txt'])

# Commit the changes with today's date
commit_date = datetime.now()  # Use the current date and time
commit_message = 'Adding content to file'
repo.index.commit(commit_message, author_date=commit_date, author='Your Name', committer='Your Name')

# Push the changes to remote
origin = repo.remote(name='origin')
origin.push(branch)