# -*- coding: utf-8 -*-
__author__ = 'boqingfu'
import this

print this
print this.s

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print "".join([d.get(c, c) for c in this.s])
print this.s.decode("rot13")