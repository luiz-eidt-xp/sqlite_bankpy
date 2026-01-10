import sqlite3 as sql3
from admin import bank_admin
# ! senha do administrador
senha_admin = "123sqlite"

conexao = sql3.connect("sqlite/banco.db")
cursor = conexao.cursor()

rodando = True
logado = False
usuario_atual = None

while rodando:

    if not logado:
        print('\n//// Deseja logar como? ////\n')
        try:
            options = int(input("""
(1) Logar como usuário
(2) Logar como Administrador
(0) Sair do sistema
            """))
        except ValueError:
            print("Opção inválida.")
            continue

        if options == 1:
            uid = input("Digite o seu id de usuário: ")
            cursor.execute(
                "SELECT id, titular FROM contas_bancarias WHERE id = ?",
                (uid,)
            )
            user = cursor.fetchone()

            if user:
                usuario_atual = user
                logado = True
                print(f"\n----Seja bem-vindo {user[1]}, você logou com sucesso!----\n")
            else:
                print("Usuário não encontrado.")

        elif options == 2:
            pass_admin = input("Digite a senha de admin: ")
            if pass_admin == senha_admin:
              print("\n----Logado como admin!----\n")
              bank_admin() # supondo que isso gerencie o admin
            else: 
                print("Senha errada!")
        elif options == 0:
            rodando = False
        else:
            print("Opção inválida.")

    else:
        print("O que deseja fazer agora?")
        login_opt = int(input("""
(1) Sacar
(2) Transferir
(3) Sair da conta
        """))

        if login_opt == 1:
            print("Função sacar (em desenvolvimento)")
        elif login_opt == 2:
            print("Função transferir (em desenvolvimento)")
        elif login_opt == 3:
            logado = False
            usuario_atual = None
            print("\n!!!! Você saiu da conta. !!!!")
        else:
            print("Opção inválida.")

conexao.commit()
