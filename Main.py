from fastapi import FastAPI

app = FastAPI()


@app.get("/helloword")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste01():
    return {"teste": "Ooow deu certo"}

