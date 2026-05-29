# 🚀 API Flask + MySQL com Docker (DevOps Project)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Running-success)

---

## 📌 Sobre o Projeto

Este projeto é uma **API REST** desenvolvida em Flask integrada com MySQL, totalmente containerizada com Docker e Docker Compose.

Ele simula um ambiente real de **DevOps**, onde a aplicação e o banco de dados rodam de forma isolada e comunicam entre si via rede Docker.

---

## 🧱 Arquitetura
Usuário ↓ Flask API (Docker) ↓ MySQL Database (Docker) ↓ Docker Network

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11
- Flask
- MySQL 8
- Docker
- Docker Compose

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Nicolasfjj/api-mysql-devops.git
cd api-mysql-devops
2. Subir os containers
Bash
docker compose up -d --build
3. Verificar containers
Bash
docker ps
🌐 Endpoints da API
🔵 Teste da API

GET /
Resposta:
JSON
{
  "msg": "API rodando 🚀"
}
🟢 Criar cliente

POST /clientes
Body:
JSON
{
  "nome": "João",
  "email": "joao@email.com"
}
🟡 Listar clientes

GET /clientes
Resposta:
JSON
[
  {
    "id": 1,
    "nome": "João",
    "email": "joao@email.com"
  }
]
🐳 Docker
Subir ambiente
Bash
docker compose up -d --build
Parar ambiente
Bash
docker compose down
🗄️ Banco de Dados
Tabela utilizada:
SQL
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);
⚠️ Problemas comuns
Porta 5000 em uso
Bash
docker ps
docker stop <container>
Porta MySQL em uso
Altere no docker-compose:
YAML
ports:
  - "3307:3306"
📈 Status do Projeto
✔ API funcionando
✔ Banco conectado
✔ Docker Compose configurado
✔ CRUD básico implementado
🚀 Próximas melhorias
Autenticação JWT
CI/CD com GitHub Actions
Deploy em nuvem (AWS / Render / VPS)
Nginx como reverse proxy
Monitoramento com logs
👨‍💻 Autor
Nicolas Samuel Corrêa Nascimento
Técnico em Informática
