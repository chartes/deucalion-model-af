#!/bin/python3

import glob

stored = ""

indexes = {
	
}
for file in glob.glob("**/*.score.md", recursive=True):
	with open(file) as f:
		record = False

		for line in f:
			if line.startswith("## "):
				record = True
				stored += line.replace("## ", "#### ")
				indexes[line[3:].strip()] = file
			elif line.startswith("### "):
				record = False
			elif record is True:
				stored += line

#print(stored)
#print(index)

sources = [
	"",
	""
]
with open("README.md") as f:
	index = 0
	ignore = False
	for line in f:
		if line.startswith("<!-- Start Scores -->"):
			sources[index] += line
			ignore = True
			index = 1
		elif line.startswith("<!-- End Scores -->"):
			ignore = False
			sources[index] += line
		elif ignore is False:
			sources[index] += line

indexes = "More details:\n"+ "\n".join([
	f"- [{task}]({link})"
	for task, link in indexes.items()
])+"\n\n\n"

with open("README.md", "w") as f:
	f.write(sources[0]+indexes+stored+sources[1])