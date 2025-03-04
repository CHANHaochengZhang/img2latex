#!/usr/bin/python3
import requests
import base64
import sys
import pandas as pd
# For solve future warning:
# FutureWarning: Passing literal json to 'read_json' is deprecated 
# and will be removed in a future version. To read from a literal 
# string, wrap it in a 'StringIO' object.
from io import StringIO

url = 'http://localhost:11434/api/chat'
img_url = "./uploads/up_file"
    
prompt = "Just formulas, no any others, just give me the latex codes of the formulas in image"

with open(img_url, "rb") as img:
    base64_img = base64.b64encode(img.read()).decode("utf-8")



post_json = {
  "model": "llama3.2-vision",
  "messages": [
    {
      "role": "user",
      "content": prompt,
      "images": [base64_img]
    }
  ]
}

ret = requests.post(url, json = post_json)

# For solve future warning:
# FutureWarning: Passing literal json to 'read_json' is deprecated 
# and will be removed in a future version. To read from a literal 
# string, wrap it in a 'StringIO' object.
df = pd.read_json(StringIO(ret.text), lines=True)

a=""
for json_data in df['message']:
    a+=json_data['content']

print("%s"%(a))

# 没有Mac做不了app，那就用网页
# 可以做个网页应用，拖图片上去，点击就能生成公式