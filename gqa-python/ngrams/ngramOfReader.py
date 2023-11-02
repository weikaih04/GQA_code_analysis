import json
from collections import defaultdict
# roFreqs = json.load(open("ofFreqs.json"))
ofFreqsIn = open("ofPairsF.txt")
ofFreqsOut = open("ofFreqs.json", "w")

# 0oFreqs = defaultdict(lambda: defaultdict(dict))
# roFreqs = {}
ofFreqs = {}

for line in ofFreqsIn:
	line = line.strip()
	so, pfs = line.split(",")
	s, o = so.split("_")
	pfs = pfs.split(";")
	pflist = []
	for pf in pfs:
		p, f = pf.split(".")
		pflist.append((p, int(f)))

	if s not in ofFreqs:
		ofFreqs[s] = {}
	ofFreqs[s][o] = pflist

json.dump(ofFreqs, ofFreqsOut)