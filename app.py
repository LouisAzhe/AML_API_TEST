# -*- coding:utf-8 _*-
"""
# author : Azhe
# github : https://github.com/LouisAzhe
# time: 2022/7/20 p.m 11:59
# file: app.py
"""
import uvicorn
from fastapi import FastAPI, File, Request
from starlette.responses import FileResponse,Response
import os
import time

app = FastAPI()
@app.get("/",tags=['Test'])
def Hello():
    return{"status":200}

@app.post("/name/",tags=['AML新聞查詢'], response_description='xlsx')
async def ReturnExcel(Name:str):
    print(Name)
    try:
        os.remove(Name+'.xlsx')
    except OSError as e:
        print(e)
    return FileResponse(Name+'.xlsx', filename=Name+'.xlsx')

if __name__ == '__main__':
    uvicorn.run(app="app:app", host="0.0.0.0", port=5678, reload=True, debug=True , log_config="uvicorn_config.json")
