import json
from collections import defaultdict
# import en 

prefix = "on" # "abo"
inpName = "on.py"

catcJ = open("{}_catc.json".format(prefix), "w")
catsJ = open("{}_cats.json".format(prefix), "w")
catoJ = open("{}_cato.json".format(prefix), "w")

oncWJ = open("{}cW.json".format(prefix), "w")
onsWJ = open("{}sW.json".format(prefix), "w")
onoWJ = open("{}oW.json".format(prefix), "w")

oncBJ = open("{}cB.json".format(prefix), "w")
onsBJ = open("{}sB.json".format(prefix), "w")
onoBJ = open("{}oB.json".format(prefix), "w")

catcT = open("{}_catc.txt".format(prefix), "w")
oncTs = open("{}_oncs.txt".format(prefix), "w")

scT = open("{}_sc.txt".format(prefix), "w")
ocT = open("{}_oc.txt".format(prefix), "w")

catcTs = open("{}_catcs.txt".format(prefix), "w")
catsT = open("{}_cats.txt".format(prefix), "w")
catoT = open("{}_cato.txt".format(prefix), "w")
byS = open("{}_bys.txt".format(prefix), "w")
byO = open("{}_byo.txt".format(prefix), "w")
top2S = open("{}_top2s.txt".format(prefix), "w")
top2O = open("{}_top2O.txt".format(prefix), "w")
top2SS = open("{}_top2ss.txt".format(prefix), "w")
top2OO = open("{}_top2oo.txt".format(prefix), "w")

oncWT = open("{}cW.txt".format(prefix), "w")
onsWT = open("{}sW.txt".format(prefix), "w")
onoWT = open("{}oW.txt".format(prefix), "w")
oncWTs = open("{}csW.txt".format(prefix), "w")

oncBT = open("{}cB.txt".format(prefix), "w")
onsBT = open("{}sB.txt".format(prefix), "w")
onoBT = open("{}oB.txt".format(prefix), "w")
oncBTs = open("{}csB.txt".format(prefix), "w")

# V blacklisting split
# V top stats per s/o cat
# V top s/o 2

def catn(o):
    return objDict[o]["cat"]

def isPlural(o):
    return objDict[o]["mod"] == "plural"
    
def singularOf(objname):
    return en.noun.singular(objname)

def pluralOf(objname):
    return en.noun.plural(singularOf(objname))

def filterAt(s, o):
    toOn = ["beach", "sidewalk", "platform", "island", "tarmac", "podium", "shore", "pathway", 
            "street", "pavement", "stairs", "sea"]
    toIn = ["park", "skate park", "restaurant", "field", "harbor", "river", "market", "room", "water", "area", "court", "parking lot", 
            "stadium", "bleachers", "parade", "store"]
    
    blacklist = [("water", "beach"), ("runway", "airport"), ("car", "curb"), ("player", "bat"), ("tarmac", "airport"), 
        ("ocean", "beach"), ("curtain", "window"), ("man", "bat"), ("tree", "edge"), ("streetlamp", "night"), 
        ("curtains", "window"), ("waves", "beach"), ("water", "sand"), ("sky", "sunset"), ("arm", "side"), 
        ("building", "water"), ("trees", "edge"), ("faucet", "sink"), ("tree", "bottom"), ("light", "night"), 
        ("window", "building"), ("foaming wave", "sea"), ("people", "terrain"), ("cow", "camera"), 
        ("trees", "parking"), ("bear", "terrain"), ("glass", "table"), ("flower", "circle"), ("cars", "curb"), 
        ("person", "slope"), ("batter", "bat"), ("stripe", "top"), ("pot", "windowsil"), ("man", "base"), 
        ("plane", "airfield"), ("lights", "night"), ("boat", "anchor"), ("batter", "base")]

    for b in blacklist:
        if s == b[0] and o == b[1]:
            Remove

    if o in toOn:
        rel["rel"] = "on"

    if o in toIn:
        rel["rel"] = "in"

    if o == "zoo" and isA(s, "animal"):
        rel["rel"] = "in"

def filterOn(s, o):
    # numbers, chair, branch, trunk wall
    background = ["background", "ground", "terrain", "land", "cloud", "clouds", "mountains", "rock", "rocks", "boulders", "sky", "rain", "snow flakes", "sea foam", "fire", "stone", "stones", "wave", "waves", "bubble", "bubbles", "steam", "smoke", "leaf", "petal", "petals", "branch", "branches", "tree branch", "tree branches", "twig", "twigs", "stick", "sticks", "log", "logs", "stump", "cliff", "island", "waterfall", "moon", "sun", "air", "ceiling", "roof", "floor", "deck", "wall", "walls", "wallpaper", "step", "steps", "staircase", "stairs", "window", "windows", "door", "doors", "garage door", "tile", "floor tile", "pillars", "bridge", "elevator", "chimney", "smoke stack", "paint", "platform", "hook"]
    blacklistSubjects = ["fence post", "seed", "post", "handle", "heel", "pocket", "pockets", "frame", "drawers", "drawer", "belt", "balcony", "crust", "floor", "window", "windows", "tile", "leaf", "door", "doors", "hair", "skin", "fur", "wool", "feathers"]
    blacklistObjects = ["glasses", "strap", "air", "land", "ground", "step", "oven door", "soup", "mirror", "pen", "background", "wave", "waves", "number", "numbers", "word", "words", "weeds", "weed", "skis", "plant", "plants", "sandwiches", "characters", "character", "painting", "drawing", "ring", "fire", "collar", "money", "phones", "phone", "display", "photo", "tile", "wheels", "wheel"] # mirror?
    sblackcat = ["body part", "part", "vehicle part", "place", "road", "building", "room"]
    clothing = ["clothing", "footwear", "accessory"]
    oblackcat = ["building", "vehicle", "aircraft", "clothing", "device", "part", "accessory", "label", "symbol", "meal", "drink", "weapon", "person", "body part", "room"]
    hats = ["chef hat", "cowboy hat", "hat", "hats", "cap", "crown", "bandage", "helmet", "sugar", "watch", "wristwatch", "bracelet"] 
    waterWhitelist = ["surfboard", "ice", "snow"]
    waterWhitelistCat = ["animal", "watercraft"]
    curtains = ["curtain", "curtains", "drape", "drapes", "blind", "blinds", "shower curtain"] 
    containers = ["bottle", "bottles", "cup", "container", "containers", "food container", "egg carton", "milk carton", "jar", "jars", "cookie jar", "box", 
    "storage box", "juice box", "cereal box", "bread box", "lunch box", "pizza box", "pizza boxes", "boxes", 
    "canister", "canisters", "package", "packages", "basket", "baskets", "bowl", "bowls"]
    onWindow = ["curtain", "blinds", "curtains", "sign", "drapes", "number", "words", "lock", "drape"]
    food = ["food", "fruit", "vegetable", "dessert", 'baked good', 'meat', 'fast food', 'sauce', 'ingredient']
    foodExtra = ["icing", "frosting", "glaze", "powder"]
    extraParts = ["door frame", "doorway", "window frame", "touchpad", "horse hoof", "strap", "straps", "hair", "skin", "fur", "wool", "feathers", "seat belt", "cockpit"]
    chairs = ["office chair", "chairs", "couch", "couches", "sofa", "bench", "chair"]
    vehicleWhitelistCats = ["person", "animal"]
    bags = ["bag", "bags", "pouch", "purse", "wallet", "handbag", "backpack", "backpacks", "briefcase", "luggage", 
    "suitcase", "suitcases", "luggage cart", "shopping bag", "sack", "trash bag"]
    vehicleWhitelist = ["ladder", "surfboard", "ladder", "antenna", "flag", "basket", "helmet", "chain"] 
    buildingWhitelist = ["clock", "sign", "flag", "cross", "statue", "dome", "pole", "number", "flags", "flag", 
    "antenna", "statue", "cross", "satellite dish", "bell", "snow", "flag", "clocks", "bell", "sculpture", "antenna", 
    "bird", "birds", "snow"]
    person = ["man", "person", "woman", "girl", "people", "guy", "lady"]

    blacklist = [("train", "windshield"), ("containers", "spices"), ("cap", "oil"), ("cup", "flour"),
    ("socks", "shoe"), ("scissors", "balloon"), ("keyboard", "piano"), ("airplane", "wing"), 
    ("gloves", "bat"), ("tree", "trunk"), ("tree", "trunks"), ("trees", "trunk"), ("trees", "trunks"), 
    ("faucet", "sink"), ("bear", "branch"), ("elephant", "branch"), ("duck", "branch"), ("soda", "post"), 
    ("toilet", "wall"), ("sink", "wall"), ("refrigerator", "wall"), ("cabinets", "wall"), ("cabinet", "wall"), 
    ("box", "herbs"), ("drawers", "nightstand"), ("drink", "food"), ("plate", "food"), ("food", "oven"), 
    ("chicken", "oven"), ("fish", "oven"), ("bread", "microwave"), ("seat", "toilet"),
    ("pears", "microwave"), ("glass", "door"), ("glass", "building"), ("glass", "train"), ("glass", "bus"), 
    ("glass", "wall"), ("glass", "oven"), ("glass", "car"), ("glass", "cabinet door"),  ("glass", "motorcycle"), 
    ("glass", "pole"), ("glass", "shower"), ("glass", "parking meter"),  ("glass", "helmet"), ("glass", "shop"), 
    ("glass", "clock"), ("glass", "computer"), ("glass", "ceiling"), ("glass", "tower"), ("glass", "cockpit"), 
    ("glass", "roof"), ("glass", "island"), ("glass", "label"), ("glass", "screen"), ("glass", "windshield"), 
    ("glass", "monitor"), ("glass", "bridge"), ("glass", "balcony"), ("glass", "television"), ("glass", "street"), 
    ("glass", "menu"), ("train", "boat"), ("plant", "pot"), ("pole", "canopy"), ("cabinet", "door"), ("lid", "toilet"), 
    ("bowl", "toilet"), ("hat", "face"), ("helmet", "face"), ("people", "seat"), ("grass", "park"), ("post", "pole"), 
    ("toilet", "floor"), ("man", "statue"), ("person", "statue"), ("woman", "statue"), 
    ("elephant", "water"), ("horse", "water"), ("dog", "water"), ("bear", "water"), 
    ("faucet", "wall"), ("man", "wall"), ("fence", "wall"), ("fireplace", "wall"), ("toaster", "wall"), 
    ("person", "wall"), ("sheep", "wall"), ("oven", "wall"), ("tree", "wall"), ("woman", "wall"), ("vase", "wall"), 
    ("microwave", "wall"), ("chair", "wall"), ("container", "wall"), ("shower", "wall"), ("book", "wall"), 
    ("cow", "wall"), ("boy", "wall"), ("people", "wall"), ("deer", "wall"), ("grass", "floor"), ("urinal", "floor"),
    ("leaves", "grass"), ("leaves", "branches"), ("leaves", "bush"), ("leaves", "leaves"), 
    ("leaves", "tree branch"), ("leaves", "flower"), ("leaves", "flowers"), ("leaves", "vine"), 
    ("leaves", "tree branches"), ("leaves", "hillside"), ("tree leaves", "tree"), ("leaves", "crust") ]

    whitelist = [("whipped cream", "milkshake"), ("whipped cream", "drink"), ("strawberry", "smoothie"),
    ("snow", "ground"), ("grass", "groun"), ("leaves", "ground"), ("ball", "ground"), ("bag", "ground"), 
    ("backpack", "ground"), ("kite", "ground"), ("bottle", "ground"), ("box", "ground"), ("suitcase", "ground"), 
    ("bucket", "ground"), ("cup", "groun"), ("frisbee", "ground"), ("luggage", "ground"), ("carpet", "ground"), 
    ("bat", "ground"), ("fruit", "ground"), ("snowboard", "ground"), ("helmet", "ground"), ("shoes", "ground"), 
    ("banana", "ground"), ("rug", "ground"), ("pot", "ground"), ("snow", "car"), ("dog", "bike"), ("towel", "oven door"), 
    ("towels", "oven door"),  ("cross", "necklace"), ("beads", "necklace"), ("bead", "necklace"), ("heart", "necklace"), 
    ("cat", "laptop"), ("cat", "computer"), ("cat", "keyboard"), ("animal", "computer"), ("book", "computer"), 
    ("pen", "keyboard"), ("kitten", "laptop"), ("antenna", "television"), ("antenna", "cell phone"),  
    ("flowers", "laptop"), ("basket", "bike"), ("helmet", "motorcycle"), ("cat", "car"), ("man", "train"), 
    ("person", "bus"), ("man", "bus"), ("helmet", "bike"), ("bag", "bike"), ("bag", "motorcycle"), 
    ("people", "train"), ("driver", "bus"), ("passenger", "bus"), ("ladder", "truck"), ("flag", "truck"), 
    ("surfboard", "car"), ("ladder", "train"), ("flag", "bus"), ("bell", "train"), ("cat", "jeep"), ("bike", "bus"), 
    ("passenger", "train"), ("toy", "car"), ("bags", "truck"), ("passengers", "bus"), ("flag", "airplane"), 
    ("star", "airplane"), ("man", "airplane"), ("people", "airplane"), ("person", "airplane"), 
    ("mickey mouse", "airplane"), ("passenger", "airplane"), ("pilot", "airplane"), ("girl", "airplane"), 
    ("antennas", "airplane"), ("woman", "airplane"), ("antenna", "airplane"), ("flags", "airplane"), 
    ("flag", "aircraft"), ("antenna", "aircraft"), ("man", "bike"), ("man", "motorcycle"), ("person", "bike"), 
    ("woman", "bike"), ("basket", "bike"), ("helmet", "motorcycle"), ("woman", "motorcycle"), ("cat", "car"), 
    ("man", "train"), ("person", "bus"), ("man", "bus"), ("man", "scooter"), ("people", "bus"), ("bag", "bike"), 
    ("bag", "motorcycle"), ("people", "train"), ("driver", "bus"), ("passenger", "bus"), ("dog", "motorcycle"), 
    ("ladder", "truck"), ("person", "train"), ("flag", "train"), ("flag", "motorcycle"), ("chain", "bike"), 
    ("box", "train"), ("flag", "truck"), ("guy", "bike"), ("person", "scooter"), ("boy", "bike"), ("dog", "bike"), 
    ("surfboard", "car"), ("ladder", "train"), ("flag", "bus"), ("bike", "bus"), ("passenger", "train"), 
    ("woman", "bus"), ("birds", "car"), ("snow", "car"), ("toy", "car"), ("bags", "truck"), ("luggage", "truck"), 
    ("sack", "wagon"), ("antenna", "car"), ("dog", "truck"), ("box", "motorcycle"), ("ladder", "car"), 
    ("antenna", "motorcycle"), ("bananas", "bike"), ("bike", "train"), ("man", "car"), ("container", "train"), 
    ("flower", "truck"), ("bike", "car"), ("surfboard", "vehicle"), ("kitten", "bus"), ("box", "bike"), 
    ("surfboard", "truck"), ("backpack", "bike"), ("dog", "bus"), ("luggage", "motorcycle"), ("sack", "scooter"), 
    ("cows", "truck"), ("grass", "ground"), ("glove", "hand"), ("ring", "finger"), ("flowers", "grass"),
    ("tag", "ear"), ("airplane", "ground"), ("bird", "ground"), ("chimney", "roof"), ("building", "hill")]

    # word/s number/s
    # post_
    # label
    # donut_bag bags
    # floor
    # water
    # vase
    # wall

    # if in more popular replace < 10 > 20

    if isPlural(o) and not isPlural(s) and o not in ["rocks", "steps", "stairs", "papers", "books"] and s not in ["snow","grass"] and not (s == "train" and o == "train tracks") and not (catn(o) in food and (catn(s) in food or s in foodExtra)):
        return True
    for bd in whitelist:
        if s == bd[0] and o == bd[1]:
            return False    
    if (catn(s) in vehicleWhitelistCats or s in bags or s in vehicleWhitelist) and catn(o) == "vehicle":
        return False 
    if s in buildingWhitelist and catn(o) == "building":
        return False
    if s in hats and catn(o) == "body part":
        return False        
    for bd in blacklist:
        if s == bd[0] and o == bd[1]:
            return True         
    # if s in person and o in chairs:
    #   return True
    if catn(s) == "flower" and o == "vase":
        return True
    if s in extraParts:
        return True
    if s not in onWindow and o in ["window", "windows"]:
        return True
    if o in containers and s != "lid":
        return True     
    if (s in background or s in blacklistSubjects or catn(s) in sblackcat) and s not in ["bracelet"]:
        return True
    if (o in blacklistObjects or catn(o) in oblackcat) and o not in ["handle"]:
        return True
    if catn(o) in oblackcat: # and catn(s) in clothing:
        return True
    if o == "water" and s not in waterWhitelist and catn(s) not in waterWhitelistCat:
        return True
    if s in curtains and o not in ["window", "door"]:
        return True
    if (catn(s) in ["person", "animal"] or s in ["bear", "teddy bear"]) and catn(o) in ["clothing", "footwear"]:
        return True
    # if isPlural(o) and not isPlural(s) and (catn(o) in food and (catn(s) in food or s in foodExtra)):
    #   return False
    # if catn(s) in ["animal"] and catn(o) in ["clothing", "footwear"]:
    #   return False    
    return False

