---
layout: post
title: "Cherry pick files from a commit in a repository"
tags: ["Git", "cherry pick"]
date: 2024-03-01 14:13:00+01:00
---

In git there is the command [`git cherry-pick`](https://git-scm.com/docs/git-cherry-pick) that allows to “apply the changes introduced by some existing commits”.
This is nice if you want to reorder entire commits or things like that.

I often have the use case that I want to see individual files side-by-side to compare them or overwrite files with a previous version, your might have more precise use cases in mind.
At the beginning I thought `git cherry-pick` is the command I was looking for but I sound found out, it is not. So I went back, often to the GitHub web interface and just browsed the history and then the file tree to view the file at a certain state.

But since `git` has a very nice object storage I found out, that I can get any object with `git show ${object_id}` resp. `git show --format=raw ${object_id}`. An object can be a commit, a tree (directory), or a blob (file). So I needed to get the object id of the blob that I want to see. This can be done with `git ls-tree` command resp. to just get the specific id of the file I'm looking for: `git ls-tree --object-only -r ${commit} ${file}`.

All to gather I have put this into these lines, which you can find at [https://github.com/white-gecko/git-cherry-file](https://github.com/white-gecko/git-cherry-file):

```bash
#!/bin/sh
## Done by Natanael 2023-01-31
# see also: https://stackoverflow.com/a/42623347/414075
commit=$1
file=$2
target_file=${3:-${file}.cherry}
echo "Pick ${file} from commit ${commit}"
file_id=$( git ls-tree --object-only -r ${commit} ${file} )
echo "It has the object id ${file_id}"
git show --format=raw ${file_id} > ${target_file}
echo "Written to ${target_file}"
```

Just make it executable and put it into your path, e.g. `~/.local/bin/git-cherry-file` and call it with:


```bash
$ git-cherry-file HEAD~2 README.md
```

It will create a new file `README.md.cherry`. If you want to specify the target path you can add it as an additional argument, e.g. to overwrite the current file:

```bash
$ git-cherry-file HEAD~2 README.md README.md
```

I hope you like it.
