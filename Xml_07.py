#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import minidom
import os
import BuscaImovel
root = minidom.Document()

xml = root.createElement('Anuncios')
root.appendChild(xml)

imovelChild = root.createElement('Imovel')
xml.appendChild(imovelChild)

childOfImovel = root.createElement(str(BuscaImovel.tag))
childOfImovel.appendChild(root.createElement(str(BuscaImovel.valor)))
imovelChild.appendChild(childOfImovel)

xml_str = root.toprettyxml(indent="\t")

save_path_file = "teste.xml"

with open(save_path_file, "w") as f:
    f.write(xml_str)

