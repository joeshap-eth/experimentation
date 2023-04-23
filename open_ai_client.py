import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_text(prompt):
    print()
    print(f"Text (GPT) generation prompt is: {prompt}")
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()


def generate_image(prompt):
    print()
    print(f"Img (Dalle-E) generation prompt is: {prompt}")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )

    return response['data'][0]['url']
