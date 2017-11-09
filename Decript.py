#!/usr/bin/python
import H as H
import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb
import urllib
from BeautifulSoup import BeautifulSoup # Ou: from bs4 import BeautifulSoup

def funcao(url, ano):
    parametros = urllib.urlencode({'ano': ano, 'entrar': 'Buscar'})
    html = urllib.urlopen(url, parametros).read()
    return html

url  = "http://venus.maringa.pr.gov.br/arquivos/orgao_oficial/paginar_orgao_oficial_ano.php"
ano  = 2015
html = funcao(url, ano)
soup = BeautifulSoup(html)

for link in soup.findAll('a'):
    print(link.get('href'))

curl -s -X POST -H "Cache-Control: no-cache" --data-urlencode "de=$HOST_CRIPT" "http://admimobi.vistahost.com.br/c"