import os
import subprocess
from datetime import datetime, timedelta

# 7x52 grid
pattern = [
    # ALEX WAS HERE
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],  # Row 1 (Sunday)
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Row 2 (Monday)
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Row 3 (Tuesday)
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],  # Row 4 (Wednesday)
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Row 5 (Thursday)
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Row 6 (Friday)
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]   # Row 7 (Saturday)
]

# Starting date (adjust this to a suitable Sunday in 2025)
start_date = datetime(2024, 1, 7)  # Adjust to fit your timeline

# File to update with the commit date
file_to_update = "commit_log.txt"

# Function to update the file with the current commit date
def update_file_with_date(commit_date):
    with open(file_to_update, "a") as f:
        f.write(f"# Commit made on: {commit_date.strftime('%Y-%m-%d')}\n")

# Function to run git commit with a specific date
def make_commit(commit_date):
    commit_message = f"Commit on {commit_date.strftime('%Y-%m-%d')}"
    os.environ['GIT_AUTHOR_DATE'] = commit_date.isoformat()
    os.environ['GIT_COMMITTER_DATE'] = commit_date.isoformat()
    update_file_with_date(commit_date)  # Update the file with the commit date
    subprocess.run(['git', 'add', file_to_update])
    subprocess.run(['git', 'commit', '--allow-empty', '-m', commit_message])

# Iterate over the pattern and make commits on the respective dates
for week in range(len(pattern[0])):
    for day in range(7):
        if pattern[day][week] == 1:
            commit_date = start_date + timedelta(weeks=week, days=day)
            make_commit(commit_date)

# Push the changes
subprocess.run(['git', 'push', 'origin', 'main'])