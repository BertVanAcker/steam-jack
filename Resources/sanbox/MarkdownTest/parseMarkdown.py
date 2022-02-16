import marko

textFile = open("input/TEST.md", "r")

text = textFile.read()

x = marko.parse(text)
a = 1