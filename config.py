# chatbot.py
from huggingface_hub import InferenceClient
import textwrap

def get_mistral_answer(HF_token, question):
    """
    Function to get a response from the Mistral model.
    """
    client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.3", token=HF_token)
    
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': question}
    ]
    
    result = client.chat_completion(
        messages=messages,
        max_tokens=200,
        temperature=0.3
    )
    
    words = textwrap.fill(result.choices[0].message.content.strip(), width=80)
    return words