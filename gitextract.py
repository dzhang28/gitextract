#!/usr/bin/python3

import sys
import re

count = 0

def checkKeyword(subTxt, outfile, keywords):
    matched = False
    for subline in subTxt.split("\n"):
        for keyword in keywords:
            if re.search(rf'{keyword}', subline, re.IGNORECASE) \
                and not re.match(r'^\s+Cc:\s', subline) \
                and not re.match(r'^\s+Acked-by:\s', subline) \
                and not re.match(r'^\s+Tested-by:\s', subline) \
                and not re.match(r'^\s+Reviewed-by:\s', subline) \
                and not re.match(r'^\s+Reported-by:\s', subline):
                matched = True
                break
        if matched:
            break
        
    global count

    if matched:
        outfile.write(subTxt)
        with open(rf'tmp-{count}.txt', 'w') as tmpfile:
            tmpfile.write(subTxt)
        count += 1

def extractKeywords(inputfile, outputfile, keywords):
    pattern = re.compile(r'^commit\s[0-9a-z]{40}')
    subTxt = ''
    subStarted = False
    with open(inputfile, 'rt', encoding="ISO-8859-1") as infile, open(outputfile, 'w') as outfile:
        for line in infile:
            if pattern.match(line):  
                if subTxt != '':
                    checkKeyword(subTxt, outfile, keywords)
                    subTxt = ''
                subStarted = True
                subTxt += line
            elif subStarted:
                subTxt += line
    # Write last sub txt
    checkKeyword(subTxt, outfile, keywords)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 gitextract.py inputfile outputfile keywords")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    keywords = sys.argv[3:]

    extractKeywords(inputfile, outputfile, keywords)
    
    global count
    print(f'Total {count} commits found.')

if __name__ == "__main__":
    main()