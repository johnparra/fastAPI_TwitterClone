#python
from typing import List
import json

#python and pydantic
from models import Tweets, User, UserRegister

from fastapi import FastAPI
from fastapi import status, Body


app = FastAPI()

@app.get(
    path="/",
    summary="Get Working Tweets in Home"
)
def home():
    """
    Home

    This api work with tweets

    Not parameters

    Show dictionary with {"tweets":"¡Working!}
    """
    return {
        "tweets": "¡Working!"
    }

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register User",
    tags=["users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup a user

    With this api you can register UserRegister

    Parameters:
        - Request Body with UserRegister like parameter

    Returns:
        - A json with user information without password
            -user_id: UUID
            -email: EmailStr
            -first_name: str
            -last_name: str
            -birth_date: datetime
    """
    with open('users.json', mode="r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login User",
    tags=["users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show List Users",
    tags=["users"]
)
def show_all_users():
    """
    Show all users

    This API show all users in the app

    Parameters:
        -

    Returns:
        This API show all users in the app with the following keys:
            -user_id: uuid
            -email: EmailStr
            -first_name: str
            -last_name: str
            -birth_date: datetime
    """
    with open('users.json', mode='r', encoding='utf-8') as f:
        user_list = json.loads(f.read())
        return user_list

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show One User",
    tags=["users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["users"]
)
def update_a_user():
    pass

#Path Operations => Tweets

@app.get(
    path="/",
    response_model=List[Tweets],
    summary="Show all tweets",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"]
)
def home():
    pass

@app.post(
    path="/post",
    response_model=Tweets,
    summary="Create a tweet",
    status_code=status.HTTP_201_CREATED,
    tags=["Tweets"]
)
def post():
    pass

@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweets,
    summary="Show a tweet",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"]
)
def show_a_tweet():
    pass

@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweets,
    summary="Update a tweet",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"]
)
def update_a_tweet():
    pass

@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweets,
    summary="Delete a tweet",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"]
)
def delete_a_tweet():
    pass