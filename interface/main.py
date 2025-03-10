from nicegui import ui

def verificar_login():
    usuario = usuario_input.value
    senha = senha_input.value

    if usuario == "admin" and senha == "1234":
        resultado_label.text = "Login bem-sucedido!"
        resultado_label.style("color: green;")
    else:
        resultado_label.text = "Usuário ou senha incorretos!"
        resultado_label.style("color: red;")

# Criando a interface
ui.label("Login").style("font-size: 20px; font-weight: bold;")

usuario_input = ui.input(label="Usuário", placeholder="Digite seu usuário")
senha_input = ui.input(label="Senha", placeholder="Digite sua senha", password=True)

ui.button("Entrar", on_click=verificar_login)

resultado_label = ui.label().style("margin-top: 10px;")

ui.run()
