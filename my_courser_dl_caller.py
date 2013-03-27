#!/usr/env python

import os

if __name__ == '__main__':

    cwd = os.getcwd()
    
    if cwd != r'F:\video':
        cwd = r'F:\video'
        os.chdir(cwd)
    
    cmd = r'"F:\\source code\\coursera\\coursera\\coursera_dl.py" '

    usr = raw_input()

    usr = ' -u ' + usr + '@gmail.com '

    psw = raw_input()
    psw = ' -p ' + psw + ' '
    
    course = raw_input()

    os.system(cmd + usr + psw +course)
