from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return "this is index test page"

@app.get("/root")
def root():
    return "this is root page for test only"