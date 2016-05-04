#!/bin/python
# -*- coding:utf-8 -*-

import re
import sys

def functions_in_a_file(lines):
    regex = r'^\s*def (\w+)'

    functions = []
    for l in lines:
        t = re.findall(regex, l)
        if not t:
            continue
        functions.append(t[0])

    return functions


def find_functions_from_files(files):
    functions_list = []
    for f in files:
        fp = file(f)
        lines = fp.readlines()
        fp.close()

        functions_list += functions_in_a_file(lines)

def find_functions_map_from_files(files, functions):
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'please input target filename(s)'
        sys.exit()

    functions = find_functions_from_files(sys.argv[1:])

    callgraph = find_functions_map_from_files(sys.argv[1:], functions)

    print callgraph
