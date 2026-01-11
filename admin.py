import sqlite3 as sql3

conexão = sql3.connect("sqlite/banco.db")
cursor  = conexão.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS contas_bancarias (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
             )
        """)
print('==== Bem vindo ao sistema do banco generico ====')
def bank_admin():
    action = int(input('''/ Selecione qual ação vc deseja fazer/
               
(1)Listar todos os usuários
(2)Ver saldo de algum usuário   
(3)Deletar um usuário   
               '''))
    if action == 1:
        cursor.execute("SELECT * FROM contas_bancarias")
        dados = cursor.fetchall()
        for conta in dados:
            id, titular, saldo, cpf = conta
            print(f"""
({id})----------------           
Titular: {titular}
Saldo: {saldo}
Cpf: {cpf}
-------------------   
""")    
    elif action == 2:
        user = input("Digite o usuário: ")
        cursor.execute("""SELECT id, titular, saldo FROM contas_bancarias WHERE titular = ?""", (user,))
        users = cursor.fetchall()
        for user in users:
                id, titular, saldo = user
                print(f"""
({id})----------------           
Titular: {titular}
Saldo: {saldo}
-------------------   
""")
    elif action == 3:
         whatid = input("Digite o id do usuário que deseja deletar: ")
         cursor.execute("""DELETE FROM contas_bancarias WHERE id = ?""", (whatid,))
         print("Usuário deletado com sucesso!")
    else:
        print("Escolha algumas das opções!!")
        return
conexão.commit()