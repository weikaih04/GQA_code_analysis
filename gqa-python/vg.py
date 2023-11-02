import argparse
import json
import pickle 
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
# from visual_genome import api as vg
from PIL import Image as PIL_Image
import requests
import io
# from models import Image, Object, Attribute, Relationship
# from models import Region, Graph, QA, QAObject, Synset
import http.client
import json
# import utils
from nltk.corpus import wordnet



def GetImageData(id=61512):
  data = utils.retrieve_data('/api/v0/images/' + str(id))
  if 'detail' in data and data['detail'] == 'Not found.':
    return None
  image = utils.parse_image_data(data)
  return image

parser = argparse.ArgumentParser()
parser.add_argument('--dir', default="vg14", type = str)

# parser.add_argument('--inDir', required=True, type = str)
# parser.add_argument('--tier', required=True)
parser.add_argument('--outputName', default = "info", type = str)
# parser.add_argument('--cont', action = "store_true")
# parser.add_argument('--features', action = "store_true")
# parser.add_argument('--maxObjectNum', default = 100, type = int)
# parser.add_argument('--featuresDim', default = 2048, type = int)
# parser.add_argument('--inEnd', default = [""], nargs = "*")

# parser.add_argument('--imagesNum', default = _, type = int)

args = parser.parse_args()

out = "{dir}/{outputName}".format(dir = args.dir, outputName = args.outputName)
idFilename = "{dir}/image_data.json".format(dir = args.dir)
objectsFilename = "{dir}/objects.json".format(dir = args.dir)
attributesFilename = "{dir}/attributes.json".format(dir = args.dir)
relationsFilename = "{dir}/relationships.json".format(dir = args.dir)
descriptionsFilename = "{dir}/region_descriptions.json".format(dir = args.dir)
outDict = lambda dictName: out + "_{dictName}.pkl".format(dictName = dictName)
outJson = lambda dictName: out + "_{dictName}.json".format(dictName = dictName)

outIdFilename = out + "_annotations.json"

data = {}
vgId2Id = {}

allPunct = ["?", "!", "\\", "/", ")", "(", ".", ",", ";", ":"]
fullPunct = [";", r"/", "[", "]", '"', "{", "}", "(", ")", "=", 
                "+", "\\", "_", "-",">", "<", "@", "`", ",", "?", "!", "%", 
                "^", "&", "*", "~", "#", "$"]
contractions = {"aint": "ain't", "arent": "aren't", "cant": "can't", "couldve": "could've", "couldnt": "couldn't", \
                 "couldn'tve": "couldn't've", "couldnt've": "couldn't've", "didnt": "didn't", "doesnt": "doesn't", "dont": "don't", "hadnt": "hadn't", \
                 "hadnt've": "hadn't've", "hadn'tve": "hadn't've", "hasnt": "hasn't", "havent": "haven't", "hed": "he'd", "hed've": "he'd've", \
                 "he'dve": "he'd've", "hes": "he's", "howd": "how'd", "howll": "how'll", "hows": "how's", "Id've": "I'd've", "I'dve": "I'd've", \
                 "Im": "I'm", "Ive": "I've", "isnt": "isn't", "itd": "it'd", "itd've": "it'd've", "it'dve": "it'd've", "itll": "it'll", "let's": "let's", \
                 "maam": "ma'am", "mightnt": "mightn't", "mightnt've": "mightn't've", "mightn'tve": "mightn't've", "mightve": "might've", \
                 "mustnt": "mustn't", "mustve": "must've", "neednt": "needn't", "notve": "not've", "oclock": "o'clock", "oughtnt": "oughtn't", \
                 "ow's'at": "'ow's'at", "'ows'at": "'ow's'at", "'ow'sat": "'ow's'at", "shant": "shan't", "shed've": "she'd've", "she'dve": "she'd've", \
                 "she's": "she's", "shouldve": "should've", "shouldnt": "shouldn't", "shouldnt've": "shouldn't've", "shouldn'tve": "shouldn't've", \
                 "somebody'd": "somebodyd", "somebodyd've": "somebody'd've", "somebody'dve": "somebody'd've", "somebodyll": "somebody'll", \
                 "somebodys": "somebody's", "someoned": "someone'd", "someoned've": "someone'd've", "someone'dve": "someone'd've", \
                 "someonell": "someone'll", "someones": "someone's", "somethingd": "something'd", "somethingd've": "something'd've", \
                 "something'dve": "something'd've", "somethingll": "something'll", "thats": "that's", "thered": "there'd", "thered've": "there'd've", \
                 "there'dve": "there'd've", "therere": "there're", "theres": "there's", "theyd": "they'd", "theyd've": "they'd've", \
                 "they'dve": "they'd've", "theyll": "they'll", "theyre": "they're", "theyve": "they've", "twas": "'twas", "wasnt": "wasn't", \
                 "wed've": "we'd've", "we'dve": "we'd've", "weve": "we've", "werent": "weren't", "whatll": "what'll", "whatre": "what're", \
                 "whats": "what's", "whatve": "what've", "whens": "when's", "whered": "where'd", "wheres": "where's", "whereve": "where've", \
                 "whod": "who'd", "whod've": "who'd've", "who'dve": "who'd've", "wholl": "who'll", "whos": "who's", "whove": "who've", "whyll": "why'll", \
                 "whyre": "why're", "whys": "why's", "wont": "won't", "wouldve": "would've", "wouldnt": "wouldn't", "wouldnt've": "wouldn't've", \
                 "wouldn'tve": "wouldn't've", "yall": "y'all", "yall'll": "y'all'll", "y'allll": "y'all'll", "yall'd've": "y'all'd've", \
                 "y'alld've": "y'all'd've", "y'all'dve": "y'all'd've", "youd": "you'd", "youd've": "you'd've", "you'dve": "you'd've", \
                 "youll": "you'll", "youre": "you're", "youve": "you've"}
