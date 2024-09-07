import anthropic
import argparse

# Initialize the Anthropic client
client = anthropic.Client(api_key='your_anthropic_api_key_here')  # Replace with your actual API key

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
    response = client.completions.create(
        model="claude-v1",  # Replace with the specific model version if necessary
        prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
        max_tokens_to_sample=300
    )
    
    # Extract the LLM's response
    return response['completion']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='Text to classify')
    args = parser.parse_args()

    prompt = create_prompt(args.text)
    answer = call_llm(prompt)
    print(answer)
