 **TaskFlow API**
API de gestão de tarefas desenvolvida com Python e FastAPI, focada em organização e produtividade. Este projeto foi construído em etapas para demonstrar a evolução de uma aplicação backend moderna.

 **Tecnologias**
Python: Linguagem principal.

FastAPI: Framework web de alta performance.

SQLAlchemy: ORM para mapeamento e manipulação do banco de dados.

SQLite: Banco de dados relacional para persistência de dados.

Pydantic: Validação de dados e Schemas.

Uvicorn: Servidor ASGI.

 **Como rodar o projeto**
Clonar o repositório: git clone https://github.com/SEU_USUARIO/taskflow-api.git

Criar Ambiente Virtual: python -m venv venv

Ativar Ambiente: - Windows: .\venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Instalar Dependências: pip install -r requirements.txt

Executar o Servidor: python -m uvicorn main:app --reload

Documentação Interativa: Aceda a http://127.0.0.1:8000/docs para testar as rotas.

 **Evolução do Projeto**
Fase 1: MVP (Mínimo Produto Viável) ✅
Estrutura base da API e rotas CRUD iniciais.

Armazenamento temporário em memória.

Validação de campos obrigatórios com Pydantic.

Fase 2: Persistência de Dados ✅
Implementação do SQLite para armazenamento permanente.

Integração com SQLAlchemy para gestão de modelos de base de dados.

Implementação de regras de negócio, como a proibição de IDs duplicados.

 **Próximos Passos**
[ ] Fase 3: Implementação de Autenticação JWT (JSON Web Token) para múltiplos usuários.

[ ] Fase 4: Containerização da aplicação utilizando Docker.