# window / mirror 
# natural env: stick, leaf pillars bubble log ( also for on)
# TODO on the head, hand,... earring / ear/nose in the mouth?
# as expression: in the sauce, cheese, rain foil sun, wall in the
# toOn: curtain,in,window, road, pizza
def filterIn(s, o):
    whitelist = [("foot", "sand"),  
        ("hair", "sink"), ("card", "pocket"), ("cards", "pocket"), ("cards", "car"), 
        ("receipt", "box"), ("card", "wallet"), ("tire", "water"), ("tire", "suitcase"),
        ("paper", "printer"), ("vegetable", "pizza"), ("tomato", "pizza"), ("cheese", "hot dog"), ("sauce", "pizza"), 
        ("pepperoni", "pizza"), ("egg", "pizza"), ("peppers", "pizza"), ("basil", "pizza"), ("ham", "pizza"), 
        ("onion", "hot dog"), ("ketchup", "hot dog"), ("candle", "pizza"), ("mushroom", "pizza"), ("meat", "pizza"),
        ("tag", "ear"), ("baby", "blanket"), ("pig", "blanket"), ("cat", "blanket"), ("knife", "apple"), 
        ("drawer", "desk"), ("drawers", "desk"), ("drawer", "table"), ("drawers", "table"), ("bird", "clouds"), 
        ("airplane", "clouds"), ("kite", "clouds"), ("stick", "bread"), ("sticks", "vase"), ("stick", "pot"), 
        ("stick", "sandwich"), ("stick", "buns"), ("stick", "cake"), ("leaves", "background"), ("leaves", "pond"), 
        ("leaves", "basket"), ("leaves", "living room"), ("leaves", "container"), ("leaves", "window"), 
        ("leaves", "bag"), ("leaves", "jar"), ("clock", "tower"), ("flower", "bouquet"), ("house", "mountains") ] # ("hand", "pocket"),  ("hand", "snow"), ("hands", "pockets"), 
        # ("feet", "sand"), ("feet", "water"), 

    blacklist = [("pot", "flower"), ("faucet", "sink"), ("toilet", "room"), ("furniture", "glass"),
        ("curtains", "window"), ("blind", "window"), ("blinds", "window"), ("sign", "snow"), ("umbrella", "sand"), 
        ("sign", "grass"), ("bag", "can"),("curtain", "window"), ("air conditioner", "window"), ("leaves", "tree"), 
        ("water", "toilet"), ("sign", "window"), ("water", "ocean"), ("cloud", "clouds"), ("sheep", "sheep"), 
        ("airplane", "airplanes"), ("bag", "bags"), ("banana", "bananas"), ("knife", "knives"), ("glass", "glass"), 
        ("fruit", "fruit"), ("building", "buildings"), ("orange", "oranges"), ("car", "cars"), ("person", "people"), 
        ("chicken", "chickens"), ("boat", "boats"), ("mountain", "mountains"), ("elephant", "elephants"), 
        ("cabinet", "cabinets"), ("bread", "bread"), ("luggage", "luggage"), ("cup", "cups"), ("sand", "sand"), 
        ("peanut butter"), ("peanut butter"), ("hot dogs", "croissant"), ("zucchini", "meat"), ("pepper", "meat"), 
        ("bun", "sausage"), ("pepperoni", "pepperoni"), ("utensil", "meat"), ("orange", "meat"), ("hamburger", "meat"),
        ("background", "sky"), ("box", "sky"), ("bridge", "sky"), ("number", "sky"), ("propeller", "sky"), 
        ("seeds", "sky"), ("steam", "sky"), ("smoke", "sky"), ("crane", "sky"), ("leaf", "sky"), ("sign", "sky"), 
        ("cross", "sky"), ("wing", "sky"), ("mountains", "sky"), ("cables", "sky"), ("mountain", "sky"), 
        ("clock", "sky"), ("stick", "mud"), ("cap", "river"), ("sign", "shop"), ("bubbles", "ocean"), 
        ("bubble", "ocean"), ("bubbles", "sink"), ("bubbles", "river"), ("bubbles", "bathroom"), ("bubble", "pan"), 
        ("land", "ocean"), ("woman", "ladle"), ("lid", "pan"), ("price tag", "pan"), ("cake", "pans"), 
        ("pie", "pans"), ("pot", "pans"), ("basket", "pot"), ("bottle", "pot"), ("bowl", "pot"), ("brush", "pot"), 
        ("container", "pot"), ("mixer", "pot"), ("plates", "pot"), ("tool", "pot"), ("nut", "brownies"), 
        ("vanilla", "ice cream"), ("fruit", "cake"), ("glass", "dessert"), ("dip", "cake"), ("camera", "cake"), 
        ("candle", "cakes"), ("cookies", "cupcake"), ("cake", "cupcake"), ("cat", "cake"), ("dog", "cake"), 
        ("people", "cake"), ("cake slice", "cake"), ("woman", "cake"), ("cookies", "cupcakes"), ("beer", "drink"), 
        ("beer", "beverage"), ("liquid", "drink"), ("cream", "drink"), ("cappuccino", "coffee"), ("glass", "wine"), 
        ("wine", "drink"), ("cup", "coffee"), ("napkin", "coffee"), ("motorcycle", "bed"), ("wall", "bed"), 
        ("wall", "entertainment center"), ("cap", "bottle"), ("cup", "bottle"), ("milk", "cereal"), 
        ("candle", "chocolate"), ("mound", "food"), ("hot dog", "food"), ("drape", "window"), ("glass", "window"), 
        ("drapes", "window"), ("blind", "window"), ("blinds", "window"), ("curtain", "window"), 
        ("curtains", "window"), ("man", "cooker"), ("bowl", "stove"), ("clouds", "mountains"), 
        ("clock", "alarm clock"), ("man", "backpacks"), ("boy", "suitcase"), ("girl", "suitcase"), 
        ("workers", "bucket"), ("woman", "suitcase"), ("land", "water"), ("sail", "water"), 
        ("sign", "water"), ("deck", "water"), ("lighthouse", "water"), ("pillars", "water"), 
        ("beach", "water"), ("platform", "water"), ("stairs", "water"), ("stick", "water"), ("log", "water"), 
        ("trunk", "water"), ("post", "water"), ("bone", "water"), ("ocean", "water"), ("island", "water"), 
        ("mountain", "water"), ("waterfall", "water"), ("mud", "water"), ("stump", "water"), ("forest", "water"), 
        ("sticks", "water"), ("pole", "water"), ("ice", "water"), ("sidewalk", "street"),
        ("grass", "water"), ("weeds", "field"), ("grass", "forest"), ("plants", "water"), ("grass", "pond"), 
        ("plants", "forest"), ("plants", "yard"), ("grass", "backyard"), ("bush", "backyard"), ("grass", "basket"), 
        ("grass", "garden"), ("weeds", "snow"), ("bushes", "yard"), ("bush", "forest"), ("hay", "field"),
        ("pond", "field"), ("bleachers", "stadium"), ("pond", "park"), ("pond", "zoo"), ("house", "field"), 
        ("barn", "field"), ("clock tower", "park"), ("building", "forest"), ("container", "glass"), 
        ("trunks", "background"), ("coat", "snow"), ("clothes", "sand"), ("wetsuit", "ocean"), 
        ("blinds", "windows"), ("pizza", "background"), ("food", "shop"), ("food", "restaurant"), 
        ("sign", "background"), ("glass", "cabinet"), ("crane", "background"), ("bridge", "water"), 
        ("countertop", "kitchen"), ("stump", "sand"), ("outlet", "kitchen"), ("countertop", "bathroom"), 
        ("bowl", "bathroom"), ("crane", "water"), ("umbrella", "crowd"), ("vines", "field"), ("plants", "field"), 
        ("plant", "field"), ("weed", "field"), ("weeds", "forest"), ("plant", "forest"), ("bushes", "forest"), 
        ("weed", "garden"), ("weeds", "garden"), ("plant", "garden"), ("bush", "garden"), ("plants", "garden"), 
        ("plants", "lake"), ("grass", "lawn"), ("weeds", "mud"), ("grass", "mud"), ("grass", "ocean"), 
        ("weeds", "ocean"), ("flowers", "paper"), ("bush", "park"), ("grass", "park"), ("bushes", "park"), 
        ("bush", "parking lot"), ("plant", "plain"), ("grass", "plain"), ("bush", "pond"), ("plant", "pond"), 
        ("grass", "river"), ("plant", "river"), ("weeds", "river"), ("bush", "river"), ("grass", "sky"), 
        ("plants", "snow"), ("plant", "snow"), ("weeds", "steps"), ("bushes", "train"), ("bushes", "water"), 
        ("weed", "water"), ("bush", "water"), ("grass", "weeds"), ("flowers", "weeds"), ("weeds", "yard"), 
        ("plant", "zoo"), ("ski", "snow"), ("seat", "bleachers"), ("seat", "car"), ("leaf", "water"),  
        ("seat", "bathroom"), ("seat", "boat"), ("seat", "bus"), ("seat", "auditorium"), ("bubble", "water"), 
        ("log", "field"), ("fence", "yard"), ("ski", "water"), ("snow", "sky"), ("stick", "bathroom"), 
        ("seat", "vehicle"), ("leaves", "forest"), ("leaves", "field"), ("stick", "sand"), ("leaves", "pot"), 
        ("leaf", "bowl"), ("leaf", "pot"), ("leaf", "glass"), ("leaf", "pond"), ("leaves", "yard"), 
        ("lid", "bathroom"), ("sticks", "snow"), ("frosting", "cake"), ("leaf", "salad"), ("bubble", "coffee"), 
        ("seed", "field"), ("tree branch", "background"), ("leaf", "soup"), ("seed", "food"), 
        ("leaves", "park"), ("leaves", "snow"), ("leaves", "salad"), ("leaf", "park"), ("sticks", "field"), 
        ("leaves", "bowl"), ("grass", "water"), ("weeds", "field"), ("grass", "forest"), ("plants", "water"), 
        ("grass", "pond"), ("plants", "forest"), ("plants", "yard"), ("grass", "backyard"), ("bush", "backyard"), 
        ("grass", "basket"), ("grass", "garden"), ("weeds", "snow"), ("bushes", "yard"), ("bush", "forest"), 
        ("hay", "field"), ("flag", "sky"), ("tree", "sky"), ("tree", "water"), ("trees", "sky"), ("trees", "water"), 
        ("fence", "field"), ("leaf", "vase"), ("fence", "grass"), ("leaves", "water"), ("seat", "stadium"), 
        ("leaves", "vase"), ("fence", "park"), ("leaf", "snow"), ("stick", "snow"), ("seat", "bleachers"),
        ("seat", "stadium"), ("person", "boats"), ("microwave", "cabinets"), ("fruit", "baskets"), 
        ("toothbrush", "cups"), ("fruit", "boxes"), ("pepper", "mashed potatoes"), ("hot dog", "buns"), 
        ("spoon", "pots"), ("plant", "pots"), ("refrigerator", "cabinets"), ("sink", "cabinets"), 
        ("sheep", "cages"), ("potato", "pots"), ("tomato", "sandwiches"), ("oven", "cabinets"), 
        ("silverware", "plates"), ("trees", "houses"), ("lid", "dish"), ("lid", "cupboard"), 
        ("lid", "bag"), ("tree branch", "water"), ("tree branches", "sky"), ("bubbles", "bathtub"),
        ("seaweed", "sand"), ("stick", "weeds"), ("log", "weeds"), ("man", "glass"), 
        ("cat", "glass"), ("kitten", "glass"), ("tree", "glass"), ("clock", "glass"), ("trees", "glass"), 
        ("glass", "bathroom"), ("snow", "grass"), ("sign", "field"), ("stick", "field"), ("mirror", "car"), 
        ("mirror", "vehicle"), ("mirror", "park"), ("mirror", "window"), ("mirror", "train"), ("mirror", "minivan"),
        ("chair", "stadium"), ("lamb", "hay")]

    blacklistS = ["seat", "leaves", "leaf", "log", "pillars", "stick", "sticks", "bush", "bubble", "fence post", "post", "mound", "screen", "background", "ceiling", "pole", "wall", "garage door", "shower door", "cabinet doors", "cabinet door", "door", "doors", 
    "doorway", "doorways", "tiles", "air", "sky", "floor", "wave", "waves"]
    blacklistO = ["windows", "hill", "table", "mountain side", "wallpaper", "terrain", "wave", "waves", "rain", "mountains", "land", "town", "shore", "mountain", "hills", "hillside", "hilltop", "entrance", "dock", "display", "city", "room", "flower", "flowers", "bush", "motorcycle", "bike", "candy", "cheese", "chips", "chocolate", "cream cheese", "cream", "dip", "egg", "eggs", 
    "mozzarella", "parmesan cheese", "carpet" ,"ceiling" ,"roof" ,"staircase" ,"stairs" ,"walls", "cutting board", 
    "picnic table", "furniture", "armchair", "desk", "shelf", "shelves", "buildings", "house", "apartment", 
    "utensil", "wig", "door", "doors", "fence", "glasses", "tower", "tree", "trees", "wall", "floor", 
    "building", "herd", "ground", "cap", "post", "fence post", "sign post"] 
    blacklistScat = ["place", "nature environment", "urban environment", "meal", "road", "vehicle part", "part", "room", "label", "body part"]
    blacklistOcat = ["road", "office supplies", "animal", "person", "sauce", "textile", "fast food", "device", 
    "meal", "part", "footwear", "vehicle part", "label", "ingredient", "accessory", "clothing", "body part", "utensil"]
    chairs = ["office chair", "chairs", "couch", "couches", "sofa", "bench", "chair"]
    waterWhitelsit = ["mug", "glass", "vase", "bowl", "bottle", "cup", "jar", "fountain", "sink", "bathtub", "bucket", "container", 
        "glasses", "bottles", "flower pot", "basket", "aquarium"] 
    natural = ["sand", "rock", "rocks", "boulders", "water", "mud", "ice", "stone", "stones", "leaf", "leaves", 
        "tree leaves", "petal", "petals", "branch", "branches", "tree branch", "tree branches", "twig", 
        "twigs", "stick", "sticks", "log", "logs", "stump"]
    naturalR = ["branch", "branches", "twig", "twigs", "stone", "stones", "rock", "rocks", "tile", "hair", "skin", "fur", "wool", "feathers"]
    extraParts = ["door frame", "doorway", "window frame", "touchpad", "horse hoof", "strap", "straps", "hair", "skin", "fur", "wool", "feathers", "seat belt", "cockpit"]
    inclusiveObjs = ["stroller", "pot", "planter", "mirror", "backpack", "bag", "basket", "baskets", "bird cage", "bowl", "briefcase", "bucket", "can", 
        "candle holder", "cart", "crate", "crates", "dish drainer", "dispenser", "dumpster", "flower pot", "grinder", 
        "knife block", "napkin dispenser", "package", "pouch", "salt shaker", "suitcase", "tissue box", "towel dispenser", 
        "tray", "utensil holder", "vase", "vending machine", "wallet", "waste basket", "wheelchair"] 
    airWhitelist = ["phone", "pigeon", "aircraft", "dog", "guy", "airplane", "jet", "man", "apple", "snowboards", 
    "frisbee", "snowboard", "snowboarder", "bike", "birds", "skateboarder", "kite", "skier", "kites", "boy", "ball", 
    "horse", "people", "surfer", "woman", "helicopter", "shoe", "skis", "person", "balloon", "motorcycle", "player", 
    "bird", "baseball", "airplanes", "skateboard"]
    noneWhitelist = ["net", "pen", "air", "aquarium", "audience", "bathtub", "cockpit", "cooler", "crowd", "doorway", "fireplace", "fountain", 
        "glass", "pitcher", "pocket", "pockets", "shower", "sink"]
    thingWhitelist = ["cages", "cage", "ice", "nest", "painting", "napkin", "paper", "sand", "snow", "tent", "water"]

    for w in whitelist:
        if s == w[0] and o == w[1]:
            return False
    for b in blacklist:
        if s == b[0] and o == b[1]:
            return True
    if s in blacklistS or catn(s) in blacklistScat:
        return True
    if o in blacklistO or catn(o) in blacklistOcat:
        return True
    # if o in ["mirror", "window"]:
    #   return False
    if s in ["window", "windows"]: # and o not in ["bathroom", "kitchen", "bedroom", "living room"]:
        return True
    if o in chairs:
        return True
    if s == "water" and o not in waterWhitelsit:
        return True
    if (catn(s) in ["plant", "tree"] or s in natural) and o in ["grass", "bushes"]:
        return True
    if s in naturalR or o in naturalR:
        return True
    if catn(o) == "symbol" and o not in ["drawing", "drawings"]:
        return True
    if catn(s) == "symbol" and s not in ["drawing", "drawings"]:
        return True     
    if catn(o) == "plant" and o not in ["grass", "bushes", "hay", "weeds"]:
        return True     
    if catn(o) in ["vegetable", "fruit"] and s not in ["seed", "seeds"]:
        return True 
    if catn(o) == "aircraft" and catn(s) != "person":
        return True
    if s in extraParts:
        return True
    if catn(o) == "object" and o not in inclusiveObjs:
        return True
    if catn(o) == "" and o not in noneWhitelist:
        return True 
    if catn(o) == "thing" and o not in thingWhitelist:
        return True             
    if o == "air" and s not in airWhitelist:
        return True
    if catn(s) == "building" and o != "background":
        return True
    return False

    # if not isPlural(s) and pluralOf(s) == o:
    #   return True
    # if  isPlural(s) and isPlural(o):
    #   return False
    #  singular/plural bubble
    #   body part as subject
    #snow (covered in), without the?
    # in glass 
    # _field


