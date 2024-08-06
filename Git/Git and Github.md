# Git Commands

| Command | Description |
| - | - |
| `git remote add origin {URL}` | Add a remote repository with {URL} as the origin to your local Git repo. |
| `git push --set-upstream origin {branch name}` | Push "master" or "main" to the {URL} and set it as the default remote branch if {branch name} is "master" or "main". |
| `git fetch origin` | Get all the change history of the origin. |
| `git log origin/master` | View a history of commits in origin/master. |
| `git diff origin/master` | Vies the differences between local master and origin/master. |
| `git merge origin/master` | Merge the origin/master with the current branch. |
| `git pull origin` | Update the local Git from origin. A combination of `fetch` and `merge`. |
| `git pull` | Update the local Git from origin. A combination of `fetch` and `merge`. |
| `git push origin` | Push the local Git to origin. |
| `git branch -a` | Display all the local and remote branches. |
| `git branch -r` | Display all the remote branches. |
| `git push origin {Branch Name}` | Push {Branch Name} branch to the origin at remote server. |