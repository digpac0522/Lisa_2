import os 
import openai

def input_text():
    openai.api_key  = "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"

    with open("./input.wav", "rb") as file:
            
            transcript=openai.Audio.transcribe(
                file=file,
                model='whisper-1',
                response_format='verbose_json',
            )
   # print(transcript["text"])
    return transcript["text"]

