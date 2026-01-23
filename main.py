from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

# Importações dos novos arquivos de infraestrutura
import models
import db_models
from database import engine, get_db

# Cria as tabelas no banco de dados automaticamente ao iniciar
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API - Fase 2 (SQLite)")

@app.get("/")
def home():
    return {"mensagem": "TaskFlow API ativa com persistência! Acesse /docs para testar."}

@app.post("/tasks/", response_model=models.Task, status_code=201)
def criar_tarefa(task: models.Task, db: Session = Depends(get_db)):
    # Verifica se o ID já existe no banco de dados real
    db_task = db.query(db_models.TaskDB).filter(db_models.TaskDB.id == task.id).first()
    if db_task:
        raise HTTPException(status_code=400, detail="Já existe uma tarefa com este ID.")
    
    # Transforma o objeto do Pydantic em um modelo do SQLAlchemy
    nova_tarefa = db_models.TaskDB(
        id=task.id,
        titulo=task.titulo,
        descricao=task.descricao,
        prioridade=task.prioridade.value,
        concluida=task.concluida
    )
    
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa) # Atualiza o objeto com dados do banco (como IDs automáticos)
    return nova_tarefa

@app.get("/tasks/", response_model=List[models.Task])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(db_models.TaskDB).all()

@app.delete("/tasks/{task_id}")
def deletar_tarefa(task_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(db_models.TaskDB).filter(db_models.TaskDB.id == task_id).first()
    
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    
    db.delete(tarefa)
    db.commit()
    return {"mensagem": f"Tarefa {task_id} removida com sucesso do banco de dados."}