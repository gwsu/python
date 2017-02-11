#!/usr/bin/python2.7
#-*- coding: UTF-8 -*-

for letter in 'python':
    if letter == 'h':
        pass
        print '这是pass块'
    print 'curret char is:', letter

var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print 'curret var is:',var
print "good bye!"


