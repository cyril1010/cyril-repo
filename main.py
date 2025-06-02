from fastapi import FastAPI

app1 = FastAPI(title="My FastAPI App!!!")




@app1.get('/hello')
def say_hi():
  return 'Hello from the edited copy'
