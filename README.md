# 📚 Sistema de Livros com Django + Docker

Bem-vindo ao **Sistema de Livros**, um projeto acadêmico desenvolvido em **Django** com **PostgreSQL** e **Docker**, seguindo a estrutura e orientações das aulas.

Este sistema permite cadastrar, listar e filtrar livros, oferecendo uma API simples e funcional para gerenciamento de acervo.

---

## 🎯 Tema do Sistema

O tema do sistema é **Gerenciamento de Livros**.  
O objetivo é organizar livros cadastrados em um banco de dados e disponibilizar endpoints para acesso e filtragem via API.

---

## 🛠️ Funcionalidades

O sistema oferece:

- **📗 Cadastro de livros** – Permite incluir novos livros com título, autor, ano, descrição e status;
- **📋 Listagem de livros via API** – Retorna todos os livros cadastrados;
- **🔎 Filtragem de livros lidos** – Permite buscar apenas os livros marcados como lidos.

---

## 🗄️ Dados Armazenados

Cada livro armazena as seguintes informações:

| Campo       | Descrição                                     |
|------------|-----------------------------------------------|
| Título      | Nome do livro                                 |
| Autor       | Nome do autor                                 |
| Ano         | Ano de publicação                             |
| Descrição   | Pequena descrição sobre o livro              |
| Status      | Indica se o livro foi lido, está sendo lido ou deseja ler (`LIDO`, `LENDO`, `QUERO_LER`) |

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11** – Linguagem principal;
- **Django** – Framework web backend;
- **PostgreSQL** – Banco de dados relacional;
- **Docker & Docker Compose** – Containers para ambiente isolado.

---

## 🧩 Estrutura do Projeto

sgta/
├── backend/ # Django app e configuração
│ ├── config/ # Configurações do Django
│ └── livros/ # App de livros (models, views, urls, admin)
├── docker/ # Dockerfile
├── postgres/ # Volume do PostgreSQL
├── docker-compose.yml # Orquestração de containers
├── requirements.txt # Dependências Python
└── README.md # Documentação do projeto

## 📦 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/LindaChristi/livros.git
   cd sgta

2. Suba os containers com Docker Compose:

   docker compose up --build

3. Abra outro terminal para realizar as migrations:

  docker exec -it sgta-web-1 bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  
4. Acesse:
Admin Django: http://localhost:8000/admin
API - todos os livros: http://localhost:8000/api/livros/
API - livros lidos: http://localhost:8000/api/lidos/
