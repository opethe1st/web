from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"msg": "Welcome to this app"}


def main():
    uvicorn.run(app)
