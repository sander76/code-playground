# remove local branches which are no longer on remote.

https://stackoverflow.com/a/47939403/1629704

- git fetch --prune (or git fetch -p, which is an alias, or git prune remote origin which does the same thing without fetching, and is probably not what you want most of the time).
- Note any remote branches that are reported as deleted. Or, to find them later on, git branch -v (any orphaned tracking branch will be marked "[gone]").
- git branch -d [branch_name] on each orphaned tracking branch

https://stackoverflow.com/questions/17983068/delete-local-git-branches-after-deleting-them-on-the-remote-repo


## remove tracked files

```
git rm --cached <filename>
git commit -m "<Message>"
```

more info: https://www.baeldung.com/ops/git-remove-tracked-files-gitignore
