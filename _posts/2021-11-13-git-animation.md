---
layout: post
title: "Animate the History of your Git Repository"
tags: ["Git", "Animation"]
date: 2021-11-13 20:09:00+02:00
---

I was looking for a way to get an impression of the temporal development of my git repository.
So I chose to check for ways to animate the history of a git repository.

I found some DIY approach that should provide very nice results, but it requires some more effort.
Basically you iterate through all of your commits, execute a command to visualize this commit, what ever that means to you, and then merge all of these visualizations as frames together as a movie file.
The exect steps are here: [http://eptcomic.com/ept1movie.htm](http://eptcomic.com/ept1movie.htm).

Another tool is Gource ([https://gource.io/](https://gource.io/)).
It renders your repository in a 3D animation, that looks quite fancy.
A good startingpoint is:

    $ apt install gource
    $ gource -c 4.0 -s 1 -a 1 .

The major difference between the two tools and their results is, that with the first on you can visualize the content of the repository as it evolves, while the Gource mainly visualizes the file structure and the collaboration process on it.

(This post was originally started on 2020-10-18)
