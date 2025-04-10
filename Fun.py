import random
import json

# Load past memories if they exist
try:
    with open("memory_ai.json", "r") as file:
        memory = json.load(file)
except FileNotFoundError:
    memory = []

def transform_memory(input_text):
    poetic_phrases = [
        "A whisper in the wind remembers...",
        "Echoes of a dream left behind...",
        "Like ink on water, the past shifts...",
        "A silent observer keeps watch...",
        "The sky holds its own quiet secrets..."
    ]
    
    transformed = f"{random.choice(poetic_phrases)} {input_text[::-1]}"
    
    # Add to memory
    memory.append(transformed)
    with open("memory_ai.json", "w") as file:
        json.dump(memory, file, indent=2)
    
    return transformed

print("Whisper a memory:")
while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break
    response = transform_memory(user_input)
    print(f"AI: {response}")