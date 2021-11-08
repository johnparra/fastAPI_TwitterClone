from models import User

from fastapi import FastAPI


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