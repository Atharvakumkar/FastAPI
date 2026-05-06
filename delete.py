from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

logs = [
    {"source" : "Server1",
     "message" : "Error Loading data",
     "severity" : "High"}
]

@app.delete("/logs/{index}")
def delete_log(index: int):
    if index < len(logs):
        removed = logs.pop(index)
        return {"message" : "Log Deleted", "log" : removed}
    return {"error" : "Log not found"}

if __name__ == "__main__":
    uvicorn.run("delete:app", reload=True)