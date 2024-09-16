from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/teste")
async def funcaoteste01():
    return {"teste": "Ooow deu certo"}

