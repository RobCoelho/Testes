import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb
# -*- coding: latin-1 -*-


def mariadb_selecionar_imovel():
    try:
        mariadb_connection = mariadb.connect(host='db-vws-01.vistahost.com.br',
                                             user='basedete', password='I3Ugaok9fQsGJCDT', database='basedete')
        cursor = mariadb_connection.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está errado com o seu nome de usuário e password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)
    cursor = mariadb_connection.cursor()

    try:
        cursor.execute("SELECT CODIGO FROM CADIMO LIMIT 50")
        result = cursor.fetchall()
        print('\n\nConsultar Imóvel:\n')

    except mariadb.Error as error:
        print("Error: {}".format(error))

    def lista_tags():

        from xml.dom import minidom
        import os
        root = minidom.Document()
        encoding = "utf-8"
        xml = root.createElement('Anuncios')
        root.appendChild(xml)

        imovelChild = root.createElement('Imovel')
        xml.appendChild(imovelChild)

        for item in result:
            tag = 'CodigoImovel'
            valor = item

            childOfImovel = root.createElement('%s' % tag)
            childOfImovel.appendChild(root.createTextNode('%s' % valor))
            imovelChild.appendChild(childOfImovel)

        xml_str = root.toprettyxml(indent="\t")

        save_path_file = "teste.xml"

        with open(save_path_file, "w") as f:
            f.write(xml_str)

    lista_tags()

    mariadb_connection.close()

    return

mariadb_selecionar_imovel()
