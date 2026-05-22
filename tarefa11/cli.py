import users_wrapper as u


def rodar_sistema():
    while True:
        print("\n1 - Listar usuários")
        print("2 - Ler usuário")
        print("3 - Editar usuário")
        print("4 - Excluir usuário")
        print("5 - Criar usuário")
        print("6 - Sair")

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            print("Lista de usuários:")
            users = u.list()
            if users:
                for user in users:
                    print(f"ID: {user['id']}, Nome: {user['name']}")
            else:
                print("Nenhum usuário encontrado.")

        elif opcao == "2":
            user_id = input("Digite o ID do usuário: ")
            user = u.read(user_id)
            if user:
                print(f"Nome: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"Telefone: {user['phone']}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":
            user_id = input("Digite o ID do usuário: ")
            user = u.read(user_id)
            if user:
                print(f"Nome: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"Telefone: {user['phone']}")

                user["name"] = input("Digite o novo nome do usuário: ")
                user["email"] = input("Digite o novo email do usuário: ")
                user["phone"] = input("Digite o novo telefone do usuário: ")

                novo_usuario = u.update(user_id, user)
                if novo_usuario:
                    print(f"Usuário {novo_usuario['name']} atualizado com sucesso.")
                else:
                    print("Erro ao atualizar usuário.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            user_id = input("Digite o ID do usuário: ")
            user = u.read(user_id)
            if user:
                print(f"Nome: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"Telefone: {user['phone']}")

                confirmacao = input("Deseja excluir este usuário? (s/n): ").strip().lower()
                if confirmacao == "s":
                    u.delete(user_id)
                    print("Usuário excluído com sucesso.")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            print("Digite os dados do novo usuário:")
            user = {
                "name": input("Nome: "),
                "email": input("Email: "),
                "phone": input("Telefone: ")
            }

            confirmacao = input("Deseja criar este usuário? (s/n): ").strip().lower()
            if confirmacao == "s":
                novo_usuario = u.create(user)
                if novo_usuario:
                    print(f"Usuário {novo_usuario['name']} criado com sucesso.")
                else:
                    print("Erro ao criar usuário.")
            else:
                print("Criação cancelada.")

        elif opcao == "6":
            print("Tchau")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    rodar_sistema()