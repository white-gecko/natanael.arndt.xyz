---
layout: post
title: Docker Jekyll Pages Release 0.2.0
tags: ["docker", "jekyll", "static", "git"]
date:   2017-06-21 17:00:00+02:00
---
Since I've forked the *dockerjekyllpages* from [DonMcNamara/dockerfiles](https://github.com/DonMcNamara/dockerfiles/tree/master/dockerjekyllpages) just over a year ago to run my blog I've done some changes – improvements in my eyes.
To make them usable for others I frequently built the image on the [docker hub](https://hub.docker.com/r/whitegecko/dockerjekyllpages/) and now even tagged release **0.2.0** on [GitHub](https://github.com/white-gecko/dockerjekyllpages/releases/tag/0.2.0) as well as on the [docker hub](https://hub.docker.com/r/whitegecko/dockerjekyllpages/tags/).

Changes include:

* Update base image, ruby and thus jekyll
* Reorganize file structure
* NGINX: also serve pages without .html
* NGINX: deliver 404 status codes
* NGINX: serve custom 404 pages
* Build process: install dependencies from Gemfile
* Build process: specify branch to checkout
* Build process: build from volume
* Update README

My planes for the future can be seen in the [issue tracker](https://github.com/white-gecko/dockerjekyllpages/issues).

Feel free to use the container and and send me pull requests or just write issues.
