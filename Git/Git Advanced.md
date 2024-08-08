# Git Advanced

## Contents

- [Git Ignore](#git-ignore)
  - [Create .gitignore](#create-gitignore)
  - [Local and Personal Git Ignore Rules](#local-and-personal-git-ignore-rules)
  - [Rules for .gitignore](#rules-for-gitignore)
- [Git Security SSH](#git-security-ssh)
  - [Generating an SSH Key Pair](#generating-an-ssh-key-pair)
- [GitHub and SSH](#github-and-ssh)
  - [Copy the SSH Public Key](#copy-the-ssh-public-key)
  - [Test SSH Connection to GitHub](#test-ssh-connection-to-github)
  - [Add New GitHub SSH Remote](#add-new-github-ssh-remote)

## Git Ignore

When sharing your code, you want some of the files or parts of your project, not be shared. Some examples:

- log files
- temporary files
- hidden files
- personal files

You can specify these files or parts of your project with a `.gitignore` file. Git will not track files and folders specified in `.gitignore` file. However, this file itself is tracked.

### Create .gitignore

Create a new folder with name *Git Ignore Test* and open it with Visual Studio Code.

Open this folder in Git Bash and initialize Git there.

```Bash
git init
```

Create a new `cpp` file and write any codes you want. You can notice that `VS Code` automatically creates a new folder called `.vscode`.

For example, we don't want this folder to be tracked by git.

Go to the root of your local Git and create a `.gitignore` file:

```Bash
touch .gitignore
```

Open this new file add this rule:

```plain
# Ignore ALL files and folders or files within folders with name .vscode
.vscode
```

Save the file and then go to the Git Bash and see the `status` of Git. Since we still didn't commit any files, all the files showed in `status` will be the tracked files.

```Bash
git status
```

Now you can see two important things:

1. `.vscode` folder is not tracked anymore.
2. `.gitignore` file is tracked.

Stage the files and commit them.

```Bash
git add -A
git commit -m "First release of Git Ignore Test"
```

### Local and Personal Git Ignore Rules

Create a new repository in GitHub with name `Git Ignore Test`.

Copy the `URL` provided by GitHub (ending with `.git`) and set it as the `remote` for your local Git.

```Bash
git remote add origin {URL}
```

Create an `upstream` branch for the current branch and push to it.

```Bash
git push --set-upstream origin main
```

Now go to the `remote` repository on GitHub. You can see the `.vscode` folder is not there, but `.gitignore` file is.

Anyone working on your repository now can benefit from `.gitignore` file. However, it is possible that you wanted to prevent the Git from tracking a personal file or folder. Anyone can **see** the name of files and folders ignored by Git here and we don't want it sometimes.

Create a new local file like `Janie.txt`. We don't want anyone on GitHub see that a file with name `Janie` was existed.

You can see that Git knows `Janie.txt` is there.

``` Bash
git status
```

Go to the `.git/info/exclude` file. Notice that `.git` folder is hidden. At the end of the file, add this rule:

``` Bash
Janie.txt
```

Now get `status` again and see that Git has excluded this file to be tracked. Try to `push` the local branch. You can see that there is nothing to `push`.

### Rules for .gitignore

Here are the general rules for matching patterns in .gitignore files:

| Pattern | Explanation/Matches | Examples |
| - | - | - |
| | Blank lines are ignored | |
| # text comment | Lines starting with # are ignored | |
| *name* | All *name* files, *name* folders, and files and folders in any *name* folder | /name.log <br/> /name/file.txt <br/> /lib/name.log |
| *name*/ | Ending with / specifies the pattern is for a folder. <br/> Matches all files and folders in any *name* folder | /name/file.txt <br/> /name/log/name.log <br/><br/> **no match:** <br/> /name.log |
| *name.file* | All files with the *name.file* | /name.file <br/> /lib/name.file
| /name.file | Starting with / specifies the pattern matches only files in the root folder | /name.file <br/><br/> **no match:** <br/> /lib/name.file |
| lib/name.file | Patterns specifiing files in specific folders are always realative to root (even if you do not start with / ) | /lib/name.file <br/><br/> **no match:** <br/> name.file <br/> /test/lib/name.file |
| **/*lib*/*name.file* | Starting with ** before / specifies that it matches any folder in the repository. Not just on root. | /lib/name.file <br/> /test/lib/name.file |
| **/*name* | All *name* folders, and files and folders in any *name* folder | /name/log.file <br/> /lib/name/log.file <br/> /name/lib/log.file |
| /*lib*/**/*name* | All *name* folders, and files and folders in any *name* folder within the *lib* folder. | /lib/name/log.file <br/> /lib/test/name/log.file <br/> /lib/test/ver1/name/log.file <br/><br/> **no match:** <br/> /name/log.file |
| *.*file* | All files withe .*file* extention | /name.file <br/> /lib/name.file |
| **name*/ | All folders ending with *name* | /lastname/log.file <br/> /firstname/log.file |
| *name*?.*file* | ? matches a single non-specific character | /names.file <br/> /name1.file <br/><br/> **no match:** <br/> /names1.file |
| *name*[a-z].*file* | [*range*] matches a single character in the specified range (in this case a character in the range of a-z, and also be numberic.) | /names.file <br/> /nameb.file <br/><br/> **no match:** <br> /name1.file |
| *name*[abc].*file* | [*set*] matches a single character in the specified set of characters (in this case either a, b, or c) | /namea.file <br/> /nameb.file <br/><br/> **no match:** <br/> /names.file |
| *name*[!abc].*file* | [!*set*] matches a single character, except the ones spesified in the set of characters (in this case a, b, or c) | /names.file <br/> /namex.file <br/><br/> **no match:** <br/> /namesb.file |
| *name*/ <br/> !*name*/secret.log | ! specifies a negation or exception. Matches all files and folders in any *name* folder, except *name*/secret.log | /name/file.txt <br/> /name/log/name.log <br/><br/> **no match:** <br/> /name/secret.log |
| *.*file* <br/> !*name*.*file* | ! specifies a negation or exception. All files withe .file extention, except *name*.*file* | /log.file <br/> /lastname.file <br/><br/> **no match:** <br/> /name.file |
| *.*file* <br/> !*name*/*.*file* <br/> *junk*.* | Adding new patterns after a negation will re-ignore a previous negated file<br/>All files with .*file* extention, except the ones in *name* folder. Unless the file name is *junk* | /log.file <br/> /name/log.file <br/><br/> **no match:** <br/> /name/junk.file |

## Git Security SSH

SSH is a secure shell network protocol to use network managment, remote file transfer, and remote system access.

SSH uses keys to encrypt the connections. When generating a key, you will generate a "public" and "private" key.

- Public: The one you share with the remote party.
- Private: The one you keep for yourself.

The public key can be obtained from the private key using some algorithms, but the other way around.

### Generating an SSH Key Pair

Open the Git Bash or Linux terminal and start by creating a new key, using your email as a lable:

```Bash
ssh-keygen -t rsa -b 4096 -C "{email}"
```

You will be asked to enter a directory to store the file: `Enter file in which to save the key (/c/Users/user/.ssh/id_rsa):`

Enter a new directory or enter empty to use the default directory: `/c/Users/user/.ssh/id_rsa`

Then you will be asked for a passphrase: `Enter passphrase (empty for no passphrase):`

Even if someone could access your SSH key, they will still need to know the passphrase you set. You'll need to supply this passphrase every time you use the SSH key.

Now your SSH key is saved in `/c/Users/ghchg/.ssh/id_rsa` or the directory you specified.

First run the SSH-Agent using one of the following commands:

```Bash
eval $(ssh-agent)
eval `ssh-agent -s`
```

Then add the SSH key pair to SSH-Agent:

```Bash
ssh-add {Directory}
```

## GitHub and SSH

### Copy the SSH Public Key

Use `clip <` to copy the public key to your clipboard.

```Bash
clip < /c/Users/user/.ssh/id_rsa.pub
```

In GitHub go to the "Settings" and then "SSH and GPG keys". Now click the "New SSH key" button. Write a title and paste the key. After entering your GitHub password, you can see that your new SSH key is added.

### Test SSH Connection to GitHub

Test your connection to GitHub via SSH.

```Bash
ssh -T git@github.com
```

Enter `yes` and if you see your GitHub username, you have successfully authenticated.

### Add New GitHub SSH Remote

Now we can add a new remote via SSH to our Git. First get the SSH address in [the same way you get the `URL` to clone your remote repository.](Git%20Contribute.md#git-clone-from-github)

Please note that you were using HTTPS connection to set your remote repository before. Now we're going to do it by SSH. It's really good to have a secure way to access your remote, for example on public networks.

First see the current remotes.

```Bash
git remote -v
```

Since you had already pushed your local repo (Git Ignore Test) to GitHub, you should see two `https://` remotes for `fetch` and `pull`.

Now add a new origin using the SSH address that get.

```Bash
git remote add ssh-origin {SSH URL}
```

View your current remotes again. You should see that two `git@github.com:` new remotes are there too. Now every time you wanted to `push` or `pull` from GitHub, you can choose between `origin` (HTTPS) or `ssh-origin` (SSH).

Look at the [Git and Github](Git%20and%20Github.md) commands. The first command says

```Bash
git remote add origin {URL}
```

Actually the name `origin` is what you can choose for the remote. Although it is recommened to follow the conventions, you can still set it as `https-origin` or anything else:

```Bash
git remote add {remote name} {URL}
```

Now know the reason why our SSH remote name is `ssh-origin`.

So each remote has two info:

- Remote Name
- URL

You can change the URL of any remotes. It means you can even change the https URL to SSH URL.

```Bash
git remote set-url {remote name} {new URL}
```

Now we want to change change the `origin` remote from HTTPS to SSH.

```Bash
git remote set-url origin {SSH URL}
```

Use `git remote -v` to check the changes. You can then set the `origin` URL back to the HTTPS.
