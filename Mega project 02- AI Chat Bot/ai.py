from openai import OpenAI

def ai(text):
    client = OpenAI(api_key="***********************")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named vishal who speaks hindi as well as english. he is from india and he is a coder. you analyse chat history and respond as vishal"},
        {"role": "user", "content": text}
    ]
)
    return (completion.choices[0].message.content)