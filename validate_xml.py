import json
import xml.etree.ElementTree as ET
tree = ET.parse('userPropertyTypes.xml')

for elem in tree.iter():

    if elem.text[0] == '[':
        print ("**JSON** %s: '%s'" % (elem.tag, elem.text))
        try:
            json.loads(elem.text)
            print ("**JSON OK** %s: '%s'" % (elem.tag, elem.text))                                                      
        except:
            print ("**JSON ERROR** %s: '%s'" % (elem.tag, elem.text))
    else:
        print ("%s: '%s'" % (elem.tag, elem.text))
        