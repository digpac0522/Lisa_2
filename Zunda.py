import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role":"system","content":"あなたの名前は「ずんだもん」で、あなたは私の友達です。語尾が「のだ」 や「なのだ」や「のか」や「かい？」で終わらなければなりません。敬語は絶対に使ってはいけません。必ず文節の区切りが「のだ」 や「なのだ」や「」で終わらなければなりません。あなたは男の子です。"},{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break 

        response = chat_with_gpt(user_input)
        print("ずんだもん: ", response)