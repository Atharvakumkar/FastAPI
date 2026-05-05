import uvicorn
from fastapi import FastAPI

app = FastAPI()

logs = [
    {
        "source" : "server1",
        "message" : "Login Success",
        "severity" : "low"
    },
    {
        "source" : "server2",
        "message" : "Login Failed",
        "severity" : "High"
    },
]

@app.get("/get_logs")
def get_logs():
    return {"logs" : logs}

if __name__ == "__main__":
    uvicorn.run("get:app", reload=True)