def filterInside(s, o):
    whitelist = [  
        ("frisbee", "mouth"), ("hand", "glove"), ("toothbrush", "mouth"),
        ("hair", "sink"), ("card", "pocket"), ("cards", "pocket"), ("cards", "car"), 
        ("receipt", "box"), ("card", "wallet"), ("tire", "water"), ("tire", "suitcase"),
        ("paper", "printer"),  ("cheese", "hot dog"), 
        ("onion", "hot dog"), ("ketchup", "hot dog"),  
        ("baby", "blanket"), ("pig", "blanket"), ("cat", "blanket"), ("knife", "apple"), 
        ("drawer", "desk"), ("drawers", "desk"), ("drawer", "table"), ("drawers", "table"), ("bird", "clouds"), 
        ("airplane", "clouds"), ("kite", "clouds"), ("stick", "bread"), ("sticks", "vase"), ("stick", "pot"), 
        ("stick", "sandwich"), ("stick", "buns"), ("stick", "cake"), ("leaves", "background"), ("leaves", "pond"), 
        ("leaves", "basket"), ("leaves", "living room"), ("leaves", "container"), 
        ("leaves", "bag"), ("leaves", "jar"), ("flower", "bouquet") ] # ("hand", "pocket"),  ("hand", "snow"), ("hands", "pockets"), 
        # ("feet", "sand"), ("feet", "water"), 

    blacklist = [("pot", "flower"), ("faucet", "sink"), ("toilet", "room"), ("furniture", "glass"),
        ("curtains", "window"), ("blind", "window"), ("blinds", "window"), ("sign", "snow"), ("umbrella", "sand"), 
        ("sign", "grass"), ("bag", "can"),("curtain", "window"), ("air conditioner", "window"), ("leaves", "tree"), 
        ("water", "toilet"), ("sign", "window"), ("water", "ocean"), ("cloud", "clouds"), ("sheep", "sheep"), 
        ("airplane", "airplanes"), ("bag", "bags"), ("banana", "bananas"), ("knife", "knives"), ("glass", "glass"), 
        ("fruit", "fruit"), ("building", "buildings"), ("orange", "oranges"), ("car", "cars"), ("person", "people"), 
        ("chicken", "chickens"), ("boat", "boats"), ("mountain", "mountains"), ("elephant", "elephants"), 
        ("cabinet", "cabinets"), ("bread", "bread"), ("luggage", "luggage"), ("cup", "cups"), ("sand", "sand"), 
        ("peanut butter"), ("peanut butter"), ("hot dogs", "croissant"), ("zucchini", "meat"), ("pepper", "meat"), 
        ("bun", "sausage"), ("pepperoni", "pepperoni"), ("utensil", "meat"), ("orange", "meat"), ("hamburger", "meat"),
        ("background", "sky"), ("box", "sky"), ("bridge", "sky"), ("number", "sky"), ("propeller", "sky"), 
        ("seeds", "sky"), ("steam", "sky"), ("smoke", "sky"), ("crane", "sky"), ("leaf", "sky"), ("sign", "sky"), 
        ("cross", "sky"), ("wing", "sky"), ("mountains", "sky"), ("cables", "sky"), ("mountain", "sky"), 
        ("clock", "sky"), ("stick", "mud"), ("cap", "river"), ("sign", "shop"), ("bubbles", "ocean"), 
        ("bubble", "ocean"), ("bubbles", "sink"), ("bubbles", "river"), ("bubbles", "bathroom"), ("bubble", "pan"), 
        ("land", "ocean"), ("woman", "ladle"), ("lid", "pan"), ("price tag", "pan"), ("cake", "pans"), 
        ("pie", "pans"), ("pot", "pans"), ("basket", "pot"), ("bottle", "pot"), ("bowl", "pot"), ("brush", "pot"), 
        ("container", "pot"), ("mixer", "pot"), ("plates", "pot"), ("tool", "pot"), ("nut", "brownies"), 
        ("vanilla", "ice cream"), ("fruit", "cake"), ("glass", "dessert"), ("dip", "cake"), ("camera", "cake"), 
        ("candle", "cakes"), ("cookies", "cupcake"), ("cake", "cupcake"), ("cat", "cake"), ("dog", "cake"), 
        ("people", "cake"), ("cake slice", "cake"), ("woman", "cake"), ("cookies", "cupcakes"), ("beer", "drink"), 
        ("beer", "beverage"), ("liquid", "drink"), ("cream", "drink"), ("cappuccino", "coffee"), ("glass", "wine"), 
        ("wine", "drink"), ("cup", "coffee"), ("napkin", "coffee"), ("motorcycle", "bed"), ("wall", "bed"), 
        ("wall", "entertainment center"), ("cap", "bottle"), ("cup", "bottle"), ("milk", "cereal"), 
        ("candle", "chocolate"), ("mound", "food"), ("hot dog", "food"), ("drape", "window"), ("glass", "window"), 
        ("drapes", "window"), ("blind", "window"), ("blinds", "window"), ("curtain", "window"), 
        ("curtains", "window"), ("man", "cooker"), ("bowl", "stove"), ("clouds", "mountains"), 
        ("clock", "alarm clock"), ("man", "backpacks"), ("boy", "suitcase"), ("girl", "suitcase"), 
        ("workers", "bucket"), ("woman", "suitcase"), ("land", "water"), ("sail", "water"), 
        ("sign", "water"), ("deck", "water"), ("lighthouse", "water"), ("pillars", "water"), 
        ("beach", "water"), ("platform", "water"), ("stairs", "water"), ("stick", "water"), ("log", "water"), 
        ("trunk", "water"), ("post", "water"), ("bone", "water"), ("ocean", "water"), ("island", "water"), 
        ("mountain", "water"), ("waterfall", "water"), ("mud", "water"), ("stump", "water"), ("forest", "water"), 
        ("sticks", "water"), ("pole", "water"), ("ice", "water"), ("sidewalk", "street"),
        ("grass", "water"), ("weeds", "field"), ("grass", "forest"), ("plants", "water"), ("grass", "pond"), 
        ("plants", "forest"), ("plants", "yard"), ("grass", "backyard"), ("bush", "backyard"), ("grass", "basket"), 
        ("grass", "garden"), ("weeds", "snow"), ("bushes", "yard"), ("bush", "forest"), ("hay", "field"),
        ("pond", "field"), ("bleachers", "stadium"), ("pond", "park"), ("pond", "zoo"), ("house", "field"), 
        ("barn", "field"), ("clock tower", "park"), ("building", "forest"), ("container", "glass"), 
        ("trunks", "background"), ("coat", "snow"), ("clothes", "sand"), ("wetsuit", "ocean"), 
        ("blinds", "windows"), ("pizza", "background"), ("food", "shop"), ("food", "restaurant"), 
        ("sign", "background"), ("glass", "cabinet"), ("crane", "background"), ("bridge", "water"), 
        ("countertop", "kitchen"), ("stump", "sand"), ("outlet", "kitchen"), ("countertop", "bathroom"), 
        ("bowl", "bathroom"), ("crane", "water"), ("umbrella", "crowd"), ("vines", "field"), ("plants", "field"), 
        ("plant", "field"), ("weed", "field"), ("weeds", "forest"), ("plant", "forest"), ("bushes", "forest"), 
        ("weed", "garden"), ("weeds", "garden"), ("plant", "garden"), ("bush", "garden"), ("plants", "garden"), 
        ("plants", "lake"), ("grass", "lawn"), ("weeds", "mud"), ("grass", "mud"), ("grass", "ocean"), 
        ("weeds", "ocean"), ("flowers", "paper"), ("bush", "park"), ("grass", "park"), ("bushes", "park"), 
        ("bush", "parking lot"), ("plant", "plain"), ("grass", "plain"), ("bush", "pond"), ("plant", "pond"), 
        ("grass", "river"), ("plant", "river"), ("weeds", "river"), ("bush", "river"), ("grass", "sky"), 
        ("plants", "snow"), ("plant", "snow"), ("weeds", "steps"), ("bushes", "train"), ("bushes", "water"), 
        ("weed", "water"), ("bush", "water"), ("grass", "weeds"), ("flowers", "weeds"), ("weeds", "yard"), 
        ("plant", "zoo"), ("ski", "snow"), ("seat", "bleachers"), ("leaf", "water"),  
        ("seat", "bathroom"), ("seat", "boat"),  ("seat", "auditorium"), ("bubble", "water"), 
        ("log", "field"), ("fence", "yard"), ("ski", "water"), ("snow", "sky"), ("stick", "bathroom"), 
        ("leaves", "forest"), ("leaves", "field"), ("stick", "sand"), ("leaves", "pot"), 
        ("leaf", "bowl"), ("leaf", "pot"), ("leaf", "glass"), ("leaf", "pond"), ("leaves", "yard"), 
        ("lid", "bathroom"), ("sticks", "snow"), ("frosting", "cake"), ("leaf", "salad"), ("bubble", "coffee"), 
        ("seed", "field"), ("tree branch", "background"), ("leaf", "soup"), ("seed", "food"), 
        ("leaves", "park"), ("leaves", "snow"), ("leaves", "salad"), ("leaf", "park"), ("sticks", "field"), 
        ("leaves", "bowl"), ("grass", "water"), ("weeds", "field"), ("grass", "forest"), ("plants", "water"), 
        ("grass", "pond"), ("plants", "forest"), ("plants", "yard"), ("grass", "backyard"), ("bush", "backyard"), 
        ("grass", "basket"), ("grass", "garden"), ("weeds", "snow"), ("bushes", "yard"), ("bush", "forest"), 
        ("hay", "field"), ("flag", "sky"), ("tree", "sky"), ("tree", "water"), ("trees", "sky"), ("trees", "water"), 
        ("fence", "field"), ("leaf", "vase"), ("fence", "grass"), ("leaves", "water"), ("seat", "stadium"), 
        ("leaves", "vase"), ("fence", "park"), ("leaf", "snow"), ("stick", "snow"), ("seat", "bleachers"),
        ("seat", "stadium"), ("person", "boats"), ("microwave", "cabinets"), ("fruit", "baskets"), 
        ("toothbrush", "cups"), ("fruit", "boxes"), ("pepper", "mashed potatoes"), ("hot dog", "buns"), 
        ("spoon", "pots"), ("plant", "pots"), ("refrigerator", "cabinets"), ("sink", "cabinets"), 
        ("sheep", "cages"), ("potato", "pots"), ("tomato", "sandwiches"), ("oven", "cabinets"), 
        ("silverware", "plates"), ("trees", "houses"), ("lid", "dish"), ("lid", "cupboard"), 
        ("lid", "bag"), ("tree branch", "water"), ("tree branches", "sky"), ("bubbles", "bathtub"),
        ("seaweed", "sand"), ("stick", "weeds"), ("log", "weeds"), ("man", "glass"),  
        ("cat", "glass"), ("kitten", "glass"), ("tree", "glass"), ("clock", "glass"), ("trees", "glass"), 
        ("glass", "bathroom"), ("snow", "grass"), ("sign", "field"), ("stick", "field"), ("mirror", "car"), 
        ("mirror", "vehicle"), ("mirror", "park"), ("mirror", "window"), ("mirror", "train"), ("mirror", "minivan"),
        ("chair", "stadium"), ("lamb", "hay")]

    blacklistS = ["sky", "leaves", "leaf", "log", "pillars", "stick", "sticks", "bush", "bubble", "fence post", "post", "mound", "screen", "background", "ceiling", "pole", "wall", "garage door", "shower door", "cabinet doors", "cabinet door", "door", "doors", 
    "doorway", "doorways", "tiles", "air", "sky", "floor", "wave", "waves"]
    blacklistO = ["mirror", "window", "crowd", "cake", "tray", "sky", "beach", "cemetery", "city", "coast", "desert", "field", "garden", "dock", "harbor", "marina", "hill", "hills", "hillside", "hilltop", "lawn", "shore line", "parking lot", "mountain", "mountain peak", "plain", "shore", "mountain side", "stage", "street", "town", "village", "rooftop", "meadow", 
    "windows", "hill", "table", "mountain side", "wallpaper", "terrain", "wave", "waves", "rain", "mountains", "land", "town", "shore", "mountain", "hills", "hillside", "hilltop", "entrance", "dock", "display", "city", "room", "flower", "flowers", "bush", "motorcycle", "bike", "candy", "cheese", "chips", "chocolate", "cream cheese", "cream", "dip", "egg", "eggs", 
    "mozzarella", "parmesan cheese", "carpet" ,"ceiling" ,"roof" ,"staircase" ,"stairs" ,"walls", "cutting board", 
    "picnic table", "furniture", "armchair", "desk", "shelf", "shelves", "buildings",  "apartment", 
    "utensil", "wig", "door", "doors", "glasses", "tower", "tree", "trees", "wall", "floor", 
     "herd", "ground", "cap", "post", "fence post", "sign post"] 
    blacklistScat = ["place", "nature environment", "urban environment", "meal", "road", "vehicle part", "part", "room", "label", "body part"]
    blacklistOcat = ["road", "office supplies", "animal", "person", "sauce", "textile", "fast food", "device", 
    "meal", "part", "footwear", "vehicle part", "label", "ingredient", "accessory", "clothing", "body part", "utensil"]
    chairs = ["office chair", "chairs", "couch", "couches", "sofa", "bench", "chair"]
    waterWhitelsit = ["mug", "glass", "vase", "bowl", "bottle", "cup", "jar", "fountain", "sink", "bathtub", "bucket", "container", 
        "glasses", "bottles", "flower pot", "basket", "aquarium"] 
    natural = ["sand", "rock", "rocks", "boulders", "water", "mud", "ice", "stone", "stones", "leaf", "leaves", 
        "tree leaves", "petal", "petals", "branch", "branches", "tree branch", "tree branches", "twig", 
        "twigs", "stick", "sticks", "log", "logs", "stump"]
    naturalR = ["branch", "branches", "twig", "twigs", "stone", "stones", "rock", "rocks", "tile", "hair", "skin", "fur", "wool", "feathers"]
    extraParts = ["door frame", "doorway", "window frame", "touchpad", "horse hoof", "strap", "straps", "hair", "skin", "fur", "wool", "feathers", "seat belt", "cockpit"]
    inclusiveObjs = ["lamp", "stroller", "pot", "planter", "mirror", "backpack", "bag", "basket", "baskets", "bird cage", "bowl", "briefcase", "bucket", "can", 
        "candle holder", "cart", "crate", "crates", "dish drainer", "dispenser", "dumpster", "flower pot", "grinder", 
        "knife block", "napkin dispenser", "package", "pouch", "salt shaker", "suitcase", "tissue box", "towel dispenser", 
        "tray", "utensil holder", "vase", "vending machine", "wallet", "waste basket", "wheelchair"] 
    # airWhitelist = ["phone", "pigeon", "aircraft", "dog", "guy", "airplane", "jet", "man", "apple", "snowboards", 
    # "frisbee", "snowboard", "snowboarder", "bike", "birds", "skateboarder", "kite", "skier", "kites", "boy", "ball", 
    # "horse", "people", "surfer", "woman", "helicopter", "shoe", "skis", "person", "balloon", "motorcycle", "player", 
    # "bird", "baseball", "airplanes", "skateboard"]
    noneWhitelist = ["net", "pen", "aquarium", "audience", "bathtub", "cockpit", "cooler", "crowd", "doorway", "fireplace", "fountain", 
        "glass", "pitcher", "pocket", "pockets", "shower", "sink"]
    thingWhitelist = ["fence", "cages", "cage", "ice", "nest", "painting", "napkin", "paper", "sand", "snow", "tent", "water"]

    for w in whitelist:
        if s == w[0] and o == w[1]:
            return False
    for b in blacklist:
        if s == b[0] and o == b[1]:
            return True
    if s in blacklistS or catn(s) in blacklistScat:
        return True
    if o in blacklistO or catn(o) in blacklistOcat and o not in ["shoe"]:
        return True
    # if o in ["mirror", "window"]:
    #   return False
    if s in ["window", "windows"]: # and o not in ["bathroom", "kitchen", "bedroom", "living room"]:
        return True
    if o in chairs:
        return True
    if s == "water" and o not in waterWhitelsit:
        return True
    if (catn(s) in ["plant", "tree"] or s in natural) and o in ["grass", "bushes"]:
        return True
    if s in naturalR or o in naturalR:
        return True
    if catn(o) == "symbol" and o not in ["drawing", "drawings"]:
        return True
    if catn(s) == "symbol" and s not in ["drawing", "drawings"]:
        return True     
    if catn(o) == "plant" and o not in ["grass", "bushes", "hay", "weeds"]:
        return True     
    if catn(o) in ["vegetable", "fruit"] and s not in ["seed", "seeds"]:
        return True 
    if catn(o) == "aircraft" and catn(s) != "person":
        return True
    if s in extraParts:
        return True
    if catn(o) == "object" and o not in inclusiveObjs:
        return True
    if catn(o) == "" and o not in noneWhitelist:
        return True 
    if catn(o) == "thing" and o not in thingWhitelist:
        return True             
    # if o == "air" and s not in airWhitelist:
    #     return True
    if catn(s) == "building" and o != "background":
        return True
    return False

    # if not isPlural(s) and pluralOf(s) == o:
    #   return True
    # if  isPlural(s) and isPlural(o):
    #   return False
    #  singular/plural bubble
    #   body part as subject
    #snow (covered in), without the?
    # in glass 
    # _field

