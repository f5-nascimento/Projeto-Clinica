import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "***********",
    database = "clínica"
)

cursor = conexao.cursor()

tela = input("SISTEMA DE GESTÃO DE MÉDICOS" + "\n" +
             "1 - Cadastrar Médicos " + "\n" +
             "2 - Atualiazar Médicos" + "\n" +
             "3 - Deletar Médicos" + "\n" +
             "4 - Consultar Médicos " "\n" +
             "Qual Operação Deseja Fazer? ")

if tela == "1":
    print(" ")
    print("--------------------------------------")
    print("CADASTRO DE MÉDICOS")
    nome = input("Digite o nome do Médico: ")
    especialidade = input("Digite a especialidade do Médico: ")
    cursor.execute("insert into medicos (nome_medicos, especialidade_medicos) values ('{}', '{}')".format(nome, especialidade))
    conexao.commit()
    print(cursor.rowcount, " inserida com sucesso")

    cursor.execute("select * from medicos")
    myresult = cursor.fetchall()

    for i in myresult:
        print(i)


elif tela == "2":
    print(" ")
    print("--------------------------------------")
    print("ATUALIZAR MÉDICOS")
    cursor.execute("select * from medicos")
    myresult = cursor.fetchall()

    for i in myresult:
        print(i)

    id = input("Digite o id do Médico: ")
    nome = input("Digite o nome do Médico: ")
    especialidade = input("Digite a especialidade do Médico: ")
    cursor.execute("update medicos set nome_medicos = ('{}'), especialidade_medicos = ('{}') "
                   "where id_medicos = ({}) ".format(nome, especialidade, id))
    conexao.commit()

    cursor.execute("select * from medicos")
    myresult = cursor.fetchall()

    for i in myresult:
        print(i)



elif tela == "3":
    print(" ")
    print("--------------------------------------")
    print("DELETAR MÉDICOS")
    cursor.execute("select * from medicos")
    myresult = cursor.fetchall()

    for i in myresult:
        print(i)

    id = input("Digite o id do Médico: ")
    cursor.execute("delete from medicos where id_medicos = ({})".format(id))
    conexao.commit()

    cursor.execute("select * from medicos")
    myresult = cursor.fetchall()

    for i in myresult:
        print(i)



elif tela == "4":
    print(" ")
    print("--------------------------------------")
    print("MÉDICOS CADASTRADOS")
    cursor.execute("select * from medicos")
    myresult = cursor.fetchall()

    for i in myresult:
        print(i)










