from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Hello, Docker!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