def filterWith(s, o):
    whitelist = [("man", "beard"), ("man", "hat"), ("man", "glasses"), ("plate", "food"), ("vase", "flowers"), 
    ("man", "backpack"), ("woman", "umbrella"), ("donut", "sprinkles"), ("glass", "wine"), ("woman", "bag"), 
    ("man", "jacket"), ("man", "racket"), ("man", "camera"), ("man", "surfboard"), ("bottle", "label"), 
    ("man", "sunglasses"), ("man", "bag"), ("pizza", "cheese"), ("man", "umbrella"), ("man", "cap"), 
    ("tower", "clock"), ("building", "clock"), ("donut", "frosting"), ("man", "frisbee"), ("woman", "glasses"), 
    ("dog", "frisbee"), ("man", "tie"), ("man", "dog"), ("vase", "flower"), ("window", "blinds"), 
    ("man", "mustache"), ("person", "umbrella"), ("kite", "tail"), ("man", "skateboard"), ("man", "helmet"), 
    ("glass", "water"), ("woman", "purse"), ("woman", "sunglasses"), ("cake", "frosting"), ("man", "jeans"), 
    ("man", "shorts"), ("boy", "skateboard"), ("person", "jacket"), ("woman", "dog"), ("table", "food"), 
    ("pizza", "pepperoni"), ("woman", "racket"), ("man", "coat"), ("dog", "collar"), ("hot dog", "mustard"), 
    ("window", "curtains"), ("bowl", "food"), ("plate", "pizza"), ("man", "eyeglasses"), ("man", "snowboard"), 
    ("man", "luggage"), ("boy", "frisbee"), ("player", "bat"), ("man", "phone"), ("person", "helmet"), 
    ("bush", "flowers"), ("woman", "hat"), ("hot dog", "ketchup"), ("man", "kite"), ("man", "laptop"), 
    ("girl", "umbrella"), ("window", "curtain"), ("couch", "pillow"), ("person", "backpack"), ("cake", "icing"), 
    ("person", "surfboard"), ("donut", "icing"), ("woman", "scarf"), ("person", "hat"), ("man", "horse"), 
    ("boy", "bat"), ("plate", "sandwich"), ("people", "umbrellas"), ("bed", "pillow"), ("man", "skis"), 
    ("man", "bat"), ("woman", "phone"), ("woman", "jacket"), ("girl", "glasses"), ("person", "bag"), 
    ("plate", "cake"), ("soda", "ice"), ("girl", "racket"), ("glass", "beer"), ("pizza", "sauce"), 
    ("table", "tablecloth"), ("player", "racket"), ("couch", "pillows"), ("suitcase", "tag"), 
    ("surfer", "surfboard"), ("shirt", "collar"), ("woman", "camera"), ("boy", "shorts"), ("sandwich", "meat"), 
    ("woman", "eyeglasses"), ("woman", "child"), ("woman", "coat"), ("person", "kite"), ("plant", "flowers"), 
    ("man", "bike"), ("man", "suit"), ("tree", "flowers"), ("girl", "phone"), ("shelf", "books"), ("tray", "food"), 
    ("man", "glove"), ("boy", "hat"), ("pole", "flag"), ("man", "controller"), ("woman", "dress"), 
    ("girl", "helmet"), ("person", "coat"), ("person", "dog"), ("chair", "pillow"), ("guy", "beard"), 
    ("bowl", "soup"), ("bowl", "sauce"), ("man", "ball"), ("man", "boy"), ("man", "elephant"), ("boy", "racket"), 
    ("boy", "cap"), ("lady", "eyeglasses"), ("lady", "umbrella"), ("cake", "candle"), ("box", "donut"), 
    ("girl", "bag"), ("glass", "juice"), ("player", "glove"), ("sandwich", "lettuce"), ("cupcake", "icing"), 
    ("man", "stick"), ("woman", "baby"), ("woman", "backpack"), ("building", "balcony"), ("girl", "jacket"), 
    ("girl", "hat"), ("person", "glasses"), ("person", "camera"), ("lady", "bag"), ("pizza", "olives"), 
    ("cake", "sprinkles"), ("flower", "leaves"), ("man", "cat"), ("woman", "suitcase"), ("girl", "headband"), 
    ("pizza", "basil"), ("pizza", "vegetables"), ("bowl", "broccoli"), ("animal", "horn"), ("woman", "luggage"), 
    ("plate", "donut"), ("bowl", "spoon"), ("bike", "basket"), ("hill", "trees"), ("man", "scarf"), 
    ("man", "goggles"), ("man", "suitcase"), ("man", "vest"), ("girl", "sunglasses"), ("boy", "helmet"), 
    ("person", "laptop"), ("donut", "chocolate"), ("glass", "beverage"), ("dog", "toy"), ("mountain", "trees"), 
    ("man", "mask"), ("man", "gloves"), ("man", "motorcycle"), ("woman", "boy"), ("boy", "ball"), 
    ("plate", "bread"), ("donut", "glaze"), ("glass", "ice"), ("window", "blind"), ("cup", "handle"), 
    ("sandwich", "cheese"), ("cow", "tag"), ("sofa", "pillow"), ("camera", "strap"), ("bun", "hot dog"), 
    ("man", "watch"), ("person", "skateboard"), ("plate", "salad"), ("pizza", "mushrooms"), ("pizza", "ham"), 
    ("table", "laptop"), ("cake", "candles"), ("cat", "collar"), ("shelf", "animals"), ("boat", "people"), 
    ("cupcake", "frosting"), ("donuts", "sprinkles"), ("man", "child"), ("man", "cell phone"), 
    ("woman", "surfboard"), ("boy", "glasses"), ("boy", "backpack"), ("plate", "hot dog"), ("plate", "fries"), 
    ("lady", "purse"), ("pizza", "onion"), ("guy", "hat"), ("container", "food"), ("bowl", "fruit"), 
    ("cabinet", "drawer"), ("man", "sweater"), ("man", "socks"), ("woman", "sweater"), ("woman", "helmet"), 
    ("woman", "necklace"), ("girl", "purse"), ("pole", "clock"), ("person", "shorts"), ("person", "goggles"), 
    ("person", "horse"), ("plate", "fruit"), ("pot", "flowers"), ("donut", "candies"), ("pizza", "onions"), 
    ("pizza", "peppers"), ("table", "lamp"), ("table", "bowl"), ("player", "helmet"), ("field", "sheep"), 
    ("tray", "donut"), ("meat", "broccoli"), ("man", "bird"), ("man", "fork"), ("man", "bandana"), 
    ("man", "guitar"), ("man", "knife"), ("man", "wetsuit"), ("woman", "vest"), ("woman", "frisbee"), 
    ("woman", "cell phone"), ("building", "dome"), ("girl", "kite"), ("boy", "dog"), ("pole", "bird"), 
    ("person", "cap"), ("person", "bike"), ("person", "racket"), ("plate", "broccoli"), ("lady", "jacket"), 
    ("lady", "glasses"), ("bottle", "flower"), ("house", "chimney"), ("chair", "wheels"), ("table", "drawer"), 
    ("guy", "surfboard"), ("hot dog", "cheese"), ("field", "zebra"), ("bed", "headboard"), ("boat", "person"), 
    ("animal", "horns"), ("donuts", "frosting"), ("man", "donut"), ("man", "ring"), ("man", "microphone"), 
    ("woman", "handbag"), ("boy", "sunglasses"), ("boy", "eyeglasses"), ("person", "sweater"), ("plate", "dessert"), 
    ("plate", "waffle"), ("plate", "meat"), ("pizza", "tomatoes"), ("dog", "scarf"), ("table", "cake"), 
    ("guy", "backpack"), ("guy", "glasses"), ("horse", "carriage"), ("cake", "decoration"), ("cup", "beverage"), 
    ("field", "rocks"), ("field", "cows"), ("cabinet", "doors"), ("bear", "hat"), ("tray", "vegetables"), 
    ("box", "pizza"), ("box", "label"), ("hat", "flower"), ("basket", "bread"), ("man", "apron"), ("man", "banana"), 
    ("man", "glass"), ("man", "cup"), ("woman", "glass"), ("woman", "boots"), ("woman", "banana"), ("woman", "horse"), 
    ("woman", "cow"), ("tree", "ornament"), ("building", "chimney"), ("girl", "coat"), ("girl", "scarf"), 
    ("boy", "phone"), ("person", "sunglasses"), ("person", "skis"), ("plate", "donuts"), ("plate", "vegetables"), 
    ("pot", "flower"), ("vase", "water"), ("donut", "sugar"), ("pizza", "meat"), ("pizza", "broccoli"), 
    ("tower", "window"), ("child", "bat"), ("chair", "towel"), ("bowl", "water"), ("bowl", "salad"), 
    ("bowl", "apple"), ("bowl", "liquid"), ("player", "cap"), ("cup", "pens"), ("cup", "water"), 
    ("cup", "toothbrush"), ("bed", "pillows"), ("shirt", "pocket"), ("sandwich", "onion"), ("pillow", "flower"), 
    ("tablecloth", "flower"), ("shelves", "books"), ("chicken", "sauce"), ("man", "sandwich"), ("man", "boots"), 
    ("man", "sheep"), ("man", "headband"), ("woman", "sheep"), ("woman", "blanket"), ("woman", "parrot"), 
    ("woman", "bracelet"), ("woman", "apron"), ("girl", "sweater"), ("girl", "cat"), ("girl", "flower"), 
    ("girl", "frisbee"), ("girl", "dress"), ("girl", "necklace"), ("boy", "jacket"), ("person", "jeans"), 
    ("person", "motorcycle"), ("plate", "pastry"), ("plate", "eggs"), ("plate", "meal"), ("plate", "sauce"), 
    ("plate", "banana"), ("lady", "dog"), ("lady", "coat"), ("lady", "bottle"), ("lady", "hat"), 
    ("pizza", "spinach"), ("tower", "windows"), ("child", "helmet"), ("dog", "ball"), ("table", "book"), 
    ("guy", "luggage"), ("guy", "jacket"), ("container", "utensils"), ("cake", "flower"), ("cake", "animals"), 
    ("hot dog", "onions"), ("bowl", "pasta"), ("fence", "flag"), ("player", "headband"), ("bear", "heart"), 
    ("sandwich", "tomato"), ("jar", "flower"), ("box", "vegetable"), ("box", "lid"), ("box", "vegetables"), 
    ("cupcake", "sprinkles"), ("bench", "snow"), ("car", "snow"), ("cart", "hay"), ("meat", "sauce"), 
    ("truck", "ladder"), ("jacket", "zipper"), ("bread", "bacon"), ("bread", "meat"), ("policeman", "helmet"), 
    ("man", "uniform"), ("man", "paddle"), ("man", "rope"), ("man", "computer"), ("man", "cow"), 
    ("man", "bottle"), ("woman", "kite"), ("woman", "raincoat"), ("woman", "cat"), ("woman", "shorts"), 
    ("woman", "cap"), ("tree", "decorations"), ("girl", "bracelets"), ("girl", "cell phone"), ("girl", "skirt"), 
    ("girl", "shorts"), ("girl", "backpack"), ("girl", "glove"), ("girl", "bandana"), ("girl", "jeans"), 
    ("girl", "cup"), ("boy", "glove"), ("boy", "beer"), ("boy", "jeans"), ("person", "gloves"), 
    ("plate", "potato"), ("plate", "star"), ("plate", "crumbs"), ("pot", "vegetables"), ("lady", "horse"), 
    ("lady", "sunglasses"), ("lady", "cap"), ("pizza", "pineapple"), ("pizza", "sausage"), ("pizza", "pepper"), 
    ("dog", "stick"), ("door", "mirror"), ("window", "flowers"), ("window", "balcony"), ("guy", "dog"), 
    ("guy", "eyeglasses"), ("guy", "camera"), ("guy", "earring"), ("container", "meal"), ("elephant", "chain"), 
    ("cat", "tag"), ("bowl", "blueberry"), ("fence", "gate"), ("player", "ball"), ("player", "shorts"), 
    ("field", "giraffes"), ("field", "trees"), ("suitcase", "strap"), ("bear", "tag"), ("bear", "shirt"), 
    ("sandwich", "vegetables"), ("shelf", "napkins"), ("shelf", "donut"), ("boat", "roof"), ("box", "donuts"), 
    ("cupcake", "heart"), ("bag", "straps"), ("luggage", "tag"), ("animal", "fur"), ("animal", "mane"), 
    ("pan", "pizza"), ("basket", "biscuit"), ("basket", "flowers"), ("pillow", "flowers"), ("necklace", "flower"), 
    ("backpack", "star"), ("cone", "ice cream"), ("balcony", "fence"), ("curtain", "flowers"), ("roof", "chimney"), 
    ("wallpaper", "flower"), ("mother", "child"), ("mother", "baby"), ("dress", "flowers"), ("bandana", "star"), 
    ("bagel", "blueberry"), ("salad", "dressing"), ("passenger", "backpack"), ("pasta", "sauce"), ("man", "cigar"), 
    ("man", "football"), ("man", "cane"), ("man", "briefcase"), ("man", "cigarette"), ("man", "headphones"), 
    ("man", "toothbrush"), ("man", "book"), ("woman", "controller"), ("woman", "ball"), ("woman", "bike"), 
    ("woman", "gloves"), ("woman", "jeans"), ("woman", "headband"), ("tree", "ornaments"), ("building", "antenna"), 
    ("girl", "goggles"), ("girl", "scissors"), ("girl", "gloves"), ("girl", "surfboard"), ("girl", "dog"), 
    ("boy", "bag"), ("boy", "toothbrush"), ("boy", "kite"), ("boy", "coat"), ("boy", "umbrella"), 
    ("boy", "surfboard"), ("boy", "controller"), ("person", "vest"), ("person", "tie"), ("person", "frisbee"), 
    ("person", "mask"), ("person", "purse"), ("person", "dress"), ("person", "flag"), ("person", "boots"), 
    ("person", "phone"), ("person", "watch"), ("person", "luggage"), ("plate", "potatoes"), ("plate", "flower"), 
    ("plate", "chicken"), ("donut", "powder"), ("donut", "coconut"), ("glass", "ice cubes"), ("glass", "candle"), 
    ("lady", "backpack"), ("lady", "scarf"), ("lady", "jeans"), ("pizza", "herbs"), ("pizza", "bacon"), 
    ("tower", "clocks"), ("child", "coat"), ("child", "umbrella"), ("dog", "shoe"), ("door", "curtain"), 
    ("window", "drapes"), ("window", "bell"), ("table", "bottles"), ("table", "vegetables"), ("guy", "watch"), 
    ("guy", "cap"), ("guy", "bag"), ("guy", "skateboard"), ("container", "salad"), ("container", "hot dog"), 
    ("cake", "strawberries"), ("hot dog", "onion"), ("hot dog", "chili"), ("bowl", "shrimp"), ("bowl", "bread"), 
    ("bowl", "cheese"), ("bowl", "fruits"), ("bowl", "vegetables"), ("bowl", "beans"), ("bowl", "strawberry"), 
    ("bowl", "strawberries"), ("player", "hat"), ("water", "lemon"), ("bed", "dog"), ("bed", "backpack"), 
    ("bear", "tie"), ("bear", "cap"), ("sandwich", "ham"), ("sandwich", "sauce"), ("baby", "toothbrush"), 
    ("tray", "pizza"), ("box", "cake"), ("cupcake", "toppings"), ("dish", "broccoli"), ("hill", "bushes"), 
    ("cart", "luggage"), ("sofa", "pillows"), ("bun", "lettuce"), ("donuts", "icing"), ("pan", "food"), 
    ("pan", "lid"), ("hat", "flowers"), ("basket", "bananas"), ("basket", "fruit"), ("basket", "lid"), 
    ("jeans", "pocket"), ("chicken", "broccoli"), ("pasta", "cheese"), ("waffle", "butter"), ("flag", "star"), 
    ("pancakes", "syrup"), ("pastry", "blueberry"), ("cupcakes", "frosting"), ("pots", "flowers"), 
    ("tea", "spoon"), ("monkey", "banana"), ("man", "pen"), ("man", "cart"), ("man", "name tag"), ("woman", "flower")]
    for (s,o) in whitelist:
            return False
    return True

