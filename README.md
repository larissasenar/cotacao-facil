# 💰 Cotação Fácil

Um sistema simples e rápido para consultar cotações de **ações e moedas em tempo real**, com login de usuário, gráficos e histórico de buscas. Desenvolvido com Python e publicado na web com Streamlit.

---

## 📌 Funcionalidades

- ✅ Cadastro e login de usuários (com banco de dados local SQLite)
- 📈 Busca de cotações em tempo real via [Alpha Vantage API](https://www.alphavantage.co/)
- 📊 Gráfico com variação de preços
- 🕘 Histórico de buscas da sessão
- 🔐 Logout
- 🌍 Publicado online no Streamlit Cloud

---

## 🖼️ Interface

Acesse agora:  
👉 **[https://cotacao-facil.streamlit.app/](https://cotacao-facil.streamlit.app/)**

---

## ⚙️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – para interface web
- [Alpha Vantage API](https://www.alphavantage.co/) – para dados de mercado
- [SQLite](https://www.sqlite.org/) – banco de dados de usuários
- `requests`, `matplotlib`, `pandas` – bibliotecas auxiliares

---

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cotacao-facil.git
cd cotacao-facil
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o app:
```bash
streamlit run app.py
```

---

## 🧪 Exemplos de códigos para buscar

- Ações brasileiras: `PETR4.SA`, `VALE3.SA`
- Ações americanas: `AAPL`, `TSLA`
- Moedas: `USD/BRL`, `EUR/USD`

---

## 📚 Projeto acadêmico

Este projeto foi desenvolvido como parte da disciplina **Desenvolvimento Rápido de Aplicações com Python**, com foco em aprendizado prático, APIs, deploy e interface de usuário.

---

## 👤 Autoria

Feito por **Larissa Sena**  
Orientado por **Desenvolvimento Rápido de Aplicações com Python**
