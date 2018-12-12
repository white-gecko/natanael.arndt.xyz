---
layout: page
parent: notes
title: Dealing with Blank Nodes
description: "Blank Nodes are easy to introduce but hard to handle."
date:   2018-12-12 12:00:00
update: 2018-12-12 12:34:00
---

## Introduction
*Blank Nodes* or *BNodes* are nodes in an RDF graph which can not be globaly identified e.g. using an IRI.
They can be identified within a context or skope using *blank identifiers*.
Since RDF is a data format to exchange information this is a problem because the context changes as the data is transmitted.
In general the RDF concept is very simple, you can build big graphs–as big as the Web– to encode huge amounts of knowledge by making simple triples.
But as soon as there are blank nodes you have to go the extra mile. (Things could be easy.)

The [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/#section-skolemization) states: *Blank nodes do not have identifiers in the RDF abstract syntax. The blank node identifiers introduced by some concrete syntaxes have only local scope and are purely an artifact of the serialization.*
The best thing one can do is to avoid blank nodes and replace them by IRIs–give those vampires and identity so they can be seen in a mirror.
To replace a blank node by an IRI is called [*skolemizing*](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/#section-skolemization).

## How to handle Triples with Blank Nodes
But what to do if you have blank nodes in your graph and you have to or want to preserv them?
There are a various proposals which introduce the concepts of *RDF Molecules*, *Atomic Graphs*, and *Minimum Self-Contained Graph* (MSG). They are very different in their approach of defining it but basically all say the same.

### RDF molecule
([Tracking RDF Graph Provenance using RDF Molecules](http://hdl.handle.net/11603/12181), 2005; [other version](https://ebiquity.umbc.edu/paper/html/id/263/Tracking-RDF-Graph-Provenance-using-RDF-Molecules))

***RDF graph decomposition (preliminary for RDF molecule)***: An RDF graph decomposition consists of three elements *(W, d, m)*: the background ontology *W*, the decompose operation *d(G, W)* which breaks an RDF graph *G* into a set of sub-graphs *Ĝ = {G1, G2, …, Gn}* using *W*, and the merge operation *m(Ĝ, W)* which combines all elements in *Ĝ* into the a unified RDF graph *G'* using *W*. In addition, a decomposition must be *lossless* such that,

for any RDF graph *G*, *G = m(d(G, W), W)*.

When the elements in *Ĝ* are disjoint, *Ĝ* is called an partition of *G*.

**RDF molecule**: RDF molecules are the decomposition result of an RDF graph *G*. They are the finest and lossless sub-graph of *G* according to an decomposition *(W, d, m)*.

### Atomic Graph
([A Versioning and Evolution Framework for RDF Knowledge Bases](https://doi.org/10.1007/978-3-540-70881-0_8), 2006;  [PDF](http://www.informatik.uni-leipzig.de/~auer/publication/PSI-evolution.pdf))

**Atomic Graph**: A graph is called atomic if it can not be split into two nonempty graphs whose respective sets of blank nodes are disjoint.

### Minimum Self-Contained Graph (MSG)
([RDFSync: Efficient Remote Synchronization of RDF Models](https://dx.doi.org/10.1007/978-3-540-76298-0_39), 2007; [PDF](http://iswc2007.semanticweb.org/papers/533.pdf))

**Minimum Self-Contained Graph**: Given an RDF statement *s*, the Minimum Self-Contained Graph (MSG) containing that statement, written *MSG(s)*, is the set of RDF statements comprised of the following:
- The statement in question;
- Recursively, for all the blank nodes involved by statements included in the description so far, the MSG of all the statements involving such blank nodes
