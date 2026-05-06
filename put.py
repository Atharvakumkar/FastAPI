from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

logs = [
    {"source" : "server1",
     "message" : "Login Successful",
     "severity" : "low"}
]

class Log(BaseModel):
    source: str
    message: str
    severity: str

@app.put("/logs/{index}")
def update_log(index: int, log: Log):
    if index < len(logs):
        logs[index] = log.dict()
        return {"message" : "Log Updated", "log" : logs[index]}
    return {"error" : "Log Not Found"}

if __name__ == "__main__":
    uvicorn.run("put:app", reload=True)