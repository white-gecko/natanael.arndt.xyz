---
layout: post
title: Sicherheitstest für meine Seite
tags: ["mozilla", "web", "security", "https", "sicherheit"]
date:   2016-08-28 19:00:00+
---

<span style="background-color: rgb(101, 39, 112);
border-color: rgb(74, 16, 84);
border-radius: 12px;
border-style: solid;
border-width: 6px;
color: rgb(255, 255, 255);
display: inline-block;
font-family: Arial,Helvetica,sans-serif;
height: 128px;
line-height: 116px;
padding-right: 4px;
text-align: center;
width: 128px;
float: left; margin-right: 25px">
    <span style="font-size: 88px">D</span>
    <sup style="float: right;font-size: 52px;line-height: 0px;top: 32px;vertical-align: baseline">+</sup>
</span>

Bei meiner heutigen Presseschau bin ich auf die beiden [golem](http://www.golem.de/news/observatory-mozilla-bietet-sicherheitscheck-fuer-websites-1608-122923.html) und [heise/ix](http://www.heise.de/ix/meldung/Mozilla-bringt-kostenlosen-Sicherheitstest-fuer-Websites-3306197.html) Artikel zu einem neuen Sicherheitstest von Mozilla für Webseites gestoßen.
Den Test erläutert die Entwicklerin April King ebenfalls in [einem Eintrag in ihrem eigenen Blog](https://pokeinthe.io/2016/08/25/observatory-by-mozilla-a-new-tool/).
Über die Seite [https://observatory.mozilla.org/](https://observatory.mozilla.org/) kann man mit wenig Aufwand die eigene Seite überprüfen.

Das ganze habe ich zuerst nicht für relevant erachtet, denn welcher Art sollen schon die Sicherheitslücken in einer statischen Jekyll seite sein, immerhin biete ich ja HTTPS über Let's Encrypt an (siehe [„My New Webpage“](2016-02-21-new_webpage)).
Ich habe aber dennoch einen [test gewagt](https://observatory.mozilla.org/analyze.html?host=natanael.arndt.xyz) mit einem ernüchternden Ergebnis von **D+** :-(
So gravierend hätte ich das nicht erwartet, es zeigt mir aber, dass es sich durchaus lohnt etwas an der Stelle zu unternehmen und dass auch simple statische Jekyll Seiten noch verbessert werden können.

Die Schwachstellen liegen offenbar in den Headern:

* Content Security Policy (CSP) header not implemented
* X-Content-Type-Options header not implemented
* X-Frame-Options (XFO) header not implemented
* X-XSS-Protection header not implemented

Da muss ich mich jetzt entsprechend zu den Techniken belesen und sehen, wie sie in Jekyll umsetzbar sind.
Immerhin setzt meine Seite keine Cookies und HTTPS passt im Standardtest auch.
