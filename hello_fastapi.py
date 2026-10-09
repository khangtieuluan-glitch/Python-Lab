from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "hello A->B"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"msg": f"hello {name}"}