nums = { "none": "0", "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
         "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
articles = {"a": "", "an": "", "the": ""}
allReplaceQ = {}
for replace in [contractions, nums, articles]: # , 
    allReplaceQ.update(replace)

allReplaceA = {}
for replace in [contractions, nums]: # , 
    allReplaceA.update(replace)

periodStrip = lambda s: re.sub(r"(?!<=\d)(\.)(?!\d)", " ", s) # :,' ?
collonStrip = lambda s: re.sub(r"(?!<=\d)(:)(?!\d)", " ", s) # replace with " " or ""?
commaNumStrip = lambda s: re.sub(r"(\d)(\,)(\d)", r"\1\3", s)

# remove any non a-zA-Z0-9?
vqaProcessText = lambda text, tokenize, question: processText(text, ignoredPunct = [], keptPunct = [], 
    endPunct = [], delimPunct = fullPunct, replacelistPost = allReplaceQ if question else allReplaceA, reClean = True, tokenize = tokenize)

def processText(text, ignoredPunct = ["?", "!", "\\", "/", ")", "("], 
    keptPunct = [".", ",", ";", ":"], endPunct = [">", "<", ":"], delimPunct = [],
    delim = " ", clean = False, replacelistPre = dict(), replacelistPost = dict(),
    reClean = False, tokenize = True):

    if reClean:
        text = periodStrip(text)
        text = collonStrip(text)
        text = commaNumStrip(text)

    if clean:
        for word in replacelistPre:
            origText = text
            text = text.replace(word, replacelistPre[word])
            if (origText != text):
                print(origText)
                print(text)
                print("")

        for punct in endPunct:
            if text[-1] == punct:
                print(text)
                text = text[:-1]
                print(text)
                print("")

    for punct in keptPunct:
        text = text.replace(punct, delim + punct + delim)           
    
    for punct in ignoredPunct:
        text = text.replace(punct, "")

    for punct in delimPunct:
        text = text.replace(punct, delim)

    text = text.lower()

    if config.tokenizer == "stanford":
        ret = StanfordTokenizer().tokenize(text)
    elif config.tokenizer == "nltk":
        ret = word_tokenize(text)
    else:    
        ret = text.split() # delim

    # origRet = ret
    ret = [replacelistPost.get(word, word) for word in ret]
    # if origRet != ret:
    #     print(origRet)
    #     print(ret)

    ret = [t for t in ret if t != ""]
    if not tokenize:
        ret = delim.join(ret)

    return ret

class SymbolDict(object):
    def __init__(self, empty = False): 
        self.padding = "<PAD>"
        self.unknown = "<UNK>"
        self.start = "<START>"
        self.end = "<END>"

        self.invalidSymbols = [self.padding, self.unknown, self.start, self.end]

        if empty:
            self.sym2id = {self.padding: 0} 
            self.id2sym = [self.padding]            
        else:
            self.sym2id = {self.padding: 0, self.unknown: 1, self.start: 2, self.end: 3} 
            self.id2sym = [self.padding, self.unknown, self.start, self.end]
        self.allSeqs = []

    def getNumSymbols(self):
        return len(self.sym2id)

    def isValid(self, enc):
        return enc not in self.invalidSymbols

    def resetSeqs(self):
        self.allSeqs = []

    def addSymbols(self, seq):
        if type(seq) is not list:
            seq = [seq]
        self.allSeqs += seq

    # Call to create the words-to-integers vocabulary after (reading word sequences with addSymbols). 
    def addToVocab(self, symbol):
        if symbol not in self.sym2id:
            self.sym2id[symbol] = self.getNumSymbols()
            self.id2sym.append(symbol)

    # create vocab only if not existing..?
    def createVocab(self, minCount = 0, top = 0, addUnk = False):
        counter = {}
        for symbol in self.allSeqs:
            counter[symbol] = counter.get(symbol, 0) + 1
        
        isTop = lambda symbol: True
        if top > 0:
            topItems = sorted(counter.items(), key = lambda x: x[1], reverse = True)[:top]
            tops = [k for k,v in topItems]
            isTop = lambda symbol: symbol in tops 

        if addUnk:
            self.addToVocab(self.unknown)

        for symbol in counter:
            if counter[symbol] > minCount and isTop(symbol):
                self.addToVocab(symbol)

        self.counter = counter
        self.sortedCounter = sorted(counter.items(), key = lambda x: x[1], reverse = True)[:]

    # Encodes a symbol. Returns the matching integer.
    def encodeSym(self, symbol):
        if symbol not in self.sym2id:
            symbol = self.unknown
        return self.sym2id[symbol] # self.sym2id.get(symbol, None) # # -1 VQA MAKE SURE IT DOESNT CAUSE BUGS

    # '''
    # Encodes a sequence of symbols.
    # Optionally add start, or end symbols. 
    # Optionally reverse sequence 
    # '''
    # def encodeSeq(self, decoded, addStart = False, addEnd = False, reverse = False):
    #     if reverse:
    #         decoded.reverse()
    #     if addStart:
    #         decoded = [self.start] + decoded
    #     if addEnd:
    #         decoded = decoded + [self.end]
    #     encoded = [self.encodeSym(symbol) for symbol in decoded]
    #     return encoded

    # Decodes an integer into its symbol 
    def decodeId(self, enc):
        return self.id2sym[enc] if enc < self.getNumSymbols() else self.unknown

    # '''
    # Decodes a sequence of integers into their symbols.
    # If delim is given, joins the symbols using delim,
    # Optionally reverse the resulted sequence 
    # '''
    # def decodeSeq(self, encoded, delim = None, reverse = False, stopAtInvalid = True):
    #     length = 0
    #     for i in range(len(encoded)):
    #         if not self.isValid(self.decodeId(encoded[i])) and stopAtInvalid:
    #         #if not self.isValid(encoded[i]) and stopAtInvalid:
    #             break
    #         length += 1
    #     encoded = encoded[:length]

    #     decoded = [self.decodeId(enc) for enc in encoded]
    #     if reverse:
    #         decoded.reverse()

    #     if delim is not None:
    #         return delim.join(decoded)
        
    #     return decoded

objsDict = SymbolDict(empty = True)
attrsDict = SymbolDict(empty = True) 
relsDict = SymbolDict(empty = True)
descDict = SymbolDict()
# # TODO: AVG SENTENCE WORDS!!

with open(idFilename, "r") as idFile:
    imgsInfo = json.load(idFile)
    for i in tqdm(range(len(imgsInfo))):
        imgInfo = imgsInfo[i]
        vgId = str(imgInfo["image_id"])
        cocoId = str(imgInfo["coco_id"])
        #data[cocoId] = {}
        data[vgId] = {}
        data[vgId]["width"] = imgInfo["width"]
        data[vgId]["height"] = imgInfo["height"]
        vgId2Id[vgId] = cocoId

with open("vg2coco.json", "w") as outFile:
    json.dump(vgId2Id, outFile)

with open(objectsFilename, "r") as objectsFile:
    imgsInfo = json.load(objectsFile)
    for i in tqdm(range(len(imgsInfo))):
        imgInfo = imgsInfo[i]
        vgId = str(imgInfo["image_id"])
        # cocoId = vgId
        #cocoId = vgId2Id[vgId]
        instance = data[vgId]
        instance["coco"] = vgId2Id[vgId]
        instance["objects"] = {}
        # instance["rels"] = {}
        instance["refs"] = {}
        for obj in imgInfo["objects"]:
            objId = str(obj["object_id"])
            rx0 = obj["x"]
            ry0 = obj["y"]
            rw = obj["w"]
            rh = obj["h"]
            rx1 = obj["x"] + obj["w"]
            ry1 = obj["y"] + obj["h"]
            x0 = float(obj["x"]) / instance["width"]
            y0 = float(obj["y"]) / instance["height"] 
            w = float(obj["w"]) / instance["width"]
            h = float(obj["h"]) / instance["height"]
            x1 = x0 + w
            y1 = y0 + h
            xc = float(x1 + x0) / 2
            yc = float(y1 + y0) / 2
            size = w * h
            instance["objects"][objId] = {
                "x0": x0,
                "y0": y0,
                "w": w,
                "h": h,
                "size": size,
                "x1": x1,
                "y1": y1,
                "xc": xc,
                "yc": yc,
                "rx0": rx0,
                "ry0": ry0,
                "rw": rw,
                "rh": rh,
                "rx1": rx1,
                "ry1": ry1,
                "name": obj["names"][0].strip().lower(),# obj.get("name", obj.get("names", ["NoName"])[0]),
                "outRels": {},
                "inRels": {}
            }
            # if len(obj["names"]) > 1:
            #     print(obj["names"])

            if "merged_object_ids" in obj:
                for otherId in obj["merged_object_ids"]:
                    instance["refs"][str(otherId)] = objId

            #print(obj)
            # if "name" in obj:
            #     print(obj)

            # if "name" not in obj and "names" not in obj:
            #     print(obj)
            # if len(obj["names"]) > 1:
            #     print(obj)
            objsDict.addSymbols(obj["names"][0]) # obj.get("name", "NoName")

with open(attributesFilename, "r") as attributesFile:
    imgsInfo = json.load(attributesFile)
    for i in tqdm(range(len(imgsInfo))):
        imgInfo = imgsInfo[i]
        vgId = str(imgInfo["image_id"])
        # cocoId = vgId
        #cocoId = vgId2Id[vgId]
        instance = data[vgId]
        for obj in imgInfo["attributes"]:
            objId = str(obj["object_id"])
            if objId in instance["objects"]:
                o = instance["objects"][objId]
            elif objId in instance["refs"]:
                o = instance["objects"][instance["refs"][objId]]
            else:
                continue  
                             
            if "attributes" in obj:
                attrs = obj.get("attributes",[])
                attrs = [a.strip().lower() for a in attrs]
                o["attributes"] = attrs
                attrsDict.addSymbols(attrs)  
            else:
                o["attributes"] = []

with open(relationsFilename, "r") as relationsFile:
    imgsInfo = json.load(relationsFile)
    for i in tqdm(range(len(imgsInfo))):
        imgInfo = imgsInfo[i]
        vgId = str(imgInfo["image_id"])
        # cocoId = vgId
        #cocoId = vgId2Id[vgId]
        relId = 0 
        instance = data[vgId]
        for rel in imgInfo["relationships"]:
            relName = rel["predicate"].strip().lower()
            subjId = str(rel["subject"]["object_id"])
            objId = str(rel["object"]["object_id"])
            subjId = subjId if subjId in instance["objects"] else instance["refs"].get(subjId)
            if subjId is None:
                continue
            objId = objId if objId in instance["objects"] else instance["refs"].get(objId)
            if objId is None:
                continue
            # subjN = instance["objects"][subjId]["name"]
            # objN = instance["objects"][objId]["name"]
            rel = {"rel": relName, "subj": subjId, "obj": objId} # , "subjN": subjN, "objN": objN
            #s = 
            # instance["objects"].get(subjId, instance["objects"][instance["refs"][subjId]])
            #o = 
            # instance["objects"].get(objId, instance["objects"][instance["refs"][objId]])
            if subjId is not None and objId is not None:
                instance["objects"][subjId]["outRels"][str(relId)] = rel
                instance["objects"][objId]["inRels"][str(relId)] = rel
                relId += 1
            # if (subjId is not None and objId is None) or (objId is not None and subjId is None):
            #     print(rel)
                relsDict.addSymbols(relName)

# descriptions
# with open(objectsFilename, "r") as objectsFile:
#     imgsInfo = json.load(objectsFile)
#     for i in tqdm(range(len(imgsInfo))):
#         imgInfo = imgsInfo[i]
#         vgId = str(imgInfo["image_id"])
#         cocoId = vgId
#         #cocoId = vgId2Id[vgId]
#         instance = data[cocoId]
#         instance["descriptions"] = {}
#         if "regions" in imgInfo:
#             for region in imgInfo["regions"]:
#                 regionId = str(region["region_id"])
#                 desc = vqaProcessText(region["phrase"], True, True)
#                 instance["descriptions"][regionId] = {
#                     "x": region["x"],
#                     "y": region["y"],
#                     "w": region["w"],
#                     "h": region["h"],
#                     "desc": desc,
#                 }
#                 descDict.addSymbols(desc)
        # else:
        #     print([k for k in imgInfo])

# writeVocabs()

# def writeVocabs():


objsDict.createVocab()
attrsDict.createVocab()
relsDict.createVocab()
descDict.createVocab()

with open(outDict("objs"), "wb") as outFile:
    pickle.dump(objsDict, outFile)

with open(outJson("objs"), "w") as outFile:
    json.dump(objsDict.sortedCounter, outFile)

with open(outDict("attrs"), "wb") as outFile:
    pickle.dump(attrsDict, outFile)

with open(outJson("attrs"), "w") as outFile:
    json.dump(attrsDict.sortedCounter, outFile)

with open(outDict("rels"), "wb") as outFile:
    pickle.dump(relsDict, outFile)

with open(outJson("rels"), "w") as outFile:
    json.dump(relsDict.sortedCounter, outFile)

# with open(outDict("desc"), "wb") as outFile:
#     pickle.dump(descDict, outFile)    

# sample = {}
# count = 0
# for k in data:
#     sample[k] = data[k]
#     count += 1
#     if count > 200:
#         break

with open(outIdFilename, "w") as outFile:
    json.dump(data, outFile)

# with open(outIdFilename, "r") as inFile:
#    sample = json.load(inFile)

# for imageId in sample:
#     image = GetImageData(id=imageId)
#     print ("The url of the image is: %s" % image.url)

#     fig = plt.gcf()
#     fig.set_size_inches(18.5, 10.5)
#     response = requests.get(image.url)
#     objs = list(sample[imageId]["objects"].values())
#     img = PIL_Image.open(io.BytesIO(response.content))
#     i = 0
#     j = 0
#     # if len(objs) == 0: 
#     plt.imshow(img)
#     ax = plt.gca()
#     print(len(objs))
#     for obj in objs:
#         # if i >= len(objs):
#         #     break
#         # obj = objs[i]
#         if "relations" not in obj or len(obj["relations"]) == 0:
#             continue        
#         print(obj)
#         ax.add_patch(Rectangle((obj["x"], obj["y"]),
#                                obj["w"],
#                                obj["h"],
#                                fill=False,
#                                edgecolor='red',
#                                linewidth=3))
#         text = obj["name"] + ("({})".format(",".join([x["rel"]+"-"+x["subjN"]+"-"+x["objN"] for x in obj["relations"]])) if "relations" in obj and len(obj["relations"]) > 0 else "")
#         ax.text(obj["x"], obj["y"], text, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})
#         # i += 1
#     fig = plt.gcf()
#     plt.tick_params(labelbottom='off', labelleft='off')
#     #plt.show()
#     plt.savefig(imageId+"_rel.jpg", dpi = 720) # +"_"+str(j)
#     plt.close(fig)
#     j += 1
