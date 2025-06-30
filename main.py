from fastapi import FastAPI

app = FastAPI() # Criação da Instância

@app.get("/") # Decorador de rota, que será responsável por tratar as requisições que vão para a rota "/" usando o operador get

