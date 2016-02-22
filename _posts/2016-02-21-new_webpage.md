---
layout: post
title:  "My New Webpage"
date:   2016-02-21 23:48:00
categories: blog
---

Welcome to my new web page and blog.
This time I've build the page using [jekyll](https://jekyllrb.com/) and using a custom theme, based on bootstrap, by taking some inspirations and HTML/CSS snippets from bootstrap's [blog](https://getbootstrap.com/examples/blog/) and [carousel](https://getbootstrap.com/examples/carousel/) examples.
For the typography I'm using [Open Sans](https://en.wikipedia.org/wiki/Open_Sans) and [Lato](http://www.latofonts.com/) and [Font Awesome](https://fortawesome.github.io/Font-Awesome/) for the icons.
The Publications section was implemented using [Exhibit](http://www.simile-widgets.org/exhibit3/) and taking my publications from [bibsonomy](http://www.bibsonomy.org/user/white_gecko).

The web page has four sections, this one is the “Blog”, where I'm publishing several things which pop into my head.
The “Notes” section should be some kind of an open idea management system resp. personal Wiki.
In the section “Project” I present some project, which I'm working on and finally my “Publications”.

The source code for my homepage is published on github.
On the server side I'm making use of [docker](https://en.wikipedia.org/wiki/Docker_%28software%29), especially a setup of [jwilder's reverse proxy](https://github.com/jwilder/nginx-proxy) and the [dockerjekyllpages](https://github.com/DonMcNamara/dockerfiles/tree/master/dockerjekyllpages) image by Don McNamara to rebuild the blog, triggered by pushes to my git repository.
In addition to the jwilder container, I'm using the [Let's Encrypt companion](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion) by Yves Blusseau, to make the site available via HTTPS.

My webpage is bi-lingual, which means in this case, that I'm sometimes writing text in German and sometimes in English.
I'm if you have problems understanding a text but think, it might be interesting, don't hesitate to ask me for a translation (but I can't guarantee anything).
Currently this page has not too much content, but I'm planning to gradually integrate some interesting posts form my old blog and also build a live integration of my [twitter stream](https://twitter.com/white_gecko).
