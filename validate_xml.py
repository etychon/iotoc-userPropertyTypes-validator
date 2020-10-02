import argparse
import json
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


parser = argparse.ArgumentParser()
parser.add_argument("file", help="input XML file (ie: userPropertyTypes.xml)")
args = parser.parse_args()
tree = '';
checked = 0;

try:
    tree = ET.parse(args.file)

    for elem in tree.iter():
        checked += 1

        if (elem.text and (elem.text[0] == '[')):
            print ("**JSON** %s: '%s'" % (elem.tag, elem.text))
            try:
                json.loads(elem.text)
                print ("**JSON OK** %s: '%s'" % (elem.tag, elem.text))                                                      
            except:
                print ("**JSON ERROR** %s: '%s'" % (elem.tag, elem.text))
        else:
            print ("%s: '%s'" % (elem.tag, elem.text))

except ParseError as p:
    print("** XML ERROR** \"" + str(p.msg) + "\"")
    exit

except TypeError as p:
    print("** XML ERROR** \"" + str(p.msg) + "\"")
    exit
    
except:
    print("Unexpected error:", sys.exc_info()[0])
    exit

print(" === Checked " + str(checked)+ " items: File is verfied and valid === ")
        