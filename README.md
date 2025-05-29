<font size="7">**API Escolar com Flask + SQLAlchemy**</font>


Esta API foi desenvolvida para facilitar o registro e gerenciamento de atividades escolares. Com ela, professores e administradores podem criar, consultar, listar e registrar  as atividades realizadas por estudantes. A API foi construída utilizando o framework Flask, seguindo boas práticas de desenvolvimento para garantir performance e segurança.

_____________________________________________________________________________________________________________________________________________
**Principais Funcionalidades**

Registro de atividades: Permite o cadastro de atividades realizadas pelos alunos.

Buscar atividades: Oferece endpoints para buscar registros de atividades pelo id.

Listar atividade: Facilita a procura de atividade atraves de listas.

Instruções de Execução (com Docker)

**Pré-requisitos:**

Certifique-se de ter o Docker e Docker Compose instalados em sua máquina.
____________________________________________________________________________________________________________________________________________
![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Clone o repositório:

git clone <(https://github.com/Rafaelawr/Atividades.git)>

Acesse a API:
### Pré-requisitos

- Python 3.10 ou superior
- `pip`
- Virtualenv (opcional)

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Rodar a aplicação local

```bash
python app.py
```
Após a inicialização, a API estará disponível em http://localhost:5000.


![image](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) 
## 🐳 Rodando com Docker localmente

### 1. Build da imagem

```bash
docker build -t flask-api .
```

### 2. Rodar o container

```bash
docker run -p 5000:5000 flask-api
```


____________________________________________________________________________________________________________________________________________
**Explicação da Arquitetura**

A API segue uma arquitetura RESTful, com separação clara entre os recursos e suas respectivas operações CRUD. Os principais componentes são:


![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
Flask: Utilizado como framework web para gerenciar requisições HTTP e lógica de negócios.


![image](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
SQLAlchemy: Gerencia o acesso ao banco de dados relacional, permitindo mapeamento objeto-relacional (ORM).

Blueprints: Modularizam os endpoints, organizando o código por funcionalidades (e.g., atividades, usuários).

____________________________________________________________________________________________________________________________________________
**Descrição do Ecossistema de Microsserviços**

A solução foi projetada para ser escalável, utilizando um ecossistema de microsserviços. Os principais serviços e suas integrações são:
____________________________________________________________________________________________________________________________________________
**Serviço de Registro de Atividades:**

Responsável pela lógica central da API.

Integra-se com o banco de dados para armazenar e recuperar informações.
____________________________________________________________________________________________________________________________________________

**Banco de Dados:**

Relacional com suporte a consultas complexas e alta performance.

Conectado a todos os serviços que necessitam persistir dados.
____________________________________________________________________________________________________________________________________________
**Integrações**

Comunicação: Os serviços se comunicam utilizando APIs RESTful e autenticação via JWT.

Mensageria: Para eventos assíncronos, utiliza-se um sistema de filas para garantir resiliência e escalabilidade.


Grupo 9

Alessandra F Rigonatti RA: 2401151 Eduardo Nunes RA:2401234 Rafaela Wohlers Rodrigues- RA: 2404142 Thainá Foltran de Lima - RA:2401219 Vinicios de Lima Basteiro       	  - 2402096

