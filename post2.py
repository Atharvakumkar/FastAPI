from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uuid
import uvicorn

app = FastAPI()

logs = []

class Logs(BaseModel):
    source: str
    message: str
    severity: str

@app.post("/logs2")
def add_logs(log: Logs):
    new_log = {
        "id": str(uuid.uuid4()),
        "source": log.source,
        "message": log.message,
        "severity": log.severity,
        "timestamp": datetime.now(),
    }

    logs.append(new_log)

    return {
        "message" : "Log added successfully",
        "log" : new_log,
    }

if __name__ == "__main__":
    uvicorn.run("post2:app", reload=True)