from llm_helper import llm
from fewshot import FewShotPosts
length_options = ["short", "medium", "long"]

few_shot = FewShotPosts()
def get_length_str(length):
    if length == "short":
        return "10 to 50 lines"
    if length == "medium":
        return "50 to 100 lines"
    if length == "long":
        return "100 to 150 lines"
    

def get_prompt(length, language,tag):
    length_str =get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic : {tag}
    2) Length : {length}
    3) Language: {language}
    if Language = Hinglish that means it is a mix of Hindi and english. Otherwise it should always be english if not specified. The script should always be english
    '''

    examples = few_shot.get_filtered_posts(length,language,tag)
    if len(examples)>0:
        prompt += "4) Use the writing style as per the following examples."
        for i,post in enumerate(examples):
            post_text = post['text']
            prompt += "\n\n Example{i+1} \n\n {post_text}"

            if i==1:
                break
    return prompt
    


def generate_post(length, language,tag):
    prompt = get_prompt(length,language,tag)
    response = llm.invoke(prompt)
    return response.content 