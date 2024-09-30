from fastapi import FastAPI

app = FastAPI()

@app.get('hehe')
async def check_foo():
    return {'message':'app started'}