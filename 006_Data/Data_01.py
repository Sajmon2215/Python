import xml.sax
from xml.dom import minidom


class SaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.type = ""
        self.manufacturer = ""
        self.model = ""
        self.price = ""
        self.productionYear = ""

    def startElement(self, tag, attributes):
        self.currentData = tag
        if tag == "component":
            print("*****Component*****")

    def endElement(self, tag):
        if tag == "manufacturer":
            print("Manufacturer:", self.manufacturer)
        elif tag == "model":
            print("Model:", self.model)
        elif tag == "price":
            print("Price:", self.price)
        elif tag == "productionYear":
            print("Production Year:", self.productionYear)
        self.currentData = ""

    def characters(self, content):
        if self.currentData == "type":
            self.type = content
        elif self.currentData == "manufacturer":
            self.manufacturer = content
        elif self.currentData == "model":
            self.model = content
        elif self.currentData == "price":
            self.price = content
        elif self.currentData == "productionYear":
            self.productionYear = content


sax = SaxHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(sax)
parser.parse("parts.xml")

file = minidom.parse("parts.xml")
components = file.getElementsByTagName("component")

for component in components:
    component.getElementsByTagName("productionYear")[0].childNodes[0].data = 2020

with open("parts_result.xml", 'w+') as f:
    f.write(file.toxml())