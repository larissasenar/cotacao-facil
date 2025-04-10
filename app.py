import streamlit as st
from auth import cadastrar_usuario, verificar_login
from cotacao import buscar_cotacao, buscar_historico
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="💸 Cotação Fácil", layout="centered")

# Inicializa a sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.historico = []

# MENU LATERAL
menu = ["Login", "Cadastro", "Sair"] if st.session_state.logado else ["Login", "Cadastro"]
escolha = st.sidebar.selectbox("📋 Menu", menu)

# CADASTRO
if escolha == "Cadastro":
    st.title("📋 Criar Conta")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        if cadastrar_usuario(usuario, senha):
            st.success("✅ Cadastro realizado com sucesso! Faça login.")
        else:
            st.error("❌ Usuário já existe.")

# LOGIN
elif escolha == "Login":
    if not st.session_state.logado:
        st.title("🔐 Login")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if verificar_login(usuario, senha):
                st.success(f"✅ Bem-vindo, {usuario}!")
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.rerun()
            else:
                st.error("❌ Credenciais inválidas.")
    else:
        # Tela principal do app após login
        st.title("💰 Cotação de Moedas e Ações")
        simbolo = st.text_input("🔍 Digite o código da ação ou moeda (ex: AAPL, BTC, PETR4.SA)")
        if st.button("Buscar Cotação"):
            resultado = buscar_cotacao(simbolo.upper())
            if resultado:
                st.session_state.historico.append(simbolo.upper())
                st.success(f"💹 Resultado para {simbolo.upper()}")
                st.json(resultado)

                # Gráfico histórico (últimos 30 dias)
                st.subheader("📈 Gráfico de variação (últimos dias)")
                historico = buscar_historico(simbolo.upper())
                if historico is not None:
                    fig, ax = plt.subplots()
                    ax.plot(historico.index, historico['4. close'], marker='o', linestyle='-')
                    ax.set_title(f"{simbolo.upper()} - Últimos dias")
                    ax.set_xlabel("Data")
                    ax.set_ylabel("Preço (fechamento)")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)
                else:
                    st.info("⚠️ Histórico não disponível para esse símbolo.")
            else:
                st.error("❌ Símbolo inválido ou erro na API.")

        # Histórico de buscas
        if st.session_state.historico:
            st.subheader("🕘 Histórico de Buscas (Sessão)")
            for item in reversed(st.session_state.historico[-5:]):
                st.write(f"🔸 {item}")

# LOGOUT
elif escolha == "Sair":
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.historico = []
    st.success("🚪 Logout realizado com sucesso.")

# Rodapé
    st.markdown("---")
    st.markdown("Desenvolvido para a disciplina de Desenvolvimento rápido de aplicações em python - Projeto da Faculdade 🧠")

