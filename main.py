from fastapi import FastAPI

from pydantic import BaseModel # Might not need this for now.

app = FastAPI()

app.get("/")

@app.get("/profile")
def get_profile():
    return {"slackUsername": "Michael Goke",
            "backend": True,
            "age": 21,
            "bio": "I'm a third year Computer Science undegraduate here at FUTA. When i'm not geeking out over tech stuff, i enjoy watching anime, playing football, playing videogames and so much more! Looking forward to making more friends here. Ikuzoo!"}

