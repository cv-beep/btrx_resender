import os
from fastapi import FastAPI
import requests
import json
import httpx

app = FastAPI()
URLBITRIX = os.environ['URLBITRIX']
EMOJI = os.environ['EMOJI']
SOURCE_ID = os.environ['SOURCE_ID']
WMIDFIELD = os.environ['WMIDFIELD'] #WMID USER FIELD
TS_ID = os.environ['TS_ID'] #TRACKING_SOURCE_ID
def sendWH():
  

html_form = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Форма</title>
  <style>
    body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; }
    form { padding: 20px; border: 1px solid #ccc; border-radius: 10px; }
    input { display: block; margin: 10px 0; padding: 8px; width: 250px; }
    button { padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    button:hover { background: #0056b3; }
  </style>
</head>
<body>
  <form action="/submit" method="post">
    <h3>Оставьте заявку</h3>
    <input type="text" name="name" placeholder="Ваше имя" required>
    <input type="tel" name="phone" placeholder="Телефон" required>
    <button type="submit">Отправить</button>
  </form>
</body>
</html>
"""
@app.get("/", response_class=HTMLResponse)
async def form_page():
    return html_form
  
@app.post("/submit")
async def submit_form(name: str = Form(...), phone: str = Form(...)):
    async with httpx.AsyncClient() as client:
        try:
            lead_data = {'fields':{
              'TITLE':str(EMOJI + name),
              'NAME': name,
              "STATUS_ID": "NEW",
              "ASSIGNED_BY_ID ":"36",
              "SOURCE_ID": SOURCE_ID,
              "TRACKING_SOURCE_ID": TS_ID,
              "PHONE": [{ "VALUE": phone,"VALUE_TYPE": "OTHER","TYPE_ID": "PHONE"}],
              'UTM_SOURCE': UTM_SOURCE,
              'UTM_MEDIUM':UTM_MEDIUM,
              'UTM_CAMPAIGN':UTM_CAMPAIGN,
              'UTM_CONTENT':UTM_CONTENT,
              'UTM_TERM':UTM_TERM,
              'COMMENTS':COMMENT,
              WMIDFIELD: WMID  
          }}
            response = await client.post(str(f'{URLBITRIX}/crm.lead.add.json'), json=lead_data)
          
            response.raise_for_status()
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return {"data": answ['result']}

@app.post("/addlead/")
def read_root(NAME:str,
              PHONE: int,
              WMID: int| None = None,COMMENT: str| None = None,
              UTM_SOURCE: str| None = None,UTM_MEDIUM:str| None = None,UTM_CAMPAIGN:str| None = None,UTM_CONTENT:str| None = None,UTM_TERM:str| None = None
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



