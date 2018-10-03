from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print(f"copying {fromfile} to {tofile}")

infile = open(fromfile)
incontents = infile.read()

print(f"input is {len(incontents)} long")
print(f"does tofile exist? {exists(tofile)}")
print("hit ret to continue, ctrlc to abort")

input()

tofil = open(tofile, "w")
tofil.write(incontents)

print("all dpne")

infile.close()
tofil.close()
