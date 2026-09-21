from dotenv import load_dotenv
import os

from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


response = client.chat.completions.create(

    model="openai/gpt-oss-120b",

    messages=[
        {
            "role":"user",
            "content":"Halo, apakah API berhasil?"
        }
    ]

)


print(
    response.choices[0].message.content
)