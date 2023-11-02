import json
import time
import phrasefinder as pf

with open("oaFreqs.json", "r") as f:
    oaOldFreqs = json.load(f)

def processBatch(inBatch):
    outBatch = []

    for (o, a), c in inBatch:
        tryAgain = 3
        p = "{attr} {obj}".format(attr = a, obj = o)
        while tryAgain > 0:
            freq = 0            
            try:
                freqs = pf.search(pf.Corpus.AMERICAN_ENGLISH, p).phrases
                if len(freqs) > 0:
                    freq = freqs[0].match_count
                tryAgain = 0
            except Exception as error:   
                tryAgain -= 1
                if tryAgain == 0:
                    print(p)
                # print('Fatal error: {}'.format(error))
                # freq = 0         
        outBatch.append(((o, a), freq)) 

    return outBatch

pairCountFile = open("oaPairsCNew.txt", "w")
pairFreqFile = open("oaPairsFNew.txt", "w")

attrDict = json.load(open("oaCounts.json"))
attrPairs = []
for o in attrDict:
    for a in attrDict[o]:
        c = attrDict[o][a]
        if o not in oaOldFreqs or a not in oaOldFreqs[o] or oaOldFreqs[o][a] == 0:
            attrPairs.append(((o, a), c))


sortedPairs = sorted(attrPairs, key = lambda x: x[1], reverse = True)

for ((o, a), c) in sortedPairs:
    pairCountFile.write("{}_{},{}\n".format(a, o, c))

batchSize = 10
current = 0
print(len(sortedPairs))
while current < len(sortedPairs):
    startTime = time.time()
    inBatch = sortedPairs[current:current+batchSize]
    outBatch = processBatch(inBatch)
    endTime = time.time()

    print("{},{}".format(current, endTime - startTime))
    for ((o, a), f) in outBatch:
        pairFreqFile.write("{}_{},{}\n".format(a, o, f))
        pairFreqFile.flush()

    current += batchSize
