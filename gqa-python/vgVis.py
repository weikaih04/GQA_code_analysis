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
import utils

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


sample = json.load(open("vg14/metadata_annotationsNew.json"))
def GetImageData(id=61512):
  data = utils.retrieve_data('/api/v0/images/' + str(id))
  if 'detail' in data and data['detail'] == 'Not found.':
    return None
  image = utils.parse_image_data(data)
  return image

for imageId in ["2379902"]:
    image = GetImageData(id=imageId)
    print ("The url of the image is: %s" % image.url)

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    # response = session.get(image.url)
    # response = requests.get(image.url)
    objs = list(sample[imageId]["objects"].values())
    img = PIL_Image.open("../../Downloads/2379902.jpg")
    i = 0
    j = 0
    # if len(objs) == 0: 
    plt.imshow(img)
    ax = plt.gca()
    print(len(objs))
    for obj in objs:
        # if i >= len(objs):
        #     break
        # obj = objs[i]
        # if "relations" not in obj or len(obj["relations"]) == 0:
        #     continue        
        print(obj)
        ax.add_patch(Rectangle((obj["rx0"], obj["ry0"]),
                               obj["rw"],
                               obj["rh"],
                               fill=False,
                               edgecolor='red',
                               linewidth=3))
        text = obj["name"]
        #  + ("({})".format(",".join([x["rel"]+"-"+x["subjN"]+"-"+x["objN"] for x in obj["relations"]])) if "relations" in obj and len(obj["relations"]) > 0 else ""
        ax.text(obj["rx0"], obj["ry0"], text, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})
        # i += 1
    fig = plt.gcf()
    plt.tick_params(labelbottom='off', labelleft='off')
    #plt.show()
    plt.savefig(imageId+"New.jpg", dpi = 720) # +"_"+str(j)
    plt.close(fig)
    j += 1