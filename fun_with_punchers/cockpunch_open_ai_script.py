import inspect
import os
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
import open_ai_client
import eth_node_client

def create_story_and_image(token_id_one, name_one, token_id_two, name_two):
    fighter_one_info = eth_node_client.get_puncher_info(token_id_one, name_one)
    print(f"Gladiator 1 info: {fighter_one_info}")

    fighter_two_info = eth_node_client.get_puncher_info(token_id_two, name_two)
    print(f"Gladiator 2 info: {fighter_two_info}")

    text_prompt = f"Describe an epic battle between two gladiators. Only one victor should remain standing at the end and it should be random which gladiator that is. Here is a description of gladiator 1: {fighter_one_info}. Here is a description of gladiator 2: {fighter_two_info}."
    story = open_ai_client.generate_text(text_prompt)
    print()
    print(story)

    print()
    print()

    img_prompt = f"A hyper-realistic detailed painting of an epic battle between two gladiators in medieval arena. Gladiator one named {fighter_one_info}. Gladiator two named {fighter_two_info}."
    image = open_ai_client.generate_image(img_prompt)
    
    print()
    print(image)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python cockpunch_open_ai_script.py <token_id1> <name1> <token_id2> <name2>")
        sys.exit(1)

    token_id1 = int(sys.argv[1])
    name1 = sys.argv[2]
    token_id2 = int(sys.argv[3])
    name2 = sys.argv[4]
    create_story_and_image(token_id1, name1, token_id2, name2)
