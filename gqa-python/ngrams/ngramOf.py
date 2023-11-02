import json
import time
import phrasefinder as pf

with open("vg14/cObjsNV.json", "r") as f:
    objDict = json.load(f)

# with open("roFreqs.json", "r") as f:
#     roOldFreqs = json.load(f)

def isPlural(objName):
    mod = objDict[objName]["mod"]
    return (mod == "plural") 

def apos(objName):
    if objName.endswith(s):
        if isPlural(objName):
            return "{}'".format(objName)
        else:
            return "{}'s".format(objName)
    else:
        return "{}'s".format(objName)

def getPhrases(s, o):
    return ["{obj} of the {subj}".format(subj = s, obj = o), 
            "{subj} {obj}".format(subj = s, obj = o),
            "{subjs} {obj}".format(subjs = apos(s), obj = o)]    

def processBatch(inBatch):
    outBatch = []

    for (s, o), c in inBatch:
        phraseFreqs = []
        phrases = getPhrases(s, o)
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
        outBatch.append(((s, o), phraseFreqs)) 

    return outBatch

pairOfCountFile = open("ofPairsC.txt", "w")
pairHaveCountFile = open("havePairsC.txt", "w")
pairFreqFile = open("ofPairsF.txt", "w")

ofDict = json.load(open("vg14/info_rcCount.json"))

ofPairs = []
for p in ofDict["of"]:
    o, s = p.split("_")
    c = ofDict["of"][p]
    ofPairs.append(((s, o), c))
havePairs = []   
for p in ofDict["have"]:
    s, o = p.split("_")
    c = ofDict["have"][p]
    havePairs.append(((s, o), c))

ofPairs = sorted(ofPairs, key = lambda x: x[1], reverse = True)
havePairs = sorted(havePairs, key = lambda x: x[1], reverse = True)

for ((s, o), c) in ofPairs:
    pairOfCountFile.write("{}_{},{}\n".format(s, o, c))
for ((s, o), c) in havePairs:
    pairHaveCountFile.write("{}_{},{}\n".format(s, o, c))    

allPairs = {}
for p in ofPairs:
    if p[0] not in allPairs:
        allPairs[p[0]] = ofPairs[p[1]]
for p in havePairs:
    if p[0] not in allPairs:
        allPairs[p[0]] = havePairs[p[1]]        

sortedPairs = sorted(allPairs.items(), key = lambda x: x[1], reverse = True)

batchSize = 10
current = 0
print(len(sortedPairs))
while current < len(sortedPairs):
    startTime = time.time()
    inBatch = sortedPairs[current:current+batchSize]
    outBatch = processBatch(inBatch)
    endTime = time.time()

    print("{},{}".format(current, endTime - startTime))
    for ((s, o), pFreqs) in outBatch:
        pStrs = ["{phrase}.{freq}".format(phrase = p, freq = f) for p, f in pFreqs]
        pStr = ";".join(pStrs)
        pairFreqFile.write("{}_{},{}\n".format(s, o, pStr))
        pairFreqFile.flush()

    current += batchSize
