import xml.etree.ElementTree as ET

def readFontXML(source):
  content = ""
  with open(source, 'r', encoding='utf-8') as xml:
      content = xml.read()
  return content

def updateFontXML(content, sizeMultiplier):
  tree = ET.fromstring(content)
  for element in tree:
      fontSize = element.get('FontSize')
      scaledSize = str(int(float(fontSize) * sizeMultiplier))
      element.set('FontSize', scaledSize)
      # print(element.get('FontSize'))
  return tree

def saveChangesToXML(XMLTree, destination):
  content = ET.tostring(XMLTree)
  with open(destination, 'wb') as xml:
      meta = b'<?xml version="1.0" encoding="utf-8"?> \n'
      xml.write(meta)
      xml.write(content)

# content = readFontXML()
# tree = updateFontXML(content, sizeMultiplier=1.0)
# saveChangesToXML(tree)
