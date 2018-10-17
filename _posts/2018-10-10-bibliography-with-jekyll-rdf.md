---
layout: post
title: "My Bibliography with Jekyll RDF"
tags: ["JekyllRDF", "Jekyll", "RDF", "Bibliography", "Bibtex"]
date: 2018-10-10 15:10:00+02:00
---

From now on the list of [my publications](/publications) is rendered using Jekyll-RDF. I've used the [bibtex2rdf](http://bibtex2rdf.sourceforge.net/) script together with a [customized mapping](https://github.com/white-gecko/natanael.arndt.xyz/blob/master/_data/schema.map) to convert my [bibtex file](https://www.bibsonomy.org/bib/user/white_gecko) to [RDF](https://github.com/white-gecko/natanael.arndt.xyz/blob/master/_data/bib.ttl).
This file is consumed by [JekyllRDF](https://github.com/white-gecko/jekyll-rdf) and rendered together with the rest of my blog using the [publications template](https://github.com/white-gecko/natanael.arndt.xyz/blob/master/publications.html) for the lost of all publications and an [additional template](https://github.com/white-gecko/natanael.arndt.xyz/blob/master/_layouts/publication.html) to render a page for each individual publication resource.
