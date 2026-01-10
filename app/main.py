from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ISTOS AI Service running"}
