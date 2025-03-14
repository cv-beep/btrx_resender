import os
from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']
WMIDFIELD = os.environ['WMIDFIELD'] #WMID USER FIELD
TS_ID = os.environ['TS_ID'] #TRACKING_SOURCE_ID

class Item(BaseModel):
    NAME: str
    PHONE: int
    COMMENT: str
    RECORD: str
  
@app.post("/addlead/")
def read_root(item: Item):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + NAME),
            'NAME': item.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "PHONE": [{ "VALUE": Item.PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'UTM_SOURCE': UTM_SOURCE,
            'UTM_MEDIUM':UTM_MEDIUM,
            'UTM_CAMPAIGN':UTM_CAMPAIGN,
            'UTM_CONTENT':UTM_CONTENT,
            'UTM_TERM':UTM_TERM,
            'COMMENTS': item.COMMENT,
            WMIDFIELD: WMID  
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}

@app.get("/addlead/")
def read_root(item: Item):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + NAME),
            'NAME': item.NAME,
            "STATUS_ID": "NEW",
            "SOURCE_ID": SOURCE_ID,
            "PHONE": [{ "VALUE": Item.PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'UTM_SOURCE': UTM_SOURCE,
            'UTM_MEDIUM':UTM_MEDIUM,
            'UTM_CAMPAIGN':UTM_CAMPAIGN,
            'UTM_CONTENT':UTM_CONTENT,
            'UTM_TERM':UTM_TERM,
            'COMMENTS': item.COMMENT,
            WMIDFIELD: WMID  
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}
