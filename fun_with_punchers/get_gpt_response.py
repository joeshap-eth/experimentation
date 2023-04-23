import openai
import os
import sys
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


def create_story_and_image(token_id_one, name_one, token_id_two, name_two):
    fighter_one_info = testing_get_nft_info.get_puncher_info(token_id_one, name_one)
    print(f"Gladiator 1 info: {fighter_one_info}")

    fighter_two_info = testing_get_nft_info.get_puncher_info(token_id_two, name_two)
    print(f"Gladiator 2 info: {fighter_two_info}")

    text_prompt = f"Describe an epic battle between two gladiators. Only one victor should remain standing at the end and it should be random which gladiator that is. Here is a description of gladiator 1: {fighter_one_info}. Here is a description of gladiator 2: {fighter_two_info}."
    story = generate_text(text_prompt)
    print()
    print(story)

    print()
    print()
    print()
    print()

    img_prompt = f"A hyper-realistic detailed painting of an epic battle between two gladiators in medieval arena. Gladiator one named {fighter_one_info}. Gladiator two named {fighter_two_info}."
    image = generate_image(img_prompt)
    
    print()
    print(image)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python get_gpt_response.py <token_id1> <name1> <token_id2> <name2>")
        sys.exit(1)

    token_id1 = int(sys.argv[1])
    name1 = sys.argv[2]
    token_id2 = int(sys.argv[3])
    name2 = sys.argv[4]
    create_story_and_image(token_id1, name1, token_id2, name2)
