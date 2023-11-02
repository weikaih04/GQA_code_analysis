import json
import time
import phrasefinder as pf

with open("vg14/cObjsNV.json", "r") as f:
    objDict = json.load(f)

with open("roFreqs.json", "r") as f:
    roOldFreqs = json.load(f)

def getAn(objName):
    an = objDict[objName]["an"]
    return "an" if an else "a"

def isSingular(objName):
    mod = objDict[objName]["mod"]
    return (mod == "singular") 

def getPhrases(r, o):
    singular = isSingular(o)
    if singular:
        a = getAn(o)
        return ["{rel} {a} {obj}".format(rel = r, a = a, obj = o), "{rel} the {obj}".format(rel = r, obj = o)]    
    else: 
        return ["{rel} {obj}".format(rel = r, obj = o), "{rel} the {obj}".format(rel = r, obj = o)]

def processBatch(inBatch):
    outBatch = []

    for (r, o), c in inBatch:
        phraseFreqs = []
        phrases = getPhrases(r, o)
        for p in phrases:
            count = 3
            while count > 0:
                freq = 0
                try:
                    freqs = pf.search(pf.Corpus.AMERICAN_ENGLISH, p).phrases                    
                    if len(freqs) > 0:
                        freq = freqs[0].match_count
                    count = 0
                except Exception as error:   
                    count -= 1
                    if count == 0:
                        print(p)

            phraseFreqs.append((p, freq))
        outBatch.append(((r, o), phraseFreqs)) 

    return outBatch

pairCountFile = open("roPairsCNew.txt", "w")
pairFreqFile = open("roPairsFNew.txt", "w")

relDict = json.load(open("vg14/info_roCount.json"))
relPairs = []
for r in relDict:
    for o in relDict[r]:
        c = relDict[r][o]
        if c > 1 and any([x[1] == 0 for x in roOldFreqs[r][o]]):
            relPairs.append(((r, o), c))

sortedPairs = sorted(relPairs, key = lambda x: x[1], reverse = True)

for ((r, o), c) in sortedPairs:
    pairCountFile.write("{}_{},{}\n".format(r, o, c))

batchSize = 10
current = 0
print(len(sortedPairs))
while current < len(sortedPairs):
    startTime = time.time()
    inBatch = sortedPairs[current:current+batchSize]
    outBatch = processBatch(inBatch)
    endTime = time.time()

    print("{},{}".format(current, endTime - startTime))
    for ((r, o), pFreqs) in outBatch:
        pStrs = ["{phrase}.{freq}".format(phrase = p, freq = f) for p, f in pFreqs]
        pStr = ";".join(pStrs)
        pairFreqFile.write("{}_{},{}\n".format(r, o, pStr))
        pairFreqFile.flush()

    current += batchSize
