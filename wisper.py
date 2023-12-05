import os 
import openai
import json

def input_text():
    json_i=open("key.json","r")
    json_road=json.load(json_i)
    openai.api_key = json_road["API Key"]

    with open("./input.wav", "rb") as file:
            
            transcript=openai.Audio.transcribe(
                file=file,
                model='whisper-1',
                response_format='verbose_json',
            )
   # print(transcript["text"])
    return transcript["text"]

