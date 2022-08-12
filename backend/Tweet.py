# -*- coding : utf-8 -*-


from pydantic import BaseModel

# Class qui décrit le tweet
class Tweet(BaseModel):
        tweet : str