#!/usr/bin/env python

infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

lines = infile.read().split('\n')
infile.close()

for num, line in enumerate(lines):
    outfile.write("Line#" + str(num) + " -> Character Count : " +
                  str(len(line)) + " Word Count : " +
                  str(len(line.split(" "))) + "\n") if len(line) > 0 else ""
outfile.close()
