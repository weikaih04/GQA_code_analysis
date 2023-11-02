import json
from collections import defaultdict
oaFreqs = json.load(open("oaFreqs.json"))
oaFreqsIn = open("oaPairsFNew.txt")
oaFreqsOut = open("oaFreqsNew.json", "w")

# oaFreqs = {} # defaultdict(dict)

for line in oaFreqsIn:
	line = line.strip()
	ao, f = line.split(",")
	a, o = ao.split("_")

	if o not in oaFreqs:
		oaFreqs[o] = {}
	oaFreqs[o][a] = int(f)

json.dump(oaFreqs, oaFreqsOut)