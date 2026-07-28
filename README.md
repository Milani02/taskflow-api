# TaskFlow API

API de gestão de tarefas desenvolvida com Python e FastAPI, focada em organização e produtividade. Construída em etapas para demonstrar a evolução de uma aplicação backend moderna.

## Tecnologias

- **Python** — linguagem principal
- **FastAPI** — framework web de alta performance
- **SQLAlchemy** — ORM para mapeamento e manipulação do banco de dados
- **SQLite** — banco de dados relacional para persistência
- **Pydantic** — validação de dados e schemas
- **Uvicorn** — servidor ASGI

## Como rodar o projeto

```bash
git clone https://github.com/Milani02/taskflow-api.git
cd taskflow-api

python -m venv venv

# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Documentação interativa disponível em `http://127.0.0.1:8000/docs`.

## Evolução do projeto

**Fase 1 — MVP** ✅
- Estrutura base da API e rotas CRUD iniciais
- Armazenamento temporário em memória
- Validação de campos obrigatórios com Pydantic

**Fase 2 — Persistência de dados** ✅
- Implementação do SQLite para armazenamento permanente
- Integração com SQLAlchemy para gestão de modelos de banco de dados
- Regras de negócio, como a proibição de IDs duplicados

**Próximos passos**
- [ ] Fase 3: autenticação JWT para múltiplos usuários
- [ ] Fase 4: containerização com Docker