def filterHas(s, o):
    whitelist = [("door", "window"), ("wall", "window"), ("bear", "shirt"), ("animal", "shirt"), ("alien", "shirt"), 
        ("door", "windows"), ("wall", "windows"), ("man", "beard"), ("guy", "beard"), ("person", "beard"), 
        ("player", "beard"), ("boy", "beard"), ("father", "beard"), ("man", "hat"), ("person", "hat"), ("woman", "hat"), 
        ("boy", "hat"), ("girl", "hat"), ("bear", "hat"), ("child", "hat"), ("player", "hat"), ("dog", "hat"), 
        ("people", "hat"), ("cat", "hat"), ("spectator", "hat"), ("guy", "hat"), ("statue", "hat"), ("skateboarder", "hat"), 
        ("lady", "hat"), ("baby", "hat"), ("toy", "hat"), ("cowboy", "hat"), ("man", "glasses"), ("woman", "glasses"), 
        ("person", "glasses"), ("girl", "glasses"), ("lady", "glasses"), ("boy", "glasses"), ("child", "glasses"), 
        ("guy", "glasses"), ("dog", "glasses"), ("bear", "glasses"), ("statue", "glasses"), ("chair", "wheels"), 
        ("bag", "wheels"), ("table", "wheels"), ("horse", "wheels"), ("bear", "shoe"), ("cat", "shoe"), 
        ("shirt", "collar"), ("dog", "collar"), ("cat", "collar"), ("cow", "collar"), ("sheep", "collar"), 
        ("elephant", "collar"), ("poodle", "collar"), ("lamb", "collar"), ("horse", "collar"), ("man", "jacket"), 
        ("person", "jacket"), ("woman", "jacket"), ("girl", "jacket"), ("boy", "jacket"), ("child", "jacket"), 
        ("guy", "jacket"), ("lady", "jacket"), ("women", "jacket"), ("bear", "jacket"), ("tower", "clock"), 
        ("building", "clock"), ("pole", "clock"), ("man", "clock"), ("cup", "lid"), ("box", "lid"), ("bowl", "lid"), 
        ("sign", "arrow"), ("man", "shorts"), ("boy", "shorts"), ("person", "shorts"), ("woman", "shorts"), 
        ("girl", "shorts"), ("player", "shorts"), ("child", "shorts"), ("guy", "shorts"), ("skateboarder", "shorts"), 
        ("lady", "shorts"), ("skater", "shorts"), ("man", "helmet"), ("player", "helmet"), ("person", "helmet"), 
        ("boy", "helmet"), ("woman", "helmet"), ("child", "helmet"), ("girl", "helmet"), ("policeman", "helmet"), 
        ("biker", "helmet"), ("guy", "helmet"), ("skater", "helmet"), ("lady", "helmet"), ("sign", "number"), 
        ("pizza", "cheese"), ("hot dog", "cheese"), ("sandwich", "cheese"), ("plate", "cheese"), ("food", "cheese"), 
        ("bread", "cheese"), ("bowl", "cheese"), ("fries", "cheese"), ("man", "mustache"), ("guy", "mustache"), 
        ("plate", "food"), ("bowl", "food"), ("table", "food"), ("tray", "food"), ("container", "food"), ("jar", "food"), 
        ("pot", "food"), ("basket", "food"), ("box", "food"), ("pan", "food"), ("skillet", "food"), 
        ("hill", "grass"), ("mountain", "grass"), ("pole", "sign"), ("building", "sign"), ("window", "sign"), 
        ("door", "sign"), ("fence", "sign"), ("glass", "wine"), ("bottle", "wine"), ("cup", "wine"), ("shelf", "wine"), 
        ("man", "tie"), ("bear", "tie"), ("person", "tie"), ("boy", "tie"), ("guy", "tie"), ("girl", "tie"), 
        ("man", "cap"), ("boy", "cap"), ("person", "cap"), ("player", "cap"), ("woman", "cap"), ("skier", "cap"), 
        ("girl", "cap"), ("guy", "cap"), ("child", "cap"), ("man", "sunglasses"), ("woman", "sunglasses"), 
        ("person", "sunglasses"), ("lady", "sunglasses"), ("girl", "sunglasses"), ("guy", "sunglasses"), 
        ("dog", "sunglasses"), ("skater", "sunglasses"), ("building", "balcony"), ("house", "balcony"), 
        ("window", "balcony"), ("man", "backpack"), ("person", "backpack"), ("woman", "backpack"), ("boy", "backpack"), 
        ("skier", "backpack"), ("girl", "backpack"), ("lady", "backpack"), ("child", "backpack"), ("guy", "backpack"), 
        ("man", "watch"), ("woman", "watch"), ("person", "watch"), ("boy", "watch"), ("lady", "watch"), ("girl", "watch"), 
        ("bottle", "label"), ("wine", "label"), ("jar", "label"), ("man", "jeans"), ("boy", "jeans"), ("person", "jeans"), 
        ("woman", "jeans"), ("girl", "jeans"), ("lady", "jeans"), ("child", "jeans"), ("skateboarder", "jeans"), 
        ("guy", "jeans"), ("skater", "jeans"), ("bear", "jeans"), ("pizza", "pepperoni"), ("woman", "bag"), ("man", "bag"), 
        ("person", "bag"), ("girl", "bag"), ("lady", "bag"), ("guy", "bag"), ("boy", "bag"), ("woman", "purse"), 
        ("girl", "purse"), ("person", "purse"), ("lady", "purse"), ("man", "glove"), ("player", "glove"), 
        ("person", "glove"), ("boy", "glove"), ("woman", "glove"), ("girl", "glove"), ("child", "glove"), 
        ("guy", "glove"), ("man", "coat"), ("woman", "coat"), ("person", "coat"), ("girl", "coat"), ("lady", "coat"), 
        ("boy", "coat"), ("child", "coat"), ("bear", "coat"), ("snowboarder", "coat"), ("donut", "sprinkles"), 
        ("cupcake", "sprinkles"), ("donuts", "sprinkles"), ("vase", "flowers"), ("tree", "flowers"), 
        ("bush", "flowers"), ("plant", "flowers"), ("cake", "flowers"), ("umbrella", "flowers"), ("shirt", "flowers"), 
        ("pot", "flowers"), ("bushes", "flowers"), ("dress", "flowers"), ("plate", "flowers"), ("basket", "flowers"), 
        ("table", "flowers"), ("field", "flowers"), ("bed", "flowers"), ("pillow", "flowers"), ("box", "flowers"), 
        ("hat", "flowers"), ("person", "flowers"), ("comforter", "flowers"), ("cup", "flowers"), ("rug", "flowers"), 
        ("curtains", "flowers"), ("tablecloth", "flowers"), ("blanket", "flowers"), ("sign", "numbers"), 
        ("shirt", "numbers"), ("window", "curtain"), ("door", "curtain"), ("donut", "frosting"), ("cake", "frosting"), 
        ("cupcake", "frosting"), ("donuts", "frosting"), ("cupcakes", "frosting"), ("brownies", "frosting"), 
        ("man", "surfboard"), ("person", "surfboard"), ("woman", "surfboard"), ("girl", "surfboard"), 
        ("boy", "surfboard"), ("man", "camera"), ("woman", "camera"), ("person", "camera"), ("guy", "camera"), 
        ("girl", "camera"), ("pizza", "sauce"), ("bowl", "sauce"), ("container", "sauce"), ("bottle", "sauce"), 
        ("food", "sauce"), ("meat", "sauce"), ("chicken", "sauce"), ("sandwich", "sauce"), ("plate", "sauce"), 
        ("steak", "sauce"), ("pasta", "sauce"), ("bread", "sauce"), ("hot dog", "sauce"), ("rice", "sauce"), 
        ("broccoli", "sauce"), ("wall", "mirror"), ("door", "mirror"), ("mountain", "snow"), ("tree", "snow"), 
        ("mountains", "snow"), ("hill", "snow"), ("trees", "snow"), ("roof", "snow"), ("hills", "snow"), 
        ("bench", "snow"), ("woman", "necklace"), ("man", "necklace"), ("girl", "necklace"), ("lady", "necklace"), 
        ("child", "necklace"), ("shirt", "pocket"), ("jacket", "pocket"), ("pants", "pocket"), ("jeans", "pocket"), 
        ("coat", "pocket"), ("woman", "umbrella"), ("man", "umbrella"), ("person", "umbrella"), ("lady", "umbrella"), 
        ("girl", "umbrella"), ("child", "umbrella"), ("bed", "headboard"), ("window", "curtains"), ("vase", "flower"), 
        ("cake", "flower"), ("shirt", "flower"), ("plate", "flower"), ("pot", "flower"), ("painting", "flower"), 
        ("glass", "flower"), ("hat", "flower"), ("girl", "flower"), ("player", "bat"), ("man", "bat"), 
        ("boy", "bat"), ("girl", "bat"), ("person", "bat"), ("child", "bat"), ("bed", "pillow"), ("couch", "pillow"), 
        ("chair", "pillow"), ("sofa", "pillow"), ("glass", "water"), ("bottle", "water"), ("vase", "water"), 
        ("cup", "water"), ("bowl", "water"), ("pitcher", "water"), ("container", "water"), ("bucket", "water"), 
        ("dog", "frisbee"), ("man", "frisbee"), ("boy", "frisbee"), ("woman", "frisbee"), ("person", "frisbee"), 
        ("girl", "frisbee"), ("guy", "frisbee"), ("building", "chimney"), ("house", "chimney"), ("roof", "chimney"), 
        ("cabin", "chimney"), ("window", "blinds"), ("door", "blinds"), ("man", "phone"), ("woman", "phone"), 
        ("girl", "phone"), ("boy", "phone"), ("person", "phone"), ("lady", "phone"), ("sign", "words"), 
        ("shirt", "words"), ("woman", "ring"), ("man", "ring"), ("person", "ring"), ("lady", "ring"), 
        ("guy", "ring"), ("girl", "ring"), ("ear", "tag"), ("cow", "tag"), ("suitcase", "tag"), ("sheep", "tag"), 
        ("dog", "tag"), ("bear", "tag"), ("cat", "tag"), ("shirt", "tag"), ("basket", "tag"), ("animal", "tag"), 
        ("man", "goggles"), ("person", "goggles"), ("woman", "goggles"), ("boy", "goggles"), ("girl", "goggles"), 
        ("hot dog", "mustard"), ("sandwich", "mustard"), ("bottle", "mustard"), ("bun", "mustard"), 
        ("cupcake", "topping"), ("donut", "topping"), ("container", "liquid"), ("man", "suit"), ("person", "suit"), 
        ("cake", "candle"), ("cabinet", "drawer"), ("desk", "drawer"), ("table", "drawer"), ("bike", "basket"), 
        ("hot dog", "ketchup"), ("container", "ketchup"), ("bottle", "ketchup"), ("man", "skis"), 
        ("person", "skis"), ("woman", "skis"), ("boy", "skis"), ("child", "skis"), ("woman", "scarf"), 
        ("man", "scarf"), ("bear", "scarf"), ("person", "scarf"), ("girl", "scarf"), ("lady", "scarf"), 
        ("dinosaur", "scarf"), ("penguin", "scarf"), ("woman", "bracelet"), ("man", "bracelet"), 
        ("person", "bracelet"), ("girl", "bracelet"), ("lady", "bracelet"), ("boy", "bracelet"), 
        ("woman", "earring"), ("man", "earring"), ("girl", "earring"), ("lady", "earring"), ("person", "earring"), 
        ("child", "earring"), ("woman", "dress"), ("girl", "dress"), ("bear", "dress"), ("person", "dress"), 
        ("doll", "dress"), ("lady", "dress"), ("child", "dress"), ("pole", "flag"), ("building", "flag"), 
        ("boat", "flag"), ("train", "flag"), ("scooter", "flag"), ("tower", "flag"), ("motorcycle", "flag"), 
        ("man", "wetsuit"), ("woman", "wetsuit"), ("boy", "wetsuit"), ("person", "wetsuit"), ("guy", "wetsuit"), 
        ("girl", "wetsuit"), ("sandwich", "tomato"), ("man", "gloves"), ("person", "gloves"), ("player", "gloves"), 
        ("child", "gloves"), ("woman", "gloves"), ("girl", "gloves"), ("man", "sweater"), ("woman", "sweater"), 
        ("girl", "sweater"), ("person", "sweater"), ("lady", "sweater"), ("boy", "sweater"), ("child", "sweater"), 
        ("cake", "icing"), ("donut", "icing"), ("cupcake", "icing"), ("dessert", "icing"), ("sandwich", "meat"), 
        ("pizza", "meat"), ("plate", "meat"), ("bread", "meat"), ("dish", "meat"), ("bowl", "meat"), ("bun", "meat"), 
        ("bowl", "fruit"), ("tree", "fruit"), ("basket", "fruit"), ("cake", "fruit"), ("plate", "fruit"), 
        ("box", "fruit"), ("man", "skateboard"), ("boy", "skateboard"), ("person", "skateboard"), 
        ("woman", "skateboard"), ("guy", "skateboard"), ("glass", "juice"), ("bottle", "juice"), 
        ("cup", "juice"), ("pitcher", "juice"), ("pizza", "spinach"), ("mug", "coffee"), ("man", "snowboard"), 
        ("person", "snowboard"), ("child", "snowboard"), ("woman", "snowboard"), ("plate", "pizza"), ("box", "pizza"), 
        ("table", "pizza"), ("pan", "pizza"), ("man", "mask"), ("person", "mask"), ("horse", "mask"), ("bear", "mask"), 
        ("animal", "mask"), ("teddy bear", "mask"), ("man", "knife"), ("woman", "knife"), ("person", "knife"), 
        ("table", "tablecloth"), ("man", "wristband"), ("player", "wristband"), ("woman", "wristband"), 
        ("glass", "beer"), ("mug", "beer"), ("man", "beer"), ("cup", "beer"), ("bottle", "beer"), ("man", "boots"), 
        ("woman", "boots"), ("girl", "boots"), ("person", "boots"), ("lady", "boots"), ("cowboy", "boots"), 
        ("boy", "boots"), ("man", "eyeglasses"), ("woman", "eyeglasses"), ("person", "eyeglasses"), 
        ("lady", "eyeglasses"), ("girl", "eyeglasses"), ("boy", "eyeglasses"), ("door", "lock"), ("cabinet", "lock"), 
        ("suitcase", "lock"), ("gate", "lock"), ("man", "uniform"), ("lady", "uniform"), ("boy", "uniform"),
        ("woman", "uniform"), ("person", "uniform"), ("woman", "cell phone"), ("man", "cell phone"), 
        ("person", "cell phone"), ("boy", "cell phone"), ("donut", "chocolate"), ("bread", "chocolate"), 
        ("man", "kite"), ("woman", "kite"), ("girl", "kite"), ("person", "kite"), ("child", "kite"), 
        ("boy", "kite"), ("guy", "kite"), ("mountain", "trees"), ("hill", "trees"), ("field", "trees"), 
        ("pizza", "olives"), ("sandwich", "lettuce"), ("salad", "lettuce"), ("pizza", "lettuce"), 
        ("shelf", "books"), ("table", "books"), ("necklace", "stone"), ("bed", "blanket"), ("horse", "blanket"), 
        ("building", "dome"), ("tower", "dome"), ("man", "laptop"), ("woman", "laptop"), ("person", "laptop"), 
        ("girl", "laptop"), ("boy", "laptop"), ("pizza", "pepper"), ("wall", "painting"), ("pizza", "peppers"), 
        ("hot dog", "peppers"), ("woman", "skirt"), ("person", "skirt"), ("girl", "skirt"), ("player", "skirt"), 
        ("alien", "skirt"), ("fence", "gate"), ("pizza", "mushrooms"), ("shoe", "heel"), ("boot", "heel"), 
        ("woman", "handbag"), ("person", "handbag"), ("girl", "handbag"), ("cake", "candles"), ("bed", "pillows"), 
        ("couch", "pillows"), ("sofa", "pillows"), ("chair", "pillows"), ("seat", "pillows"), ("man", "bike"), 
        ("person", "bike"), ("guy", "bike"), ("donut", "glaze"), ("donuts", "glaze"), ("shelf", "book"), 
        ("man", "book"), ("woman", "book"), ("bear", "book"), ("plate", "cake"), ("table", "cake"), 
        ("box", "donut"), ("man", "donut"), ("tray", "donut"), ("plate", "donut"), ("boy", "donut"), 
        ("girl", "donut"), ("pizza", "ham"), ("boat", "rope"), ("man", "rope"), ("cow", "rope"), ("dog", "rope"), 
        ("horse", "rope"), ("sheep", "rope"), ("animal", "rope"), ("plate", "bread"), ("basket", "bread"), 
        ("dog", "toy"), ("cat", "toy"), ("child", "toy"), ("baby", "toy"), ("girl", "toy"), ("pizza", "tomatoes"), 
        ("sandwich", "tomatoes"), ("plate", "tomatoes"), ("man", "ball"), ("dog", "ball"), ("bag", "ball"), 
        ("boy", "ball"), ("player", "ball"), ("girl", "ball"), ("bear", "ball"), ("pizza", "vegetables"), 
        ("basket", "vegetables"), ("pot", "vegetables"), ("plate", "vegetables"), ("dish", "vegetables"), 
        ("box", "vegetables"), ("pan", "vegetables"), ("soup", "vegetables"), ("man", "headband"), 
        ("girl", "headband"), ("woman", "headband"), ("person", "headband"), ("player", "headband"), 
        ("bowl", "soup"), ("pot", "soup"), ("cup", "soup"), ("plate", "hot dog"), ("man", "hot dog"), 
        ("woman", "hot dog"), ("bun", "hot dog"), ("boy", "hot dog"), ("box", "hot dog"), ("container", "hot dog"), 
        ("tray", "hot dog"), ("man", "cigarette"), ("woman", "cigarette"), ("lady", "cigarette"), 
        ("man", "stick"), ("dog", "stick"), ("woman", "stick"), ("woman", "suitcase"), ("man", "suitcase"), 
        ("child", "suitcase"), ("lady", "suitcase"), ("boy", "suitcase"), ("passenger", "suitcase"), 
        ("girl", "suitcase"), ("person", "suitcase"), ("man", "dog"), ("woman", "dog"), ("girl", "dog"), 
        ("person", "dog"), ("guy", "dog"), ("boy", "dog"), ("pizza", "sausage"), ("plate", "sausage"), 
        ("man", "banana"), ("woman", "banana"), ("box", "banana"), ("bowl", "banana"), ("plate", "banana"),
        ("monkey", "banana"), ("child", "banana"), ("hot dog", "onion"), ("pizza", "onion"), 
        ("sandwich", "onion"), ("dish", "onion"), ("boat", "canopy"), ("bed", "canopy"), ("man", "tattoos"), 
        ("woman", "tattoos"), ("guy", "tattoos"), ("man", "bottle"), ("person", "bottle"), ("pants", "pockets"), 
        ("jacket", "pockets"), ("house", "porch"), ("pole", "lamp"), ("man", "paddle"), ("woman", "paddle"), 
        ("boy", "paddle"), ("person", "paddle"), ("donut", "nuts"), ("cake", "nuts"), ("pastry", "nuts"), 
        ("bouquet", "roses"), ("curtain", "roses"), ("vase", "roses"), ("container", "roses"), ("bush", "roses"), 
        ("woman", "roses"), ("donut", "powder"), ("woman", "cup"), ("man", "cup"), ("person", "cup"), 
        ("child", "cup"), ("boy", "cup"), ("bear", "heart"), ("cake", "heart"), ("card", "heart"), 
        ("shirt", "heart"), ("hat", "heart"), ("umbrella", "heart"), ("vase", "heart"), ("pillow", "heart"), 
        ("plate", "salad"), ("bowl", "salad"), ("elephant", "chain"), ("woman", "chain"), ("man", "chain"), 
        ("plate", "toast"), ("can", "utensil"), ("bowl", "utensil"), ("tower", "bell"), ("cow", "bell"), 
        ("collar", "bell"), ("building", "bell"), ("cat", "bell"), ("bed", "comforter"), ("woman", "apron"), 
        ("man", "apron"), ("lady", "apron"), ("man", "sneakers"), ("boy", "sneakers"), ("player", "sneakers"), 
        ("woman", "sneakers"), ("guy", "sneakers"), ("bowl", "cereal"), ("man", "luggage"), ("person", "luggage"), 
        ("woman", "luggage"), ("cart", "luggage"), ("woman", "earrings"), ("person", "earrings"), ("lady", "earrings"), 
        ("plate", "sandwich"), ("man", "sandwich"), ("tray", "sandwich"), ("bag", "sandwich"), ("platter", "sandwich"), 
        ("box", "sandwich"), ("child", "sandwich"), ("person", "sandwich"), ("container", "sandwich"), 
        ("boy", "sandwich"), ("girl", "sandwich"), ("guy", "sandwich"), ("bowl", "tangerine"), ("man", "outfit"), 
        ("woman", "outfit"), ("child", "outfit"), ("girl", "outfit"), ("person", "outfit"), ("doll", "outfit"), 
        ("pizza", "chicken"), ("plate", "chicken"), ("sandwich", "chicken"), ("salad", "chicken"), ("tree", "bananas"), 
        ("bowl", "bananas"), ("boy", "bananas"), ("lady", "bananas"), ("boat", "bananas"), ("table", "vase"), 
        ("man", "sandals"), ("woman", "sandals"), ("person", "sandals"), ("girl", "sandals"), ("boy", "sandals"), 
        ("lady", "sandals"), ("child", "sandals"), ("guy", "sandals"), ("plate", "broccoli"), ("pizza", "broccoli"), 
        ("bowl", "broccoli"), ("salad", "broccoli"), ("dish", "broccoli"), ("man", "headphones"), 
        ("person", "headphones"), ("lady", "headphones"), ("guy", "headphones"), ("woman", "headphones"), 
        ("child", "headphones"), ("boy", "headphones"), ("woman", "wig"), ("bottle", "pump"), ("dispenser", "pump"), 
        ("man", "cane"), ("woman", "cane"), ("person", "cane"), ("guy", "cane"), ("bowl", "spoon"), 
        ("glass", "spoon"), ("man", "spoon"), ("girl", "spoon"), ("boy", "spoon"), ("woman", "spoon"), 
        ("bowl", "apple"), ("box", "apple"), ("basket", "apple"), ("man", "fork"), ("girl", "fork"), ("boy", "fork"), 
        ("child", "fork"), ("woman", "fork"), ("lady", "fork"), ("woman", "blouse"), ("lady", "blouse"), 
        ("girl", "blouse"), ("person", "blouse"), ("glass", "drink"), ("man", "drink"), ("hot dog", "onions"), 
        ("pizza", "onions"), ("sandwich", "onions"), ("man", "controller"), ("girl", "controller"), 
        ("boy", "controller"), ("woman", "controller"), ("lady", "controller"), ("person", "controller"), 
        ("guy", "controller"), ("lady", "toothbrush"), ("man", "toothbrush"), ("baby", "toothbrush"), 
        ("boy", "toothbrush"), ("woman", "toothbrush"), ("child", "toothbrush"), ("guy", "toothbrush"), 
        ("toddler", "toothbrush"), ("girl", "toothbrush"), ("glass", "soda"), ("can", "soda"), ("bottle", "soda"), 
        ("tray", "cupcake"), ("man", "cupcake"), ("bag", "flour"), ("skateboard", "drawing"), ("shirt", "drawing"), 
        ("box", "tissue"), ("building", "fence"), ("tree", "fence"), ("desk", "drawers"), ("nightstand", "drawers"), 
        ("bowl", "orange"), ("pizza", "basil"), ("man", "towel"), ("woman", "towel"), ("building", "pillars"), 
        ("pizza", "spices"), ("bowl", "meal"), ("wall", "mirrors"), ("dog", "bandana"), ("man", "bandana"), 
        ("woman", "bandana"), ("boy", "bandana"), ("horse", "bandana"), ("girl", "bandana"), ("donut", "cream"), 
        ("cupcake", "cream"), ("pastries", "cream"), ("box", "donuts"), ("tray", "donuts"), ("plate", "donuts"), 
        ("tree", "bird"), ("bear", "clothes"), ("dog", "clothes"), ("man", "wristwatch"), ("woman", "wristwatch"), 
        ("person", "wristwatch"), ("man", "calf"), ("phone", "antenna"), ("car", "antenna"), ("boat", "antenna"), 
        ("building", "antenna"), ("router", "antenna"), ("tree", "blossoms"), ("man", "computer"), ("girl", "computer"), 
        ("person", "computer"), ("man", "rose"), ("vase", "rose"), ("suit", "rose"), ("flag", "rose"), ("cow", "tags"), 
        ("wall", "paintings"), ("building", "cross"), ("bus", "decoration"), ("cake", "decoration"), 
        ("elephant", "decoration"), ("roof", "decoration"), ("shirt", "decoration"), ("wall", "decoration"), 
        ("donut", "decoration"), ("mug", "decoration"), ("surfboard", "decoration"), ("snowboard", "decoration"), 
        ("cake", "decorations"), ("window", "decorations"), ("horse", "decorations"), ("plate", "decorations"), 
        ("tree", "decorations"), ("tower", "decorations"), ("building", "decorations"), ("wall", "decorations"), 
        ("clock", "decorations"), ("tower", "clocks"), ("building", "clocks"), ("wall", "clocks"), ("dish", "rice"), 
        ("bowl", "rice"), ("plate", "rice"), ("bowl", "carrots"), ("plate", "carrots"), ("container", "carrots"), 
        ("salad", "carrots"), ("bottle", "oil"), ("container", "oil"), ("pan", "oil"), ("bowl", "oil"), 
        ("glass", "oil"), ("train", "ladder"), ("truck", "ladder"), ("bed", "ladder"), ("building", "ladder"), 
        ("boat", "ladder"), ("house", "ladder"), ("woman", "heels"), ("shoes", "heels"), ("woman", "bikini"), 
        ("girl", "bikini"), ("man", "briefcase"), ("man", "sweatshirt"), ("person", "sweatshirt"), 
        ("boy", "sweatshirt"), ("woman", "sweatshirt"), ("girl", "sweatshirt"), ("mug", "tea"), ("table", "drinks"), 
        ("container", "drinks"), ("cake", "star"), ("surfboard", "star"), ("airplane", "star"), 
        ("elephant", "star"), ("shirt", "star"), ("box", "tissues"), ("shelf", "bottles"), ("man", "microphone"), 
        ("woman", "microphone"), ("lady", "microphone"), ("box", "candies"), ("bowl", "candies"), ("glass", "milk"), 
        ("bottle", "milk"), ("cup", "milk"), ("jar", "milk"), ("bowl", "milk"), ("cake", "strawberry"), ("man", "baby"), 
        ("woman", "baby"), ("tray", "buns"), ("glass", "beverage"), ("cup", "beverage"), ("man", "beverage"), 
        ("plate", "bacon"), ("pizza", "bacon"), ("salad", "bacon"), ("sandwich", "bacon"), ("necklace", "beads"), 
        ("woman", "bracelets"), ("lady", "bracelets"), ("girl", "bracelets"), ("boy", "bracelets"), ("box", "apples"), 
        ("bowl", "apples"), ("plate", "apples"), ("platter", "apples"), ("basket", "apples"), ("tree", "apples"), 
        ("bucket", "apples"), ("sandwich", "egg"), ("plate", "egg"), ("bread", "egg"), ("donut", "almonds"), 
        ("container", "almonds"), ("jar", "honey"), ("donut", "honey"), ("bottle", "honey"), 
        ("boat", "life preserver"), ("glass", "ice"), ("drink", "ice"), ("cup", "ice"), ("salad", "dressing"), 
        ("cup", "dressing"), ("wall", "art"), ("dish", "butter"), ("toast", "butter"), ("bread", "butter"), 
        ("knife", "butter"), ("mug", "spider"), ("hill", "bushes"), ("woman", "lipstick"), ("girl", "lipstick"), 
        ("house", "garage"), ("bowl", "broth"), ("pot", "broth"), ("tree", "ornaments"), ("bear", "costume"), 
        ("man", "costume"), ("woman", "costume"), ("toy", "costume"), ("cake", "berry"), ("waffles", "syrup"), 
        ("pancakes", "syrup"), ("plate", "syrup"), ("bottle", "syrup"), ("man", "pen"), ("woman", "pen"), 
        ("girl", "pen"), ("boy", "pen"), ("container", "hay"), ("cart", "hay"), ("bowl", "chips"), 
        ("plate", "chips"), ("man", "can"), ("woman", "flip flops"), ("man", "flip flops"), 
        ("person", "flip flops"), ("boy", "flip flops"), ("plate", "eggs"), ("bowl", "eggs"), 
        ("salad", "eggs"), ("basket", "eggs"), ("pan", "eggs"), ("toast", "eggs"), ("man", "wallet"), 
        ("trailer", "oranges"), ("tree", "oranges"), ("plate", "oranges"), ("window", "drapes"), 
        ("plate", "grapes"), ("plate", "fries"), ("basket", "fries"), ("bottle", "alcohol"), 
        ("shirt", "butterflies"), ("pants", "butterflies"), ("headband", "butterflies"), 
        ("plate", "dessert"), ("bowl", "dessert"), ("man", "cigar"), ("baby", "diaper"), 
        ("sandwich", "cucumber"), ("salad", "cucumber"), ("person", "magazine"), ("lady", "magazine"), 
        ("dog", "clothing"), ("wall", "vines"), ("container", "strawberries"), ("cake", "strawberries"), 
        ("cup", "strawberries"), ("dessert", "strawberries"), ("bowl", "strawberries"), 
        ("bucket", "strawberries"), ("woman", "jewelry"), ("girl", "jewelry"), ("man", "gun"), 
        ("woman", "gun"), ("woman", "child"), ("person", "child"), ("man", "child"), ("pizza", "herbs"), 
        ("chicken", "herbs"), ("wall", "television"), ("horse", "cart"), ("man", "cart"), 
        ("soda", "ice cube"), ("hot dog", "chili"), ("man", "name tag"), ("girl", "name tag"), 
        ("dog", "name tag"), ("woman", "name tag"), ("collar", "name tag"), ("man", "baseball"), 
        ("boy", "baseball"), ("person", "baseball"), ("plate", "fruits"), ("bowl", "fruits"), 
        ("table", "fruits"), ("basket", "fruits"), ("cake", "fruits"), ("bowl", "noodles"), 
        ("soup", "noodles"), ("man", "guitar"), ("boy", "guitar"), ("bear", "guitar"), ("plate", "pasta"), 
        ("box", "pasta"), ("bowl", "pasta"), ("umbrella", "cats"), ("pizza", "artichokes"), ("man", "sword"), 
        ("statue", "sword"), ("packet", "mayonnaise"), ("vase", "lily"), ("bowl", "berries"), ("bowl", "beans"), 
        ("horse", "carriage"), ("plate", "pancake"), ("man", "wii"), ("boy", "wii"), ("woman", "wii"), 
        ("elephant", "chains"), ("motorcycle", "chains"), ("blanket", "sunflowers"), ("bowl", "sunflowers"), 
        ("curtains", "sunflowers"), ("table", "sunflowers"), ("tray", "pastries"), ("plate", "pastries"), 
        ("bowl", "pastries"), ("laptop", "cables"), ("bowl", "cookies"), ("basket", "cookies"), ("plate", "cookies"), 
        ("box", "cookies"), ("sandwich", "beef")]
    for (s,o) in whitelist:
            return False
    return True

