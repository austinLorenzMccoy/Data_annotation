# Sentiment & Tone Analysis Project

## Goal
Classify social media texts by sentiment and emotional tone using Label Studio.

## Classification Categories
### Sentiment
- Positive
- Negative
- Neutral

### Tone
- Joyful
- Angry
- Sad
- Sarcastic
- Excited
- None

## Tools Used
- Label Studio
- Python (for data preprocessing)
- Optional: GPT for pre-labeling

## Project Structure
```
sentiment_project/
├── data/
│   └── sentiment_dataset.csv
├── config/
│   └── labeling_config.xml
└── output/
    └── labeled_data.json
```

## Getting Started
1. Install Label Studio: `pip install label-studio`
2. Start Label Studio: `label-studio start`
3. Create new project and import configuration
4. Upload dataset and begin annotation

## Sample Outputs
[Screenshots and examples will be added after annotation]

## Sample Entries with Expected Labels

| Text | Sentiment | Tone |
|------|-----------|------|
| "I love this product! Best decision ever. ❤️" | Positive | Joyful |
| "This is terrible. It ruined my whole day. 😠" | Negative | Angry |
| "Meh. It's okay, nothing special." | Neutral | None |
| "Right, because that's EXACTLY how things work... 🙄" | Negative | Sarcastic |
| "Feeling heartbroken after this disappointing update 💔" | Negative | Sad |

## Annotation Guidelines
- Look for emotional indicators (emojis, punctuation, capitalization)
- Consider context and implicit meaning
- When in doubt about tone, use "None"
- Sarcasm often contains exaggeration or obvious irony