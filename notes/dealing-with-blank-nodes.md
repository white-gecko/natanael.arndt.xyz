---
layout: page
parent: notes
title: Dealing with Blank Nodes
description: "Blank Nodes are easy to introduce but hard to handle."
date:   2018-12-12 12:00:00
update: 2018-12-12 12:00:00
---

## Introduction
*Blank Nodes* or *BNodes* are nodes in an RDF graph which can not be globaly identified e.g. using an IRI.
They can be identified within a context or skope using *blank identifiers*.
Since RDF is a data format to exchange information this is a problem because the context changes as the data is transmitted.

The [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/#section-skolemization) states: *Blank nodes do not have identifiers in the RDF abstract syntax. The blank node identifiers introduced by some concrete syntaxes have only local scope and are purely an artifact of the serialization.*
The best thing one can do is to avoid blank nodes and replace them by IRIs - give those vampires and identity so they can be seen in a mirror.
To replace a blank node by an IRI is called [*skolemizing*](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/#section-skolemization).
