#!/bin/sh
echo $1

name=`echo $1 | cut -d "." -f 1`

objname=$name.html

pandoc "$1" -o "$objname"  -t revealjs -s --slide-level=2 -V revealjs-url:"http://cdn.bootcss.com/reveal.js/3.2.0"  --mathjax="//cdn.bootcss.com/mathjax/2.6.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
