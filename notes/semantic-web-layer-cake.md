---
layout: page
parent: notes
title: The Semantic Web Layer Cake
abstract: "The Semantic Web Layer Cake tries to visualize the interplay of componants on the Semantic Web"
date:   2018-11-21 16:46:00
update: 2018-11-21 16:46:00
---

## Introduction
The *Semantic Web Layer Cake* or *Semantic Web Layer Model* is an approach to visualize and define the interplay of the components on the [Semantic Web](https://en.wikipedia.org/wiki/Semantic_Web).
The most commonly known *layer model* probably is the [OSI model](https://en.wikipedia.org/wiki/OSI_model).
The OSI model describes which tasks are performed in which layer and thus provides an abstraction of these tasks for the other layers.
In this way it is not neccessary for every single application to implement the full stack.
Further it allows to make changes within one layer by keeping applications on the other layers in tact.

Since abstraction simplifies aspects this is usually a good point for discussion.
Also the Semantic Web Layer Cake is permanently under discussion.
To keep an overview on the individual proposals I want to keep a collection of links to the individual figures.
If you know more examples or of you can give me “more original” sources, please tell me.

## The Commonly Used Layer Cake
![From bottom to top. Layer 1: Unicode, URI; layer 2: XML + NS + xmlschema; layer 3: Self-desc. doc., RDF + rdfschema; layer 4: Data, Ontology vocabulary; layer 5: Data, Logic; layer 6: Rules, Proof; layer 7: Trust; at the side is one layer spanning from 3-6: Digital Signature](https://www.w3.org/2000/Talks/1206-xml2k-tbl/sweb-stack.gif)<br/>
The first widely used and referenced model was [presented by Tim Berners-Lee in 2000](https://www.w3.org/2000/Talks/1206-xml2k-tbl/slide10-0.html).

Based on the 2000 version of the model a model was proposed in 2005-2007 which is widely used with small variations:
![If the alt texts of the pictures are helpeful for you please tell me. I will complete them as I have time. Sorry that they are not here at the moment.](https://www.w3.org/2007/03/layerCake.svg)

![](https://www.w3.org/DesignIssues/diagrams/sweb-stack/2006a.png)<br/>
This one is referenced in the [MIT-W3C DAML program: Final Report](https://www.w3.org/2005/12/31-daml-final.html), in [Semantic Web Technologies in the Enterprise](http://www.thefigtrees.net/lee/blog/2006/11/semantic_web_technologies_in_t.html) by Lee Feigenbaum on November 28, 2006 and in the talks [Emerging Web Technologies to Watch](https://www.w3.org/2006/Talks/1023-sb-W3CTechSemWeb/Overview.html#(19)) by Steve Bratt. All around the same time, so I don't know who created it. ([Alternative URL of the figure](https://www.w3.org/2006/Talks/1023-sb-W3CTechSemWeb/SemWebStack-tbl-2006a.png).)

![](https://www.w3.org/2007/Talks/0130-sb-W3CTechSemWeb/layerCake-4.png)<br/>
In the talks [Semantic Web, and Other Technologies to Watch](https://www.w3.org/2007/Talks/0130-sb-W3CTechSemWeb/#(24)) by Steve Bratt from 2007 he is using a different version.

## Alternative Proposals and Interpretations

![](http://bnode.org/media/2009/07/08/semantic_web_technology_stack.png)<br/>
In the article [The Semantic Web - Not a piece of cake...](http://bnode.org/blog/2009/07/08/the-semantic-web-not-a-piece-of-cake) by Benjamin Nowack from 2009, he puts some more dimensions into the layer model which provides nice angles to view on the things. He also provides Linked Data with an extra part of the Stack.

![](https://image.slidesharecdn.com/www2014tutorialwebsemv2-140408040534-phpapp02/95/an-introduction-to-semantic-web-and-linked-data-9-638.jpg?cb=1396930256)
In the presentation [An introduction to Semantic Web and Linked Data ](https://www.slideshare.net/fabien_gandon/semantic-web-and-linked-data) by Fabian Gandon at the WWW2014, he categorizes the layers into the five groups: Abstract Language/Representation, Query & Update, Reasoning, Trust, and Application and Interaction.

![](https://cdn-images-1.medium.com/max/1600/1*YQ04iyBrbq-VrQwkzCMkkA.png)<br/>
In the article [Semantic Web Layer Cake Tweak, Explained](https://medium.com/openlink-software-blog/semantic-web-layer-cake-tweak-explained-6ba5c6ac3fab) by Kingsley Uyi Idehen from 2017, he shows an updated model which includes the recent evolution of the Semantic Web technologies.

## Historical Models
The first widely used and referenced model by Tim Berners-Lee was also predated by some other models.

![](http://www.jfsowa.com/ikl/Hendler00.jpg)<br/>
by Jim Hendler from 2000 (via [Semantics for Interoperable Systems](http://www.jfsowa.com/ikl/) by John Sowa)

John Sowa also shows this figure in his page:
![](http://www.jfsowa.com/figs/timbl3.gif)
