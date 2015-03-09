#!/usr/bin/python
from __future__ import print_function
from inverted_index import TextIndexer
from inverted_index import TermNotFoundError

import sys

TITLE_FILE = 'title.txt'

if raw_input: input = raw_input

def query():
	global ti
	query = input("query: ").strip().split()
	try:
		results = ti.dotProductForTerms(query).items()
		results.sort(key=lambda x: x[1], reverse=True)

		for (counter, (name, val)) in enumerate(results, start=1):
			if val > 0:
				print(str(counter) + ")  ", name, "  (",val,")")

	except TermNotFoundError as e:
		print("Term not found:", e)
	input("continue...")




if len(sys.argv) < 2:
	print("Aborting: Filename required")
	sys.exit(1)

filename = sys.argv[1]

ti = TextIndexer()
ti.parse(filename)


#title screen
with open(TITLE_FILE) as f:
	[print(line.rstrip()) for line in f.readlines()]


cmds = {
	'0': lambda: sys.exit(0),
	'1': lambda: query()
}

while True:
	print("1)query\n"
		  "0)exit")

	option = input(">>")
	cmds[option]() if cmds.has_key(option) else\
	 								print("Invalid Argument Received")
