import json
import os
import requests
from typing import Dict

from hoshino import Service
from hoshino.typing import MessageSegment, CQEvent

sv = Service('随机丁真')

# 常量
url = 'https://api.aya1.top/randomdj?r=0'
randomUrl = url + "&g=1"

#返回消息格式
def GetRandomDingzhen(dingzhenJSON: dict) -> str:
    gotPicUrl = dingzhenJSON["url"]
    msg = f'''{MessageSegment.image(gotPicUrl)}'''
    return msg

@sv.on_fullmatch("随机丁真")
async def SentRandomDingzhen(bot, ev: CQEvent):
    try:
        # 获取json字典
        dingzhenJson = requests.get(randomUrl).json()
        # 发送消息
        await bot.send(ev, GetRandomDingzhen(dingzhenJson))
    except:
        await bot.send(ev, "发送失败…")
