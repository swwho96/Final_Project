import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templete = Jinja2Templates(directory="templetes")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port="0808", reload=True)