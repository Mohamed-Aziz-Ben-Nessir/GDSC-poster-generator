import uvicorn
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import Form
from Poster_Maker import make_poster

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
def get_form(request: Request):
   return templates.TemplateResponse("form.html", {"request": request})

@app.post('/', response_class=HTMLResponse)
def post_form(request: Request, form_data: Form = Depends(Form.as_form)):
    make_poster(dict(form_data))
    return templates.TemplateResponse("form.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app) 
