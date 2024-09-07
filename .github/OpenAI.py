import openai
import argparse

# Initialize the OpenAI client
openai.api_key = ''  # Replace with your actual API key

def create_prompt(text):
    """  
    Create input prompt for LLM.

    Args: 
        text: Text to classify.

    Returns: 
        Prompt for classification.
    """
    instructions = 'Is the sentiment good or bad?'
    formatting = "'positive' or 'negative'"
    return f'Text: {text}\n{instructions}\nAnswer ({formatting}):'

def call_llm(prompt):
    """ 
    Call LLM with input and return the answer.

    Args: 
        prompt: The prompt to send to the LLM.

    Returns: 
        Answer from LLM.
    """
    messages = [
        {'role': 'user', 'content': prompt}
    ]

    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-4"
    )
    
    # Extract the LLM's response from the response dictionary
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='Text to classify')
    args = parser.parse_args()

    prompt = create_prompt(args.text)
    answer = call_llm(prompt)
    print(answer)

