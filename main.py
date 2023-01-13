from fastapi import FastAPI


app= FastAPI()
@app.get("/")
def hello_alnafi_students():
    return "I am a student of DevOps"