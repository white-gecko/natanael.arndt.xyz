---
layout: page
parent: notes
title: The Linked Data Life-Cycle
description: "The Linked Data Life-Cycle tries to visualize the relevant steps performed to generate, manage, publish Linked Data."
date:   2019-08-06 23:51:00+09:00
update: 2019-08-06 23:51:00+09:00
---

## Introduction
The *Linked Data Life-Cycle*, *LOD2 Cycle*, or *LOD Cylce* tries to visualize the relevant steps performed to generate, manage, publish Linked Data.

Relevant Literature about the Linked Data Life-Cycle is:

* Sören Auer, Volha Bryl, and Sebastian Tramp, eds. Linked Open Data - Creating Knowledge Out of Interlinked Data - Results of the LOD2 Project. Vol. 8661. Lecture Notes in Computer Science. Springer, 2014. isbn: 978-3-319-09845-6. doi: 10.1007/978-3-319-09846-3. url: [http://dx.doi.org/10.1007/978-3-319-09846-3](http://dx.doi.org/10.1007/978-3-319-09846-3).
* Sören Auer et al. “Introduction to Linked Data and Its Lifecycle on the Web”. In: Reasoning Web. 2013, pp. 1–90. url: [http://jens- lehmann.org/files/2013/reasoning_web_linked_data.pdf](http://jens-lehmann.org/files/2013/reasoning_web_linked_data.pdf).
* Sören Auer et al. “Managing the life-cycle of Linked Data with the LOD2 Stack”. In: Proceedings of International Semantic Web Conference (ISWC 2012). 2012. url: [http://iswc2012.semanticweb.org/sites/default/files/76500001.pdf](http://iswc2012.semanticweb.org/sites/default/files/76500001.pdf).

The life cycle developed in the LOD2 project was also underpinned with the implementation of components for each step within the LOD2-stack.
The life cycle and the LOD2-stack can be interactively explored on the [LOD2 webpage (internet archive)](https://web.archive.org/web/20141205064903/http://stack.lod2.eu:80/blog/).

There is also a page in the wiki of the [W3C Government Linked Data (GLD) working group](https://www.w3.org/2011/gld/wiki/Main_Page) that shows several proposals and evolutionary steps of a Linked Data life cycle model: [https://www.w3.org/2011/gld/wiki/GLD_Life_cycle](https://www.w3.org/2011/gld/wiki/GLD_Life_cycle).

## TikZ Version
I was looking for a [TikZ](https://www.ctan.org/pkg/pgf) version of the life-cycle cake but coudn't find one, so here it is:

<a href="/img/lod-cycle_tikz.svg"><img style="width: 60%" src="/img/lod-cycle_tikz.svg" /></a><br/>

```
\documentclass[tikz]{standalone}
\usepackage{tikz}                       % images

\definecolor{evol}{RGB}{71,221,75}
\definecolor{sear}{RGB}{128,228,70}
\definecolor{extr}{RGB}{195,235,70}
\definecolor{stor}{RGB}{241,215,70}
\definecolor{auth}{RGB}{247,150,70}
\definecolor{link}{RGB}{75,172,198}
\definecolor{clas}{RGB}{73,206,182}
\definecolor{qlty}{RGB}{72,214,132}

\begin{document}
\newcommand{\D}{8} % number of dimensions (config option)

\newdimen\R % maximal diagram radius (config option)
\R=4.5cm

\newcommand{\A}{-360/\D} % calculated angle between dimension axes  

% add the following two lines to your document to get bigger arrows
\usetikzlibrary{arrows.meta}
\tikzset{>={Latex[width=3mm,length=3mm]}}

\tikzstyle{circ}=[draw, anchor=center, shape=circle, text width=2.2cm]

\begin{tikzpicture}[scale=1,
  every label/.style={align=center}
%every label/.style={draw, align=center}
]

  % define labels for each dimension axis (names config option)
\path (1*\A:\R) node[circ, fill=evol, label=center:{Evolution/\\Repair}] (L1) {};             % green
\path (2*\A:\R) node[circ, fill=sear, label=center:{Search/\\Browsing/\\Exploration}] (L2) {}; % lime
\path (3*\A:\R) node[circ, fill=extr, label=center:{Extraction}] (L3) {};                      % lime
\path (4*\A:\R) node[circ, fill=stor, label=center:{Storage/\\Querying}] (L4) {};            % yellow
\path (5*\A:\R) node[circ, fill=auth, label=center:{Manual\\revision/\\Authoring}] (L5) {};  % orange
\path (6*\A:\R) node[circ, fill=link, label=center:{Interlinking\\/Fusing}] (L6) {};           % teal
\path (7*\A:\R) node[circ, fill=clas, label=center:{Classifi-\\cation/\\Enrichment}] (L7) {};  % teal
\path (8*\A:\R) node[circ, fill=qlty, label=center:{Quality\\Analysis}] (L8) {};               % green


  \draw [->, bend left=10] (L1) to (L2);
  \draw [->, bend left=10] (L2) to (L3);
  \draw [->, bend left=10] (L3) to (L4);
  \draw [->, bend left=10] (L4) to (L5);
  \draw [->, bend left=10] (L5) to (L6);
  \draw [->, bend left=10] (L6) to (L7);
  \draw [->, bend left=10] (L7) to (L8);
  \draw [->, bend left=10] (L8) to (L1);

\end{tikzpicture}
\end{document}
```
[[PDF](/img/lod-cycle_tikz.pdf)], [[TeX+TikZ](/img/lod-cycle_tikz.tex)]
