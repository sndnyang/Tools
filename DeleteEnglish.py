#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

def DeleteEnglish(filename):
    split = filename.find('en.txt')
    if split != -1:
        prefix = filename[:split-1]
        postfix = filename[split:]
        writename = prefix + '.zh-cn.txt'
    else :
        writename = filename + '.zh-cn.txt'

    tranfile = open(filename)
    writefile = file(writename, 'w')
    text = tranfile.readlines()

    ascAll = string.punctuation + ' ' + string.punctuation \
             + string.letters + string.whitespace \
             + string.digits
    
    for row in text:
        for char in row:
            if char not in ascAll:
                writefile.write(row + '\n')
                break
        
    writefile.close()
    tranfile.close()
    
if __name__ == '__main__':

    import os
    cwd = os.getcwd()
    choice_option = []
    print "You can choose these files to open:"
    for f in os.listdir(cwd):
        if f.find('.txt') != -1:
            choice_option.append(f)

    count = 1
    for f in choice_option:
        print str(count) + " : " + f
        count += 1

    choice = input()-1
    DeleteEnglish(choice_option[choice])
