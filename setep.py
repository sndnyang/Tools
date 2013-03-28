#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py

from distutils.core import setup 
import py2exe 
import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "No target file!"
        sys.exit(1)
   
    temp = {"script" : sys.stdin}    
    
    setup( 
        options = { 
          "py2exe": { 
            "dll_excludes": ["MSVCP90.dll"], 
          } 
        }, 
        windows=[temp]
    ) 
