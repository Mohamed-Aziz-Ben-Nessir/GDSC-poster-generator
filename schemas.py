from fastapi import Form, File, UploadFile
from pydantic import BaseModel

class Form(BaseModel):
    title : str
    name1 : str
    pos1 : str
    name2 : str
    pos2 : str
    date : str
    time : str
    location : str
    pic1 : UploadFile
    pic2 : UploadFile

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        name1: str = Form(...),
        pos1: str = Form(...),
        name2: str = Form(...),
        pos2: str = Form(...),
        date: str = Form(...),
        time: str = Form(...),
        location: str = Form(...),
        pic1: UploadFile = File(...),
        pic2: UploadFile = File(...)
    ):
        return cls(
            title=title,
            name1=name1,
            pos1=pos1,
            name2=name2,
            pos2=pos2,
            date=date,
            time=time,
            location=location,
            pic1=pic1,
            pic2=pic2
        )
