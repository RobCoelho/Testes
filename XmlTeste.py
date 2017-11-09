from xml.dom import minidom as dom
from xml.dom.ext import PrettyPrint
doc = dom.Document()
div = dom.createElement('div')
text = dom.createTextNode('Python and XML')
div.appendChild(text)
doc.appendChild(div)

PrettyPrint(doc)
