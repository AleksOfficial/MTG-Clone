from json.decoder import JSONDecoder
import sys;
import json;
from os import listdir
from os.path import isfile, join



def get_deck(filename,outputname):
    print(filename)
    file = open(filename,"r",encoding="utf-8")
    s = file.read()
    #print(s)
    #data -> mainboard -> list -> dict: name
    x = json.loads(s)
    if(x['data']['type']=="Theme Deck"):
        output = open(outputname,"w")
        for j in x['data']['mainBoard']:
            output.write(j['name'])
            output.write("\n")
        output.close()
    file.close()
    #for 
    
    


    


if __name__ == "__main__":
    if(len(sys.argv)!=2):
        #Keywords are passed; 
        raise SyntaxError("Invalid number of arguments, amount of arguments: {}".format(len(sys.argv)))
        #main("GoblinFire_P02.json","GoblinDeck")
    else:
        onlyfiles = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
        for file in onlyfiles:
            get_deck("/".join((sys.argv[1],file)), join("./Decks/",(file.split()[0]+".txt")))
            #join()
        
