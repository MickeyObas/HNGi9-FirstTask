from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel # Might not need this for now.
import schemas

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def get_profile():
    return {"slackUsername": "MickeyTheBrave",
            "backend": True,
            "age": 21,
            "bio": "I'm a third year Computer Science undegraduate here at FUTA. When i'm not geeking out over tech stuff, i enjoy watching anime, playing football, playing videogames and so much more! Looking forward to making more friends here. Ikuzoo!"}


@app.post("/calculate/", response_model=schemas.Output)
def calculate(Input: schemas.Input):
    input_request = Input.dict()
    operation_type = input_request['operation_type']

    x = input_request['x']
    y = input_request['y']

    if operation_type in ["addition", "subtraction", "multiplication"]:
        if operation_type == "addition":
            result = x + y
        elif operation_type == "subtraction":
            result = x - y
        else:
            result = x * y 
        
        output = {
            "slackUsername": "MickeyTheBrave",
            "result": result,
            "operation_type": operation_type
        }
        
        return output

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid operation. I don't catch what '{}' means.".format(operation_type))
    


