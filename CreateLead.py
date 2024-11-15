from typing import Union
import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']

class Lead():
    def __init__(self):
        name: str()
        phone: int()
        wmid: int| None = None


@app.post("/addlead/")
def read_root(name:str,
              phone: int,
              wmid: int| None = None,
              UTM_SOURCE: str| None = None,UTM_MEDIUM:str| None = None,UTM_CAMPAIGN:str| None = None,UTM_CONTENT:str| None = None,UTM_TERM:str| None = None
              ):
    lead_data = {'fields':{
            'TITLE':str(EMOJI+name),
            'NAME':name,
            "STATUS_ID": "NEW",
            "ASSIGNED_BY_ID ":"36",
            "SOURCE_ID": SOURCE_ID,
            "TRACKING_SOURCE_ID": 10,
            "PHONE": [{ "VALUE": phone,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'UTM_SOURCE': UTM_SOURCE,
            'UTM_MEDIUM':UTM_MEDIUM,
            'UTM_CAMPAIGN':UTM_CAMPAIGN,
            'UTM_CONTENT':UTM_CONTENT,
            'UTM_TERM':UTM_TERM
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    #msginfo = str(f"Send to bitrix,ok. response: {response} , Name: {NAME},UTM:{UTM}")
    #TelegramMsg(msginfo)
    return {"data": name}