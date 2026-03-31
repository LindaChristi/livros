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
