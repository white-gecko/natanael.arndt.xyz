---
layout: page
parent: notes
title: Agile Development
description: "A diagram showing a simple agile development cycle."
date:   2020-10-14 17:03:00+02:00
update: 2020-10-14 17:03:00+02:00
---

## Introduction
The simplified development *Cycle* of an agile software engineering process.

You can read more about agile software development and SCRUM in the Wikipedia:

* [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development)
* [SCRUM](https://en.wikipedia.org/wiki/Scrum_(software_development))

## TikZ Version
I was looking for a [TikZ](https://www.ctan.org/pkg/pgf) version of the development cycle but couldn't find one, so here it is:

{% include img.html style="width: 60%" src="/img/agile_tikz.svg" href="/img/agile_tikz.svg" %}<br/>

```
\documentclass[tikz]{standalone}
\usepackage{tikz}
\usepackage{ifthen}

\definecolor{sal}{RGB}{247,160,114}
\definecolor{isa}{RGB}{249,247,243}
\definecolor{blu}{RGB}{181,226,250}
\definecolor{chm}{RGB}{237,222,164}
\definecolor{gre}{RGB}{15,163,177}

\begin{document}

% donut diagram
% http://www.texample.net/tikz/examples/circular-arrows-text/
\usetikzlibrary{decorations.text}
\newcommand{\arcarrow}[9]{
% inner radius, middle radius, outer radius, start angle,
% end angle, tip protusion angle, color, text, text-direction
  \pgfmathsetmacro{\rin}{#1}
  \pgfmathsetmacro{\rmid}{#2}
  \pgfmathsetmacro{\rout}{#3}
  \pgfmathsetmacro{\astart}{#4}
  \pgfmathsetmacro{\aend}{#5}
  \pgfmathsetmacro{\atip}{#6}
  \fill[#7, draw=black]   (\astart:\rin) arc (\astart:\aend:\rin)
       -- (\aend+\atip:\rmid) -- (\aend:\rout) arc (\aend:\astart:\rout)
       -- (\astart+\atip:\rmid) -- cycle;
  \ifthenelse{#9=1}{
    \path[decoration = {text along path, text = {#8}, text align = {align = center}, raise = -0.5ex}, decorate]
    (\astart+\atip:\rmid) arc (\astart+\atip:\aend+(\atip/2):\rmid);
  }{
    \path[decoration = {text along path, text = {#8}, text align = {align = center}, raise = -0.5ex}, decorate]
    (\aend+\atip:\rmid) arc (\aend+\atip:\astart+(\atip/2):\rmid);
  }
}

\begin{tikzpicture}

\arcarrow{2}{2.4}{2.8}{0}{40}{-5}{chm}{Test}{0}
\arcarrow{2}{2.4}{2.8}{45}{120}{-5}{blu}{Implementierung}{0}
\arcarrow{2}{2.4}{2.8}{125}{175}{-5}{isa}{Entwurf}{0}
\arcarrow{2}{2.4}{2.8}{180}{270}{-5}{sal}{Anforderungsanalyse}{1}
\arcarrow{2}{2.4}{2.8}{275}{355}{-5}{gre}{Planung anpassen}{1}

\begin{scope}[xshift=180]

\arcarrow{2}{2.4}{2.8}{-20}{35}{-5}{chm}{Test}{0}
\arcarrow{2}{2.4}{2.8}{40}{120}{-5}{blu}{Implementation}{0}
\arcarrow{2}{2.4}{2.8}{125}{175}{-5}{isa}{Design}{0}
\arcarrow{2}{2.4}{2.8}{180}{280}{-5}{sal}{Requirements Analysis}{1}
\arcarrow{2}{2.4}{2.8}{285}{335}{-5}{gre}{Plan}{1}

\end{scope}

\end{tikzpicture}
\end{document}
```

[[PDF](/img/agile_tikz.pdf)], [[TeX+TikZ](/img/agile_tikz.tex)]
