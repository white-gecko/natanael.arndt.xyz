---
layout: post
title: "Convert a Presentation to a Video"
tags: ["Presentation", "LaTeX", "Video"]
date: 2025-06-20 15:46:00+02:00
reply: true
---

At some event we had a screen to show some slides, as well as a pre-produced video, to summarize our project outcomes.
Since my presentation tool-chain mostly involves LaTeX beamer slides, I came up with the following script to convert the PDF pages into video frames and concatenate another video file.

```sh
#!/bin/sh

convert -density 609 -resize 1920x1080 main.pdf video/picture.png
cd video
ffmpeg -r 1/6 -i picture-%01d.png -c:v libx264 -r 30 video.mp4
ffmpeg -i video.mp4 -i second_video.mp4 -f lavfi -t 1 -i anullsrc -filter_complex "[0:v][2:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" out.mkv
```

The inputs are:
- `main.pdf` with your slides
- `video/second_video.mp4` with the video you want to attach

The output will be at `video/out.mkv`.

The slides should be in 16:9 format, so that it nicely scales to `1920x1080` (Full-HD).
All other options should be documented at [https://ffmpeg.org/](https://ffmpeg.org/).