def filterBetween(s, o):
    betweenWhitelist = [("table", "chairs"), ("hot dog", "bun"), ("cigarette", "fingers"), ("houses", "trees"), ("onions", "bread"), 
    ("fence", "animals"), ("fence", "trees"), ("carrots", "bread"), ("house", "trees"), ("meat", "buns"), 
    ("river", "mountains"), ("cabinets", "windows"), ("building", "trees"), ("plant", "rocks"), ("water", "trees"), 
    ("water", "rocks"), ("art", "windows"), ("car", "trees"), ("road", "trees"), ("meat", "bread"), ("tail", "legs"), 
    ("road", "buildings"), ("bush", "cars"), ("bush", "train tracks"), ("backpack", "legs"), ("frisbee", "legs"), 
    ("frisbee", "hands"), ("ball", "legs"), ("ball", "feet"), ("street", "buildings"), ("bottle", "feet"), 
    ("plate", "legs"), ("sign", "train tracks"), ("bottles", "feet"), ("tree", "buildings"), ("tree", "houses"), 
    ("bird", "rocks"), ("dog", "legs"), ("pillow", "legs"), ("cell phone", "fingers"), ("box", "train tracks"), 
    ("cheese", "bread"), ("river", "hills"), ("steps", "bushes"), ("road", "mountains"), ("road", "bushes"), 
    ("road", "houses"), ("net", "players"), ("ball", "fingers"), ("street", "trees"), ("street", "houses"), 
    ("bottle", "legs"), ("plate", "hands"), ("bench", "trees"), ("bench", "plants"), ("door", "windows"), 
    ("sign", "windows"), ("sign", "wheels"), ("bottles", "legs"), ("tree", "zebras"), ("tree", "bushes"), 
    ("tree", "rocks"), ("bird", "trees"), ("dog", "cabinets"), ("weeds", "steps"), ("weeds", "rocks"), 
    ("motorcycle", "cars"), ("waterfall", "trees"), ("tomato", "bread"), ("luggage", "legs"), ("number", "doors"), 
    ("animal", "legs"), ("animal", "branches"), ("paper", "legs"), ("vase", "candles"), ("window", "cupboards"), 
    ("window", "cabinets"), ("window", "trees"), ("man", "trees"), ("man", "elephants"), ("man", "trains"), 
    ("man", "cars"), ("skateboard", "legs"), ("tomatoes", "bread"), ("desk", "beds"), ("can", "benches"), 
    ("hot dog", "bread"), ("flower", "towels"), ("flower", "paws"), ("chicken", "bun"), ("chicken", "bread"), 
    ("train", "bushes"), ("train", "buildings"), ("lettuce", "bread"), ("bear", "rocks"), ("toy", "paws"), 
    ("floor lamp", "chairs"), ("rope", "boats"), ("bikes", "buildings"), ("television", "windows"), ("gate", "hills"), 
    ("bridge", "buildings"), ("finger", "scissors"), ("elephants", "trees"), ("marker", "trees"), ("log", "rocks"), 
    ("bag", "arms"), ("cat", "shoes"), ("cabin", "trees"), ("bus", "cars"), ("cloud", "trees"), ("broccoli", "bowls"), 
    ("bucket", "jeans"), ("chair", "beds"), ("bacon", "carrots"), ("burger", "donuts"), ("platform", "trains"), 
    ("statue", "windows"), ("zebra", "rocks"), ("snowboard", "legs"), ("town", "mountains"), ("sauce", "bread"), 
    ("person", "chairs"), ("outlet", "windows"), ("vegetable", "bananas")]
    if (s,o) in betweenWhitelist:
        return False
    return True 

