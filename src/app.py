from fastapi import FastAPI

app = FastAPI()


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


@app.get("/")
def home():
    return {"message": "FastAPI is running"}


@app.get("/add")
def addition(a: int, b: int):
    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": add(a, b)
    }


@app.get("/sub")
def subtraction(a: int, b: int):
    return {
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": sub(a, b)
    }