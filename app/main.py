from fastapi import FastAPI


app = FastAPI()

# HTTP GET
@app.get("/")
def home_view():
    return {"hello": "world"}

# HTTP POST
@app.post("/")
def home_detail_view():
    return {"hello": "world"}
