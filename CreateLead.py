import os
from fastapi import FastAPI,Form
import requests
import json
from typing import Annotated
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']
WMIDFIELD = os.environ['WMIDFIELD'] #WMID USER FIELD
TS_ID = os.environ['TS_ID'] #TRACKING_SOURCE_ID

@app.post("/addlead/")
def read_root(NAME:Annotated[str, Form()],
              PHONE:Annotated[int, Form()],
              WMID: Annotated[str | None = None, Form()],COMMENT: Annotated[str | None = None, Form()],
              UTM_SOURCE: Annotated[str | None = None, Form()],UTM_MEDIUM:Annotated[str | None = None, Form()],UTM_CAMPAIGN:Annotated[str | None = None, Form()],UTM_CONTENT:Annotated[str | None = None, Form()],UTM_TERM:Annotated[str | None = None, Form()]
              ):
    lead_data = {'fields':{
            'TITLE':str(EMOJI + NAME),
            'NAME': NAME,
            "STATUS_ID": "NEW",
            "ASSIGNED_BY_ID ":"36",
            "SOURCE_ID": SOURCE_ID,
            "TRACKING_SOURCE_ID": TS_ID,
            "PHONE": [{ "VALUE": PHONE,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
            'UTM_SOURCE': UTM_SOURCE,
            'UTM_MEDIUM':UTM_MEDIUM,
            'UTM_CAMPAIGN':UTM_CAMPAIGN,
            'UTM_CONTENT':UTM_CONTENT,
            'UTM_TERM':UTM_TERM,
            'COMMENTS':COMMENT,
            WMIDFIELD: WMID  
        }}
    response = requests.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
    print(response)
    answ = json.loads(response.text)
    return {"data": answ['result']}




