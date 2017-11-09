import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb


def mariadb_selecionar_departamento():
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
        cursor.execute("select ID, NOME, RE_FTP_HOST,"
                       "RE_FTP_USER, RE_FTP_SENHA, STATUS from CADCLI WHERE STATUS='Ativo' AND RE_CSITE_OLX='Ativo'"
                       "AND RE_FTP_HOST <> 'http://awsup1.imo.bi/aws-dsk/index.php'")
        result = cursor.fetchall()
        print('\n\nClientes com integração ativa - OLX:\n')
        for row in result:
            print(' -------------------------------\n |ID Cliente: %s\n' % row[0],
                  '|Nome: %s\n |\n' % row[1], '|DADOS DA CONEXÃO: \n' ' |Host: %s\n' % row[2], '|Usuário: %s\n' % row[3]
                  , '|Senha: %s\n' % row[4], '-------------------------------\n\n')
    except mariadb.Error as error:
        print("Error: {}".format(error))
    mariadb_connection.close()
    return

mariadb_selecionar_departamento()