def filterBelow(s, o):
    whitelist = [("door", "window"), ("door", "oven"), ("door", "microwave"), ("goggles", "helmet"), ("tree", "bird"), ("tower", "kite"), ("door", "drawer"), ("door", "sign"), ("door", "horse"), ("door", "clock"), ("bush", "clock"), ("bush", "birds"), ("bed", "computer"), ("dog", "lady"), ("step", "bench"), ("plate", "hamburger"), ("motorcycle", "car"), ("motorcycle", "airplane"), ("broccoli", "carrot"), ("glasses", "counter"), ("glasses", "hat"), ("handbag", "hat"), ("weeds", "train"), ("shoe", "leaves"), ("fire", "grill"), ("undershirt", "shirt"), ("bird", "leaves"), ("sweater", "basket"), ("fruit", "sugar"), ("plant", "window"), ("umbrellas", "kite")]
    blacklist = [("sign", "sign"), ("sign", "stop sign"), ("stop sign", "sign"), ("stairs", "man"), ("woman", "man"), ("skier", "mountains"), ("house", "mountain"), ("dugout", "spectator"), ("plate", "man"), ("bench", "man"), ("cup", "toothbrushes"), ("racket", "waist"), ("river", "mountain"), ("vase", "flower"), ("sign", "road"), ("snow", "meadow"), ("grass", "rocks"), ("grass", "floor"), ("grass", "mountains"), ("man", "hill"), ("table", "sink"), ("stairs", "banana"), ("girl", "trees"), ("windows", "clock tower"), ("windows", "sidewalk"), ("plate", "boy"), ("house", "lighthouse"), ("house", "mountains"), ("house", "hill"), ("bench", "woman"), ("apple", "sign"), ("sand", "mountain"), ("sand", "legs"), ("person", "tree"), ("paper", "sink"), ("leaves", "banana"), ("leaves", "flowers"), ("leaves", "bananas"), ("vase", "flowers"), ("train", "street"), ("train", "forest"), ("lock", "knob"), ("pond", "bear"), ("bowl", "soup"), ("airport", "airplane"), ("basket", "apples"), ("basket", "bananas"), ("shoes", "shorts"), ("flowers", "bush"), ("shirt", "person"), ("shirt", "frame"), ("shirt", "glasses"), ("shirt", "earring"), ("mountain", "bird"), ("mountain", "train"), ("mountain", "airplane"), ("sun", "boat"), ("frosting", "cake"), ("town", "hill"), ("town", "tree"), ("cord", "label"), ("tie", "glasses"), ("shrimp", "sushi"), ("bushes", "trees"), ("stones", "fence"), ("stones", "zebras"), ("guy", "sunglasses"), ("van", "man"), ("shore", "rocks"), ("dress", "flower"), ("bread", "sandwich"), ("kites", "couple"), ("lawn", "picnic table"), ("arrow", "car"), ("marker", "orange"), ("canopy", "person"), ("pasture", "sheep"), ("pocket", "zipper"), ("grill", "train")]
    blacklistO = ["chin", "shore", "sky", "roof", "arm", "water", "shirt", "building", "wing", "foot", "leaves", "vest", "wall", "hand", "leg", "head", "feet", "house", "leaf", "log", "rock", "skier", "ceiling", "words", "tower", "clouds", "airport", "eye", "paw", "nose", "trunk", "player", "batter", "roll", "crust", "hamburger", "logo", "eyes", "meal", "jeans", "fingers", "collar", "clothes", "tree trunk", "lady", "face", "mouth", "ski", "walkway", "number", "ground", "handle", "pants", "neck", "arms", "lip", "tail", "patio", "rain", "cloud", "marker", "weeds"]
    blacklistS = ["base", "wood", "concrete", "court", "cement", "platform", "wave", "waves", "ground", "wheel", "water", "skateboard", "floor", "wheels", "surfboard", "road", "pole", "rock", "leg", "trees", "building", "skis", "rocks", "sidewalk", "wall", "bed", "snowboard", "pavement", "tree", "tire", "street", "field", "legs", "ski", "ocean", "hair", "clouds", "mountains", "post", "tower", "leaf", "plant", "hand", "dish", "beach", "bush", "fence", "door", "tires", "food", "home plate", "branch", "runway", "weeds", "bricks", "handle", "head", "cloud", "motorcycle", "mound", "cake", "step", "foot", "trunk", "paw", "strap", "fruit", "jet", "jacket", "feet", "word", "eye", "frisbee", "rope", "ear", "buildings", "tiles", "stone", "broccoli", "nose", "finger", "cushion", "lid", "logo", "number", "pants", "mouth", "vegetable", "umbrella", "shorts", "hill", "steps", "stick", "roof", "paint", "lake", "jeans", "tag", "purse", "fire", "thumb", "tail", "face", "umbrellas", "hills", "glass", "knob", "teeth", "ring", "arm", "walkway", "pillars", "feathers", "words", "collar", "wristband", "wing", "numbers", "city", "airplane", "deck", "chips", "icing", "fur", "sandwich", "sky", "kite", "flag", "sticks", "terrain", "sweatshirt", "mustache", "sock", "suit", "hands", "twig", "vest", "boot", "helmet", "goggles", "cap", "frame", "coat", "soup", "skirt", "porch", "luggage", "fingers", "glasses", "polar bear", "bat", "petal", "parking lot", "socks", "cross", "trucks", "battery", "net", "land", "jar", "handbag", "wrist", "lighthouse", "propeller", "furniture", "crust", "ship", "ceiling", "background", "surfer", "cushions", "label", "doorway", "charger", "sweater", "eyes", "skin", "forest", "couch", "balcony", "arms", "rooftop", "tie"]
    blacklistScat = []
    blacklistOcat = []

    for w in whitelist:
        if s == w[0] and o == w[1]:
            return False
    for b in blacklist:
        if s == b[0] and o == b[1]:
            return True
    if s in blacklistS or catn(s) in blacklistScat:
        return True
    if o in blacklistO or catn(o) in blacklistOcat:
        return True

    return False

def filterUnder(s, o):
    whitelist = [("bedspread", "jeans"), ("mountain", "clouds"), ("couch", "window"), ("couch", "blanket"), ("mountains", "clouds"), ("mountains", "snow"), ("door", "sink"), ("food", "umbrella"), ("branch", "bird"), ("branch", "owl"), ("motorcycle", "tree"), ("motorcycle", "dog"), ("step", "door"), ("frisbee", "dog"), ("rope", "bridge"), ("rope", "box"), ("rope", "log"), ("balcony", "clock"), ("steps", "door"), ("lake", "bridge"), ("jeans", "blanket"), ("fire", "pot"), ("umbrellas", "trees"), ("flag", "tent"), ("undershirt", "shirt"), ("bench", "leaves"), ("bird", "leaves"), ("giraffes", "leaves"), ("napkin", "hamburger"), ("rug", "clothes"), ("horse", "lady")]
    blacklist = [("man", "post"), ("fish", "shrimp"), ("carrot", "salad"), ("crate", "apples"), ("leaves", "branches"), ("leaves", "tree"), ("leaves", "rock"), ("leaves", "bananas"), ("leaves", "leaves"), ("leaves", "roses"), ("leaves", "bushes"), ("leaves", "petals"), ("leaves", "branch"), ("leaves", "trees"), ("leaves", "cauliflower"), ("window", "curtains"), ("skateboarder", "guy"), ("bench", "guy"), ("container", "rice"), ("spoon", "rice"), ("leaves", "branch"), ("bus", "tire"), ("person", "controller"), ("window", "curtain"), ("toilet", "lid"), ("pan", "lid"), ("box", "lid"), ("person", "bus"), ("bottle", "bus"), ("sign", "pole"), ("can", "pole"), ("bus", "pole"), ("tie", "suit"), ("sign", "stop sign"), ("leaves", "branches"), ("stump", "branches"), ("shoes", "people"), ("stairs", "people"), ("shoe", "coat"), ("vase", "flowers"), ("chair", "boy"), ("girl", "boy"), ("chair", "man"), ("chair", "woman"), ("chair", "bear"), ("scarf", "jacket"), ("tie", "jacket"), ("person", "jacket"), ("stop sign", "sign"), ("bacon", "food"), ("bowl", "food"), ("tomato", "food"), ("potato", "food"), ("rice", "food"), ("plate", "man"), ("sofa", "man"), ("mattress", "bed"), ("dishes", "food"), ("stump", "branches"), ("barrier", "hedge"), ("tomatoes", "leaves"), ("grass", "leaves"), ("tomato", "leaves"), ("poster", "picture"), ("screen", "laptop"), ("sandal", "foot"), ("watch", "shirt"), ("bacon", "food"), ("grill", "stone"), ("stairs", "people"), ("stairs", "person"), ("stairs", "man"), ("plate", "player"), ("water", "bridge"), ("water", "bird"), ("water", "birds"), ("pipe", "car"), ("bench", "building"), ("bench", "tower"), ("box", "train"), ("box", "people"), ("box", "arm"), ("box", "lid"), ("window", "glass"), ("bag", "handle"), ("bowl", "banana"), ("bowl", "food"), ("mountain", "city"), ("container", "rice"), ("container", "bananas"), ("container", "pizza"), ("container", "hot dog"), ("stop sign", "sign"), ("tomato", "food"), ("basket", "frisbee"), ("basket", "plate"), ("basket", "food"), ("basket", "fruit"), ("basket", "pizza"), ("basket", "hot dog"), ("bag", "eye"), ("bags", "eye"), ("bag", "eyes"), ("bags", "eyes"), ("vase", "flowers"), ("pot", "bush"), ("pot", "flower"), ("pot", "leaf"), ("pot", "plant"), ("pot", "broccoli"), ("rice", "food"), ("bike", "man"), ("bike", "officer"), ("bridge", "street"), ("bridge", "train tracks"), ("tent", "rock"), ("tent", "dog"), ("potato", "food"), ("statue", "rug"), ("statue", "tray"), t-("shirt", "shirt"), ("seat", "person"), ("seat", "man"), ("seat", "chair"), ("broccoli", "food")]
    blacklistO = ["chin", "shore", "sky", "roof", "arm", "water", "shirt", "building", "wing", "foot", "leaves", "vest", "wall", "hand", "leg", "head", "feet", "house", "leaf", "log", "rock", "skier", "ceiling", "words", "tower", "clouds", "airport", "eye", "paw", "nose", "trunk", "player", "batter", "roll", "crust", "hamburger", "logo", "eyes", "meal", "jeans", "fingers", "collar", "clothes", "tree trunk", "lady", "face", "mouth", "ski", "walkway", "number", "ground", "handle", "pants", "neck", "arms", "lip", "tail", "patio", "rain", "cloud", "marker", "weeds"]
    blacklistS = ["base", "wood", "concrete", "court", "cement", "platform", "wave", "waves", "ground", "wheel", "water", "skateboard", "floor", "wheels", "surfboard", "road", "pole", "rock", "leg", "trees", "building", "skis", "rocks", "sidewalk", "wall", "bed", "snowboard", "pavement", "tree", "tire", "street", "field", "legs", "ski", "ocean", "hair", "clouds", "mountains", "post", "tower", "leaf", "plant", "hand", "dish", "beach", "bush", "fence", "door", "tires", "food", "home plate", "branch", "runway", "weeds", "bricks", "handle", "head", "cloud", "motorcycle", "mound", "cake", "step", "foot", "trunk", "paw", "strap", "fruit", "jet", "jacket", "feet", "word", "eye", "frisbee", "rope", "ear", "buildings", "tiles", "stone", "broccoli", "nose", "finger", "cushion", "lid", "logo", "number", "pants", "mouth", "vegetable", "umbrella", "shorts", "hill", "steps", "stick", "roof", "paint", "lake", "jeans", "tag", "purse", "fire", "thumb", "tail", "face", "umbrellas", "hills", "glass", "knob", "teeth", "ring", "arm", "walkway", "pillars", "feathers", "words", "collar", "wristband", "wing", "numbers", "city", "airplane", "deck", "chips", "icing", "fur", "sandwich", "sky", "kite", "flag", "sticks", "terrain", "sweatshirt", "mustache", "sock", "suit", "hands", "twig", "vest", "boot", "helmet", "goggles", "cap", "frame", "coat", "soup", "skirt", "porch", "luggage", "fingers", "glasses", "polar bear", "bat", "petal", "parking lot", "socks", "cross", "trucks", "battery", "net", "land", "jar", "handbag", "wrist", "lighthouse", "propeller", "furniture", "crust", "ship", "ceiling", "background", "surfer", "cushions", "label", "doorway", "charger", "sweater", "eyes", "skin", "forest", "couch", "balcony", "arms", "rooftop", "tie"]
    blacklistScat = []
    blacklistOcat = []

    for w in whitelist:
        if s == w[0] and o == w[1]:
            return False
    for b in blacklist:
        if s == b[0] and o == b[1]:
            return True
    if s in blacklistS or catn(s) in blacklistScat:
        return True
    if o in blacklistO or catn(o) in blacklistOcat:
        return True

    return False

