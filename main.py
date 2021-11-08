#python
from typing import List

#python and pydantic
from models import Tweets, User

from fastapi import FastAPI
from fastapi import status


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
def signup():
    pass

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
    pass

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