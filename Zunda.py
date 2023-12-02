import openai

import json

import requests
import simpleaudio

json_i=open("key.json","r")
json_road=json.load(json_i)

openai.api_key = json_road["API Key"]

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role":"system","content":"あなたの名前は「ずんだもん」で、あなたは私の友達です。語尾は絶対に「なのだ」 や「のだ」や「のか」や「かい？」です。文として絶対に違和感がないように終わらなければなりません。宮城県出身です。敬語は絶対に使ってはいけません。自己紹介はする必要はありませんが尋ねられたら答える必要があります。必ず文節の区切りが「のだ」や「なのだ」で終わらなければなりません。あなたは男の子です。"},{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()

def text_2_wav(text, speaker_id=3, max_retry=20, filename='audio.wav'):
    #creat quer
    query_payload = {"text": text, "speaker": speaker_id}
    for query_i in range(max_retry):
        response = requests.post("http://localhost:50021/audio_query",
                                 params=query_payload,
                                 timeout=10)
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
                                 data=json.dumps(query_data),
                                 timeout=10)
        if response.status_code == 200:
            with open(filename, "wb") as fp:
                fp.write(response.content)
            break
    else:
        raise ConnectionError("error")


def play_auido_by_filename(filename: str):
    # exe
    wav_obj = simpleaudio.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    play_obj.wait_done()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        history=[]
        prompt = "\n".join(history + [user_input])
        if user_input.lower() in ["quit", "exit", "bye"]:
            break 

        response = chat_with_gpt(user_input)
        filename = 'audio.wav'  # 音声データのファイル名
        text_2_wav(response, filename=filename)
        play_auido_by_filename(filename)
