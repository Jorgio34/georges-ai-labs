from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add your code below
sign_your_name = 'Jonathan Piatchou'
model = 'gpt-3.5-turbo'  
options = {
    'temperature': 0.7,
    'max_tokens': 150,
    'top_p': 0.9,
    'frequency_penalty': 0.5,
    'presence_penalty': 0.5,
    'seed': seed(sign_your_name)
}
messages = []

# Chat loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Append user message to messages list
    messages.append({'role': 'user', 'content': user_input})
    
    # Get response from the chat model
    response = chat(model=model, messages=messages, stream=False, options=options)
    
    # Append assistant's response to messages list
    messages.append({'role': 'assistant', 'content': response['content']})
    
    # Print assistant's response
    print(f"Assistant: {response['content']}")
    
    # Check for exit condition
    if user_input.lower() == '/exit':
        break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
    file_string  = ''
    file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
    file_string += f'Model: {model}\n'
    file_string += f'Options: {options}\n'
    file_string += pretty_stringify_chat(messages)
    file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
    f.write(file_string)
