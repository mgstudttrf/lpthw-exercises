import sys

script, encoding, errors = sys.argv

def main(langfile, encoding, errors):
    line = langfile.readline()

    if line:
        printline(line, encoding, errors) 
        return main(langfile, encoding, errors)

def printline(line, encoding, errors):
    line = line.strip()
    raw = line.encode(encoding, errors=errors)
    cooked = raw.decode(encoding, errors=errors)
    print(raw,"<======>", cooked)

languages = open("langs.txt", encoding = "utf-8")

main(languages, encoding, errors)
