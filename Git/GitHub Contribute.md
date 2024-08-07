# GitHub Contribute

## Contents
- [GitHub Fork](#github-fork)
- [Git Clone from GitHub](#git-clone-from-github)
- [GitHub Send Pull Request](#github-send-pull-request)

## GitHub Fork
A `fork` is a copy of a repository. `fork` is not available in Git, it's something only in GitHub and other repository hosts.

## Git Clone from GitHub
A `clone` is a full copy of a repository, including all logging and versions of files.

To `clone` a repository at GitHub, you click on the green "Code" button and get the `URL`. Then open your Git bash and `clone` the repository:
```
git clone {URL}
```

By looking at your file system, you can see the new directory by `ls` and then navigate to the directory by `cd`.

Now use `git remove -v` to see whose origin this repository is connected. As you can see, the origin refers to the original repository, not the one we `fork`ed.

What we're going to do is to rename the original `remote` to something else like `upstream` and then set our own remote `fork` repository ad `origin`.
```
git remote rename origin upstream
git remote -v
```

You can see the name for `remote` repository changed to `upstream`.

Copy the `URL` from your `fork` repository and write these commands:
```
git remote add origin {URL}
git remote -v
```

Now we have two remotes:
- `origin`: our own `fork`, where we have read and write access.
- `upstream`: the original, where we have read-only access.

According to conventions, it's better to name your own `fork` as `origin` and the original as `upstream`.

## GitHub Send Pull Request
After making changes to your local Git, it's time to `push` them to your GitHub `fork`.
```
git push origin
```

Go to GitHub and see the new commit on the repository. Click on the `pull request` and `create pull request` with the necessery messages.

Now any member with write access to the original repository can view the Pull Request and `merge`.