import json

import requests
import simpleaudio


def text_2_wav(text, speaker_id=0, max_retry=20, filename='audio.wav'):
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


if __name__ == '__main__':
    
    filename = 'audio.wav'  # 音声データのファイル名
    text_2_wav('今日も、元気です！', filename=filename)
    play_auido_by_filename(filename)
