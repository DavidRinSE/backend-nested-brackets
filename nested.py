#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys

def is_nested(line):
    brackets = {
        "(":["open"], ")":["close", "("], 
        "[":["open"], "]":["close", "["], 
        "{":["open"], "}":["close", "{"], 
        "<":["open"], ">":["close", "<"], 
    }
    
    stack = []
    tokens = 0
    
    for i, c in enumerate(line, start=0):
        if line[i:i+2] == "(*":
            stack.append("(*")
        elif line[i-1:i+1] == "*)" and line[i-2] != "(":
            if stack[-1] == "(*":stack.pop()
            else: return "NO {}".format(tokens)
        elif c in brackets:
            tokens += 1
            if brackets[c][0] == "open": stack.append(c)
            elif stack[-1] == brackets[c][1]: stack.pop()
            else: return "NO {}".format(tokens)
        else: tokens += 1
    if len(stack) != 0: return "NO {}".format(tokens)
    return "YES"

def start_nested(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(is_nested(line))

def main(args):
    if len(sys.argv) != 2:
        print ('usage: python nested.py file')
        sys.exit(1)

    filename = sys.argv[1]
    start_nested(filename)


if __name__ == '__main__':
    main(sys.argv[1:])
