import streamlit as st
from auth import cadastrar_usuario, verificar_login
from cotacao import buscar_cotacao

st.set_page_config(page_title="Cotação Fácil", layout="centered")

menu = ["Login", "Cadastro"]
escolha = st.sidebar.selectbox("Menu", menu)

if escolha == "Cadastro":
    st.title("Criar Conta")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        if cadastrar_usuario(usuario, senha):
            st.success("Cadastro realizado com sucesso! Faça login.")
        else:
            st.error("Usuário já existe.")

elif escolha == "Login":
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if verificar_login(usuario, senha):
            st.success(f"Bem-vindo, {usuario}!")

            # Tela de cotação
            st.subheader("🔍 Buscar Cotação")
            simbolo = st.text_input("Digite o código da ação ou moeda (ex: AAPL, BTC)")
            if st.button("Buscar Cotação"):
                resultado = buscar_cotacao(simbolo.upper())
                if resultado:
                    st.json(resultado)
                else:
                    st.error("Símbolo inválido ou erro na API.")
        else:
            st.error("Credenciais inválidas.")