def filterAbove(s, o):
    whitelist = [("tree", "cow"), ("tree", "car"), ("tree", "fence"), ("tree", "giraffe"), ("tree", "horses"), ("tree", "people"), ("tree", "house"), ("tree", "truck"), ("tree", "train"), ("tree", "horse"), ("tree", "zebras"), ("tree", "bus"), ("tree", "motorcycle"), ("tree", "bear"), ("tree", "bull"), ("tree", "bench"), ("tree", "bike"), ("tree", "van"), ("tree", "giraffes"), ("tree", "suv"), ("trees", "train"), ("trees", "bus"), ("trees", "cars"), ("trees", "fence"), ("trees", "giraffe"), ("trees", "truck"), ("trees", "bird"), ("trees", "elephant"), ("trees", "cow"), ("trees", "sculpture"), ("trees", "zebra"), ("trees", "giraffes"), ("trees", "sheep"), ("trees", "sand"), ("trees", "umbrella"), ("trees", "bus stop"), ("trees", "bushes"), ("trees", "boat"), ("fence", "grass"), ("fence", "snow"), ("fence", "river"), ("fence", "giraffe"), ("fence", "boy"), ("balcony", "shop"), ("balcony", "garage"), ("balcony", "clock"), ("balcony", "door"), ("balcony", "ladder"), ("balcony", "pond"), ("balcony", "bus"), ("balcony", "store"), ("balcony", "cars"), ("boy", "table"), ("boy", "grass"), ("boy", "ball"), ("tower", "trees"), ("tower", "train"), ("tower", "truck"), ("tower", "baby"), ("grass", "sand"), ("skateboard", "boy"), ("skateboard", "staircase"), ("skateboard", "steps"), ("glass", "plate"), ("glass", "dog"), ("glass", "stove"), ("surfboard", "girl"), ("surfboard", "sand"), ("surfboard", "bridge"), ("surfboard", "car"), ("dog", "grass"), ("dog", "stones"), ("people", "building"), ("people", "grass"), ("people", "dogs"), ("people", "giraffe"), ("people", "clock"), ("stop sign", "crowd"), ("door", "stove"), ("door", "stairs"), ("mountains", "shore"), ("sun", "airplane"), ("sun", "water"), ("sun", "clouds"), ("sun", "forest"), ("sun", "ocean"), ("sun", "building"), ("sun", "trees"), ("car", "bed"), ("car", "cat"), ("stick", "pizza"), ("player", "grass"), ("plants", "balcony"), ("plants", "cabinets"), ("dock", "water"), ("seagull", "water"), ("seagull", "ocean"), ("baseball", "player"), ("cliff", "ocean"), ("cliff", "water"), ("cliff", "beach"), ("dish", "table"), ("mountain", "beach"), ("mountain", "trees"), ("kites", "ocean"), ("kites", "buildings"), ("kites", "beach"), ("food", "plate"), ("antenna", "building"), ("fog", "water"), ("chimney", "sign"), ("bleachers", "fence"), ("bird", "water"), ("bridge", "water"), ("kite", "water"), ("clouds", "water"), ("steam", "water"), ("seagull", "water"), ("birds", "water"), ("mountains", "water"), ("airplane", "water"), ("sun", "water"), ("cliff", "water"), ("fog", "water"), ("ball", "water"), ("frisbee", "water"), ("mountain", "water"), ("sign", "building"), ("airplane", "building"), ("clock", "building"), ("wires", "building"), ("roof", "building"), ("flag", "building"), ("people", "building"), ("steam", "building"), ("statue", "building"), ("decoration", "building"), ("antenna", "building"), ("bridge", "building"), ("lamp", "building"), ("sun", "building"), ("clouds", "trees"), ("airplane", "trees"), ("wires", "trees"), ("giraffe", "trees"), ("aircraft", "trees"), ("mountain", "trees"), ("sun", "trees"), ("bird", "trees"), ("bird", "ocean"), ("kite", "ocean"), ("cliff", "ocean"), ("seagull", "ocean"), ("sun", "ocean"), ("kites", "ocean"), ("birds", "ocean"), ("kite", "beach"), ("bird", "beach"), ("kites", "beach"), ("cliff", "beach"), ("kite", "field"), ("bird", "field"), ("airplane", "field"), ("balloon", "umbrella"), ("flowers", "umbrella"), ("airplane", "city"), ("bridge", "roadway")]
    blacklist = [("rug", "bowls"), ("crumb", "egg"), ("hat", "shirt"), ("leaves", "flowers"), ("basket", "animals"), ("window", "curtain"), ("paper", "can"), ("bed", "sofa"), ("man", "cake"), ("sign", "buildings"), ("man", "buildings"), ("woman", "pizza"), ("man", "pizza"), ("canopy", "tent"), ("sign", "container"), ("man", "lake"), ("sign", "apple"), ("grill", "doors"), ("boots", "bike"), ("leaves", "bananas"), ("weeds", "bear"), ("twigs", "bear"), ("screen", "platform"), ("windows", "platform"), ("orange", "fruit"), ("man", "bench"), ("leaves", "tree"), ("window", "tree"), ("curtain", "window"), ("sign", "buildings"), ("candle", "number"), ("noodles", "bowl"), ("soup", "bowl"), ("hedge", "bricks"), ("magazines", "flower"), ("tray", "plate"), ("clothes", "pants"), ("horse", "beach"), ("train", "wheel"), ("pants", "shoes"), ("stars", "tie"), ("jacket", "pants"), ("jacket", "snow pants"), ("snow", "man"), ("blinds", "windows"), ("blinds", "window"), ("orange", "fruit"), ("tent", "entrance"), ("sun", "rock"), ("sun", "boy"), ("flower", "vase"), ("plant", "wall"), ("plant", "grass"), ("curtain", "window"), ("curtain", "train"), ("counter", "sink"), ("counter", "counter"), ("counter", "street"), ("counter", "dishwasher"), ("counter", "floor"), ("counter", "ground"), ("sink", "counter"), ("sink", "bathroom"), ("woman", "beach"), ("woman", "ocean"), ("woman", "floor"), ("woman", "sidewalk"), ("woman", "pants"), ("woman", "ground"), ("woman", "shoes"), ("branches", "trunk"), ("basket", "wheel"), ("plate", "plate"), ("plate", "tire"), ("branch", "grass"), ("branch", "building"), ("leaves", "tree"), ("leaves", "building"), ("leaves", "flowers"), ("leaves", "bananas"), ("person", "water"), ("person", "skateboard"), ("person", "steps"), ("person", "wall"), ("person", "ground"), ("person", "beach"), ("person", "gloves"), ("person", "floor"), ("person", "skis"), ("person", "pavement"), ("person", "road"), ("man", "water"), ("man", "ground"), ("man", "skateboard"), ("man", "ocean"), ("man", "steps"), ("man", "road"), ("man", "ground"), ("man", "skateboard"), ("man", "steps"), ("man", "bench"), ("man", "pole"), ("man", "floor"), ("man", "arm"), ("man", "lake"), ("man", "locomotive"), ("man", "air"), ("man", "hill"), ("man", "skis"), ("man", "couch"), ("man", "stones"), ("man", "hand"), ("man", "field"), ("man", "plate"), ("sign", "sign"), ("sign", "road"), ("sign", "building"), ("sign", "street"), ("sign", "apple"), ("sign", "stop sign"), ("sign", "building"), ("sign", "sidewalk"), ("sign", "ground"), ("sign", "fruit"), ("sign", "highway"), ("stop sign", "sign")]
    blacklistO = ["water", "ground", "street", "road", "building", "head", "floor", "ocean", "beach", "wall", "sidewalk", "field", "stop sign", "donut", "skateboard", "hand", "steps", "highway", "umbrella", "wheel", "city", "nose", "bathroom", "oranges", "airport", "land", "pants", "walkway", "number", "garage", "vase", "stones", "pavement", "runway", "station", "shoes", "post", "lemons", "logo", "lounge", "kite", "pole", "tire", "roadway", "bag", "skis", "face", "porch", "air"]
    blacklistS = ["sky", "clouds", "tree", "cloud", "wall", "trees", "ceiling", "pole", "building", "hand", "fence", "roof", "number", "frame", "head", "balcony", "letter", "boy", "tower", "grass", "hair", "skateboard", "rock", "glass", "surfboard", "dog", "handle", "logo", "toilet", "leaf", "walkway", "knob", "foot", "word", "people", "rocks", "stop sign", "ski", "feet", "hill", "door", "mountains", "arm", "tiles", "car", "bush", "water", "bus", "horn", "fruit", "post", "wallpaper", "words", "gate", "eye", "glasses", "nose", "wing", "leg", "stick", "background", "teeth", "decorations", "motorcycle", "display", "hands", "shirt", "mustache", "skateboarder", "player", "plants", "road", "buildings", "baseball", "boat", "guy", "dish", "platform", "mountain", "tail", "wristband", "mane", "fur", "surfer", "face", "lamp shade", "bushes", "shoe", "trunk", "collar", "seat", "zebra", "food", "skier", "paw", "wheel", "house", "hot dog", "tree branch", "log", "magazine", "ear", "socks", "crowd", "paint", "fans", "lock", "table", "zipper", "logs", "ceiling light", "wings", "highway", "numbers", "forest", "ring", "stone", "land", "animal", "fog", "sidewalk", "chimney", "belt", "feathers", "bleachers", "shorts", "fireplace", "train tracks", "curtains", "skin", "goggles", "air", "legs", "runway", "finger", "neck", "street"]
    blacklistScat = []
    blacklistOcat = []

    for w in whitelist:
        if s == w[0] and o == w[1]:
            return False
    for b in blacklist:
        if s == b[0] and o == b[1]:
            return True
    if s in blacklistS or catn(s) in blacklistScat:
        return True
    if o in blacklistO or catn(o) in blacklistOcat:
        return True

    return False

prepFilters = {
    "under": filterUnder,
    "underneath": filterUnder,
    "beneath": filterUnder,
    "below": filterBelow,
    "above": filterAbove,
    "on": filterOn,
    "in": filterIn,
    "inside": filterInside,
    "at": filterAt,
    "with": filterWith,
    "between": filterBetween,
    "in between": filterBetween,
    "has": filterHas,
} 
# has -> with


# def filterHas(s, o):
#     # door_window
#     whitelistO = ["beard", "mustache", "headboard"]
#     if o in whitelistO:
#         return False
#     extraParts = ["door frame", "doorway", "window frame", "touchpad", "horse hoof", "strap", "straps", "hair", "skin", "fur", "wool", "feathers", "seat belt", "cockpit"]
#     if catn(o) in ["body part", "part"] or o in extraParts:
#         return True
#     return False

with open("../objs/cObjsNV.json", "r") as f:
    objDict = json.load(f)

with open(inpName, "r") as f:
    inp = list(f)
    catc = defaultdict(lambda: defaultdict(lambda: 0))
    cats = defaultdict(lambda: 0)
    cato = defaultdict(lambda: 0)

    sc = defaultdict(lambda: defaultdict(lambda: 0))
    oc = defaultdict(lambda: defaultdict(lambda: 0))
    sm = defaultdict(lambda: 0)
    om = defaultdict(lambda: 0)

    onc = defaultdict(lambda: defaultdict(lambda: 0))

    oncW = defaultdict(lambda: defaultdict(lambda: 0))
    onsW = defaultdict(lambda: 0)
    onoW = defaultdict(lambda: 0)

    oncB = defaultdict(lambda: defaultdict(lambda: 0))
    onsB = defaultdict(lambda: 0)
    onoB = defaultdict(lambda: 0)

    oncByS = defaultdict(lambda: defaultdict(lambda: 0))
    oncByO = defaultdict(lambda: defaultdict(lambda: 0))

    top2s = defaultdict(lambda: defaultdict(lambda: 0))
    top2o = defaultdict(lambda: defaultdict(lambda: 0))

    for i in inp:
        b = i.startswith("B")
        if b:
            i = i[2:]
        inp = i.split(",")
        if len(inp) < 2:
            print (inp)
            continue
        ws,c = inp
        s,o = ws.split("_",1)
        c = int(c)
        if s in objDict and o in objDict:
            catc[catn(s)][catn(o)] += c
            cats[catn(s)] += c
            cato[catn(o)] += c

            top2s[s][o] += c
            top2o[o][s] += c
            onc[s][o] += c

            if not filterOn(s,o):
                oncW[s][o] += c
                onsW[s] += c
                onoW[o] += c

                oncByS[catn(s)][s+"_"+o] += c
                oncByO[catn(o)][s+"_"+o] += c

                sc[s][o] += c
                oc[o][s] += c
                sm[s] += c
                om[o] += c                             
            else:
                oncB[s][o] += c
                onsB[s] += c
                onoB[o] += c

json.dump(catc, catcJ)
json.dump(cats, catsJ)
json.dump(cato, catoJ)

json.dump(oncW, oncWJ)
json.dump(onsW, onsWJ)
json.dump(onoW, onoWJ)

json.dump(oncB, oncBJ)
json.dump(onsB, onsBJ)
json.dump(onoB, onoBJ)

def printD(f, d):
    dlist = d.items()
    dlist = sorted(dlist,key = lambda x: x[1], reverse = True)
    for x in dlist:
        f.write(str(x[0])+","+str(x[1])+"\n")

def printCombs(f, combsDict, marginalDict = None, printX = True, flip = False, flipflop = False):
    if marginalDict is not None:
        xlist = sorted(combsDict.keys(),key = lambda x: marginalDict[x], reverse = True)
    else:
        xlist = combsDict
    for x in xlist:
        try:
          if marginalDict is not None:
            f.write("+ "+x+","+str(marginalDict[x]))
          else:
            f.write("+ "+x)
          f.write("\n")
          s = sorted(combsDict[x].items(), reverse = True, key = lambda i: i[1])
          for y, num in s:
              try:
                if printX:
                    if flip:
                        toprint = y
                    else:
                        if flipflop:
                            toprint = y
                        else:
                            toprint = x+"_"+y
                    f.write(toprint + "," + str(num))
                else:
                    f.write(y + "," + str(num))
              except:
                pass
              f.write("\n")
        except:
            pass
        f.write("\n")

def printCombS(f, combsDict, flip = False):
    listD = []
    for x in combsDict:
        for y in combsDict[x]:
            listD.append(((x,y), combsDict[x][y]))

    listS = sorted(listD, reverse = True, key = lambda i: i[1])
    for x in listS:
        if flip:
            toPrint = str(x[0][1])+"_"+str(x[0][0])
        else:
            toPrint = str(x[0][0])+"_"+str(x[0][1])
        f.write(toPrint+","+str(x[1])+"\n")   

def top2(f, f2, combs):
    key2info = {}
    for key in combs:
        sortedNums = sorted(combs[key].items(), reverse = True, key = lambda i: i[1])
        if len(sortedNums) > 1:
            key2info[key] = (sortedNums[1][1], sortedNums[:20])
        else:
            key2info[key] = (0, [])

    listS = sorted(key2info.items(), reverse = True, key = lambda i: i[1][0])
    
    for e in listS:
        x, (onum, sublist) = e
        try:
          f.write("+ "+str(x)+","+str(onum))
          f.write("\n")
          f2.write(str(x)+","+str(onum))
          f2.write("\n")          
          for y, num in sublist:
              try:
                f.write(str(x)+"_"+str(y) + "," + str(num))
              except:
                pass
              f.write("\n")
        except:
            pass
        f.write("\n")

printD(catsT, cats)
printD(catoT, cato)
printCombs(catcT, catc)
printCombs(scT, sc, marginalDict = sm)
printCombs(ocT, oc, marginalDict = om, flipflop = True)
printCombS(catcTs, catc)

printCombs(byS, oncByS, printX = False)
printCombs(byO, oncByO, printX = False)

printD(onsWT, onsW)
printD(onoWT, onoW)
printCombs(oncWT, oncW) # , flip = True
printCombS(oncWTs, oncW)

printD(onsBT, onsB)
printD(onoBT, onoB)
printCombs(oncBT, oncB)
printCombS(oncBTs, oncB)

top2(top2S, top2SS, top2s)
top2(top2O, top2OO, top2o)
