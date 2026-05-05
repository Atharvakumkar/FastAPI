from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

logs = []

class Log(BaseModel):
    source: str
    message: str
    severity: str

@app.post("/logs")
def add_log(log: Log):
    logs.append(log)
    return {"message" : "Log added", "log" : log}

if __name__ == "__main__":
    uvicorn.run("post:app", reload=True)