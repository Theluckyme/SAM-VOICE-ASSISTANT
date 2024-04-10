from take_command import speak
from openai import OpenAI

def ai(query):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": query},
       
      ],
      temperature=1,
      max_tokens=50
    )

    result=completion.choices[0].message.content

    print(result)
    speak(result)