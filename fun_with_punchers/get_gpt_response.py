import openai
import os
import testing_get_nft_info

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

    print()
    print()
    print(response)
    print()
    print()
    print()
    print(vars(response))
    return response.choices[0].text.strip()


def generate_image(prompt):
    print()
    print(f"Img (Dalle-E) generation prompt is: {prompt}")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )

    print()
    print()
    print(response)
    print()
    print()
    print()
    print(vars(response))
    image_url = response['data'][0]['url']

fighter_one_token_id = 4915
fighter_one_info = testing_get_nft_info.get_puncher_info(fighter_one_token_id, 'Ninja')
print(fighter_one_info)

fighter_two_token_id = 3825
fighter_two_info = testing_get_nft_info.get_puncher_info(fighter_two_token_id, 'TNG')
print(fighter_two_info)

text_prompt = f"Describe an epic battle between two gladiators. Only one victor should remain standing at the end and it should be random which gladiator that is. Here is a description of gladiator 1: {fighter_one_info}. Here is a description of gladiator 2: {fighter_two_info}."
print(text_prompt)
story = generate_text(text_prompt)
print()
print()
print()
print()
print()
print(story)

img_prompt = f"A hyper-realistic detailed painting of an epic battle between two gladiators in medieval arena. Gladiator one named {fighter_one_info}. Gladiator two named {fighter_two_info}."
image = generate_image(img_prompt)
print(image)
