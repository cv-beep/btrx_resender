import os
from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']

class Item(BaseModel):
    NAME: str
    PHONE: int
    COMMENT: str
    RECORD: str
  
@app.post("/addlead/")
def read_post_root(item: Item):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + item.NAME),
            'NAME': item.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "PHONE": [{ "VALUE": item.PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.COMMENT
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}

@app.get("/addlead/")
def read_get_root(item: Item):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + item.NAME),
            'NAME': item.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "PHONE": [{ "VALUE": item.PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'COMMENTS': item.COMMENT
        }}
    print(f'send data ={lead_data}')
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}
