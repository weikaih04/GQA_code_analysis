import json
from collections import defaultdict
roFreqs = json.load(open("roFreqs.json"))
roFreqsIn = open("roPairsFNew.txt")
roFreqsOut = open("roFreqsNew.json", "w")

# roFreqs = defaultdict(lambda: defaultdict(dict))
# roFreqs = {}

for line in roFreqsIn:
	line = line.strip()
	ro, pfs = line.split(",")
	r, o = ro.split("_")
	pfs = pfs.split(";")
	pflist = []
	for pf in pfs:
		p, f = pf.split(".")
		pflist.append((p, int(f)))

	if r not in roFreqs:
		roFreqs[r] = {}
	roFreqs[r][o] = pflist

json.dump(roFreqs, roFreqsOut)