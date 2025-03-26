usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Coloque o login")
senha = input("coloque a senha")

if usuario == usuario_correto:
    if senha == senha_correta:
        print("Login bem-sucedido")
    else:
        print("senha incorreta")
else:
    print("usuario não encotrado")