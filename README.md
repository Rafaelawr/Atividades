API de Registro de Atividades Escolares

Descrição da API

Esta API foi desenvolvida para facilitar o registro e gerenciamento de atividades escolares. Com ela, professores e administradores podem criar, consultar, atualizar e excluir registros de atividades realizadas por estudantes. A API foi construída utilizando o framework Flask, seguindo boas práticas de desenvolvimento para garantir performance e segurança.

Principais Funcionalidades

Registro de atividades: Permite o cadastro de atividades realizadas pelos alunos.

Consulta de atividades: Oferece endpoints para buscar registros com filtros como aluno, data ou tipo de atividade.

Atualização de registros: Facilita a atualização de informações previamente registradas.

Exclusão de registros: Possibilita a remoção de atividades obsoletas ou incorretas.

Instruções de Execução (com Docker)

Pré-requisitos:

Certifique-se de ter o Docker e Docker Compose instalados em sua máquina.

Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_REPOSITORIO>

(https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) Construa e inicie os serviços com Docker Compose:

docker-compose up --build

Acesse a API:
Após a inicialização, a API estará disponível em http://localhost:5000.

Testes opcionais:
Para executar os testes automatizados:

docker-compose run api pytest

Explicação da Arquitetura

A API segue uma arquitetura RESTful, com separação clara entre os recursos e suas respectivas operações CRUD. Os principais componentes são:

Flask: Utilizado como framework web para gerenciar requisições HTTP e lógica de negócios.

SQLAlchemy: Gerencia o acesso ao banco de dados relacional, permitindo mapeamento objeto-relacional (ORM).

Blueprints: Modularizam os endpoints, organizando o código por funcionalidades (e.g., atividades, usuários).

JWT (JSON Web Tokens): Implementado para autenticação e controle de acesso.

Descrição do Ecossistema de Microsserviços

A solução foi projetada para ser escalável, utilizando um ecossistema de microsserviços. Os principais serviços e suas integrações são:

Serviço de Registro de Atividades:

Responsável pela lógica central da API.

Integra-se com o banco de dados para armazenar e recuperar informações.

Serviço de Autenticação:

Gerencia login e tokens JWT.

Comunica-se com o Serviço de Registro de Atividades para validar permissões.

Serviço de Notificações (opcional):

Envia alertas para alunos ou professores sobre atividades registradas.

Pode ser integrado via filas como RabbitMQ ou Kafka.

Banco de Dados:

Relacional (e.g., PostgreSQL) com suporte a consultas complexas e alta performance.

Conectado a todos os serviços que necessitam persistir dados.

Integrações

Comunicação: Os serviços se comunicam utilizando APIs RESTful e autenticação via JWT.

Mensageria: Para eventos assíncronos, utiliza-se um sistema de filas para garantir resiliência e escalabilidade.



