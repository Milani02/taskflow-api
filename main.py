from fastapi import FastAPI, HTTPException
from models import Task, Priority

app = FastAPI(title="TaskFlow API")

# Banco de dados temporário (em memória)
db_tasks = []

@app.get("/")
def home():
    return {"mensagem": "TaskFlow API ativa! Acesse /docs para a documentação."}

@app.post("/tasks/", status_code=201)
def criar_tarefa(task: Task):
    # Verifica se o ID já existe
    if any(t.id == task.id for t in db_tasks):
        raise HTTPException(status_code=400, detail="Já existe uma tarefa com este ID.")
    
    db_tasks.append(task)
    return {"mensagem": "Tarefa criada com sucesso!", "tarefa": task}

@app.get("/tasks/")
def listar_tarefas():
    return db_tasks

@app.delete("/tasks/{task_id}")
def deletar_tarefa(task_id: int):
    for index, task in enumerate(db_tasks):
        if task.id == task_id:
            db_tasks.pop(index)
            return {"mensagem": f"Tarefa {task_id} removida."}
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")