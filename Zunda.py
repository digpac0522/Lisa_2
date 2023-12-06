import openai

import json

import requests
import simpleaudio



json_i=open("key.json","r")
json_road=json.load(json_i)

openai.api_key = json_road["API Key"]

def chat_with_gpt(prompt,chara):
    chara.append({"role":"user","content":prompt})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=chara
    )
    chara.append({"role":"system","content":response.choices[0].message.content.strip()})

    return response.choices[0].message.content.strip(),chara

def text_2_wav(text, speaker_id=3, max_retry=20, filename='audio.wav'):
    #creat quer
    query_payload = {"text": text, "speaker": speaker_id}
    for query_i in range(max_retry):
        response = requests.post("http://localhost:50021/audio_query",
                                 params=query_payload,
                                 timeout=30)
        if response.status_code == 200:
            query_data = response.json()
            break
    else:
        raise ConnectionError('error ')

    #creait file and save wav
    synth_payload = {"speaker": speaker_id}
    for synth_i in range(max_retry):
        response = requests.post("http://localhost:50021/synthesis",
                                 params=synth_payload,
                                 data=json.
                                 dumps(query_data),
                                 timeout=30)
        if response.status_code == 200:
            open(filename, "wb").write(response.content)
            #print(response.content)
            break
    else:
        raise ConnectionError("error")


def play_auido_by_filename(filename):
    # exe
    wav_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    play_obj.wait_done()


def mon(user_input,chara):
    #txt=open("test.txt") r
    
    #chara=[{"role":"system","content":txt.read()}] r
    
    #print(chara)
    #print(type(chara))
    """
    if user_input.lower() in ["quit", "exit", "bye"]:
        break 
    """

    response,chara = chat_with_gpt(user_input,chara)
    filename = 'audio.wav'  
    text_2_wav(response, filename=filename)
    play_auido_by_filename(filename)
    
    return chara
