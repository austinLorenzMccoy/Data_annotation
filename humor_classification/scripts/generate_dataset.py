import json
import random

def generate_jokes():
    funny_jokes = [
        "Why don't programmers like nature? It has too many bugs!",
        "Why did the function go to therapy? It had too many issues with its parent process.",
        "What's a computer's favorite snack? Microchips!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why did the developer quit his job? Because he didn't get arrays!"
    ]
    
    not_funny_jokes = [
        "The weather is cloudy with clouds today.",
        "I ate a sandwich for lunch.",
        "The tree is brown and has leaves.",
        "My code works, I don't know why.",
        "This is supposed to be funny but isn't."
    ]
    
    dark_humor = [
        "What did the terminal illness say to the doctor? This won't take long.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What's the difference between a developer and a homeless person? The developer has a MacBook.",
        "Debug is like being the detective in a crime movie where you're also the murderer.",
        "My code doesn't have bugs, it has random features."
    ]
    
    offensive_content = [
        "[CONTENT_REMOVED: Inappropriate joke about protected groups]",
        "[CONTENT_REMOVED: Offensive stereotype]",
        "[CONTENT_REMOVED: Inappropriate content]",
        "[CONTENT_REMOVED: Harmful content]",
        "[CONTENT_REMOVED: Offensive material]"
    ]
    
    dataset = []
    id_counter = 1
    
    categories = [
        (funny_jokes, "Funny"),
        (not_funny_jokes, "Not_Funny"),
        (dark_humor, "Dark_Humor"),
        (offensive_content, "Offensive")
    ]
    
    # Generate 100 samples (25 per category)
    for jokes, category in categories:
        base_jokes = jokes * 5  # Repeat base jokes to get 25 samples
        for joke in base_jokes:
            dataset.append({
                "id": id_counter,
                "text": joke,
                "metadata": {
                    "category": category,
                    "length": len(joke),
                    "timestamp": "2025-06-07T10:00:00Z",
                    "source": "synthetic_data"
                }
            })
            id_counter += 1
    
    # Shuffle dataset
    random.shuffle(dataset)
    
    # Save as JSONL
    with open('../data/raw/jokes.jsonl', 'w') as f:
        for item in dataset:
            f.write(json.dumps(item) + '\n')
    
    # Save as CSV
    import pandas as pd
    df = pd.DataFrame(dataset)
    df.to_csv('../data/raw/jokes.csv', index=False)
    
    print(f"Generated {len(dataset)} samples:")
    print(f"- Saved as JSONL: ../data/raw/jokes.jsonl")
    print(f"- Saved as CSV: ../data/raw/jokes.csv")

if __name__ == "__main__":
    generate_jokes()