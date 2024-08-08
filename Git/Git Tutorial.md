# Git Commands

| Command | Description |
| - | - |
| `git --version` | Get the installed version number. |
| `git config user.name "{username}"` | Set {username} as username for the current repo. |
| `git config --global user.name "{username}"` | Set {username} as username for all the repos. |
| `git config --global user.email "{email}"` | Set {email} as email for the current repo. |
| `git config --global user.email "{email}"` | Set {email} as username for all the repos. |
| `mkdir {directory}` | Make a new directory named {directory}. |
| `cd {directory}` | Navigate to {directory}. |
| `git init` | Initialize Git on the current directory. |
| `ls` | List all the files in the current directory. |
| `git status` | Display the status of Git in the current directory. |
| `git status --short` | Display the compact status of Git in the current directory.<br/>Flags:<br/>?? - Untracked files<br/>A - Files added to stage<br/>M - Modified files<br/>D - Deleted files|
| `git add {file name}` | Add the {file name} file to Git (Staging). |
| `git add --all` | Add all of the files in the current directory (Staging all the changes). |
| `git add -A` | Add all of the files in the current directory (Staging all the changes). |
| `git commit -m "{message}"` | Commit all the staged files to Git with {message} as description. |
| `git commit -a -m "{message}"` | Skip the staging process and directly commit the changes with {message} as description. |
| `git log` | View a history of commits. |
| `git {command} -help` |  See all the available options for the {command} command. |
| `git {command} --help` |  See all the available options for the {command} command, opening Git manual page. |
| `git help --all` |  See all possible commands. |
| `SHIFT + G` | Go to the end of the displayed list. |
| `q` | Exit the current view. |
| `git branch {branch name}` | Create a branch named {branch name} based on the current branch files. |
| `git branch` | Display all the branches. |
| `git checkout {branch name}` | Move to the branch named {branch name}.<br/>Default name for the main branch is "master" or "main".|
| `git checkout -b {branch name}` | Create a branch named {branch name} and move to it. |
| `git merge {branch name}` | Merge the {branch name} branch with the current branch. |
| `git branch -d {branch name}` | Delete the {branch name} branch. |
