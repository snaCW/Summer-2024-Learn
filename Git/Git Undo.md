# Git Undo

## Contents
- [Git Revert](#git-revert)
    - [Git Revert Find Commit in Log](#git-revert-find-commit-in-log)
    - [Git Revert HEAD](#git-revert-head)
- [Git Reset](#git-reset)
    - [Git Reset Find Commit in Log](#git-reset-find-commit-in-log)
    - [Git Reset Hash](#git-reset-hash)
    - [Git Undo Reset](#git-undo-reset)

## Git Revert
`revert` is a command to take a previous `commit` and add it as a new `commit`. Steps are clear:

1. Find a previous `commit`
2. Use it to make a new `commit`

Delete your `cpp` file in the `Git Ignore Test` local repository. `stage` your changes and `commit` the changes.
```Bash
git add -A
git commit -m "I'm sure I didn't deleted the cpp file"
```

### Git Revert Find Commit in Log
Now we want to return back to the point before the last `commit`. We can find the desired point using `log`.
```Bash
git log
```

Since we only had two `commits`, the list isn't long. However, it is pretty normal for a project to have more than 100 commits. The list will be too long and you will be stuck in the terminal.

Press `SHIFT + G` to go to the end of the list and `q` to exit the current view.

Working with long lists is hard, so we use the `--oneline` option.
```Bash
git log --oneline
```

In each line you can see two data.
- First seven digits of `commit hash`
- the `commit message`

In our case we want to return back to before the `a8372d6 (HEAD -> main) I'm sure I didn't deleted the cpp file` commit. Notice that the `commit hash` is not same in your Git.

### Git Revert HEAD
The last `commit` is always this syntax: `(HEAD -> main, {Branch name merged from})`. Since we didn't `merge` anything, our last `commit` is `(HEAD) -> main`.

This is good, because we can use the `HEAD` keyword to revert back to before the last `commit`.
```Bash
git revert HEAD --no-edit
```

We can use `--no-edit` option to not add a new message for the `revert commit`. The `revert commit` message will be: `Revert "{Revert-from commit message}"`. If this is confusing, just see the message set for the `revert`.

What if we wanted to `revert` to one commit before the last commit? The common mistake is to use `git revert HEAD` two times.

> Please note that after using `git revert HEAD`, you are **committing** the point before the last `commit`. It means the second `commit` will only take you to the last commit!

Use this command to `revert` to the earlier commits:
```Bash
git revert HEAD~{Count of going back}
```

To revert back to the point before the second commit, just use:
```Bash
git revert HEAD~2
```

The total point of `revert` is to **turn back** and **commit**. You can use `reset` to not commit after turning back.

## Git Reset
This is the same as `revert`, we have two steps.

### Git Reset Find Commit in Log
Just use the `log` and find a point to `reset` there.

We want to go to the point before `a8372d6 I'm sure I didn't deleted the cpp file`. So note the `Commit Hash` of the commit before.

### Git Reset Hash
```Bash
git reset {Commit Hash}
```

This command changes the log history in order to set the `Commit Hash` as the last `commit`.

Please do not mess with `reset` especially in remote repositories.

### Git Undo Reset
Even though the commits are no longer showing up in `log`, you can still `reset` to them.

## Git Amend

### Git commit --amend

`commit --amend` is used to modify the most recent `commit`, combining changes in the `staging enviroment` with the latest `commit`. This new `commit` will replace the latest `commit` entirely.

### Git Amend Commit Message

Add a `README.md` file to the `Git Ignore Test`. Then commit the changes with this message: `Added RAEDME.md`. As you can see, the message has a misspelled word.

```Bash
git add -A
git commit -m "Added RAEDME.md"
```

Now check the `log`:

```Bash
git log --oneline
```

We want to change the message of the last `commit`.

```Bash
git commit --amend -m "Added README.md"
git log --oneline
```

Now you should be able to see how `amend` worked to change the message of the last `commit`.

> With `amend` you can mess with a repository log. Please be careful about using it.

### Git Amend Files

Now write something in the `README.md` file and `commit`.

```Bash
git add -A
git commit -m "Updated README.md"
```

Now change the contents of `README.md` to your desire and then use `amend`.

```Bash
git add README.md
git commit --amend -m "Added and Updated README.md"
git log --oneline
```

Now you can see how you used `amend` to change the last `commit`.