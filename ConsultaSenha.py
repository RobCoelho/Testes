#!/usr/bin/python
import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb

email = input('Digite seu e-mail:\n')
def mariadb_buscar_senha():
    try:
        mariadb_connection = mariadb.connect(host='dbvista201.cwc1g77rsraq.sa-east-1.rds.amazonaws.com',
                                             user='user_select', password='D3$745%9%29$', database='vistaimobi')
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
        cursor.execute("SELECT SENHA FROM VISTA_CADCLI_RE WHERE EMAIL LIKE '%"+email+"%'")
        result = cursor.fetchall()
        for row in result:
            print('Senha do cliente: %s\n' % row[0])
            print("PYTHON > PHP!! SEU LOSER!!")
    except mariadb.Error as error:
        print("Error: {}".format(error))
    mariadb_connection.close()
    return


mariadb_buscar_senha()
