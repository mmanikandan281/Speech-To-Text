# -*- coding: utf-8 -*-
"""Speech To Text.ipnb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lNx2Qgk3kVOGHjjGrJhYgYkLD61DiXFY
"""

pip install openai==0.28

import os
import openai

from google.colab import userdata
OPENAI_API_KEY = userdata.get('OpenAi')

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
openai.api_key = os.getenv('OPENAI_API_KEY')

from google.colab import files
uploaded = files.upload()

for filename in uploaded.keys():
  with open(filename, 'rb') as audio_file:
    transcription = openai.Audio.transcribe(
        model = 'whisper-1',
        file=audio_file,
        response_format='text'
        )
    print("Transcription",transcription)

def summarize_text(text):
  response = openai.ChatCompletion.create(
      model = 'gpt-3.5-turbo',
      messages=[
         {"role":"user","content":f"summarize the following text:{text}"}
      ],
      max_tokens=50
  )
  return response['choices'][0]['message']['content']

summary=summarize_text(transcription)
print("\nSummary:")
print(summary)