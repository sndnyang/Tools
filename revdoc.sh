
echo $1

name=`echo $1 | cut -d "." -f 1`

objname=$name.html

pandoc "$1" -o "$objname"  -t revealjs -s -S -V revealjs-url:"http://cdn.bootcss.com/reveal.js/3.2.0" --slide-level=2
