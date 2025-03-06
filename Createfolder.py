import os

from fastapi import FastAPI
import requests
import json
app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']



@app.post("/createfolder/")
def read_root(NAME:str,
              PARENTFOLDERID: int,
              DEALID: int,
              FIELDUPDATE: str
              ):
    inp_data = {'id':PARENTFOLDERID,'data':{'NAME': NAME}}
    
    response = requests.post(str(f'{URLBITRIX}/disk.folder.addsubfolder.json'), json=inp_data)
    print(response)
    answ = json.loads(response.text)
    deal_upd = {'id':DEALID,'fields':{'UF_CRM_DISK_URL':answ['DETAIL_URL']}}
    response = requests.post(str(f'{URLBITRIX}/crm.deal.update'), json=deal_upd)
    return {"data": answ['DETAIL_URL']}

#disk.folder.addsubfolder.json?id=5271&data[NAME]=ТЕстов
