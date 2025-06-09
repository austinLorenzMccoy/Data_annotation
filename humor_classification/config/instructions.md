# Humor Classification Guidelines

## Labels
- 😄 **Funny**: Content that is genuinely humorous and entertaining
- 😐 **Not Funny**: Content that attempts humor but fails or is neutral
- 😈 **Dark Humor**: Humor involving morbid or serious topics
- ⚠️ **Offensive**: Content that crosses ethical boundaries or is inappropriate

## Guidelines
1. Read the entire text before classifying
2. Consider cultural context
3. If multiple categories apply, choose the most prominent one
4. Mark potentially harmful content as Offensive

# Label Studio Setup Instructions

## Project Description
Project Name: Humor Classification
Version: 1.0
Last Updated: June 7, 2025

This project focuses on classifying text-based jokes and humorous content into four distinct categories. Using Label Studio's annotation interface, annotators will classify content based on humor type, considering factors such as cultural context, offensive content, and dark humor elements.

### Key Features:
- Single-label classification
- Four distinct humor categories
- Real-time annotation interface
- Quality control mechanisms
- Export capabilities for machine learning

### Target Outcomes:
- Create a high-quality labeled dataset for humor classification
- Enable consistent annotation across multiple annotators
- Support development of humor detection models

## Initial Setup
1. Start Label Studio:
```bash
label-studio start
```

2. Access Label Studio at http://localhost:8080
3. Create a new account or login

## Project Creation
1. Click "Create Project"
2. Name: "Humor Classification"
3. Data Import: Select "Upload Data" and choose your jokes dataset
4. Label Config: Copy and paste the following XML:
```xml
<View>
  <Text name="text" value="$text"/>
  <Choices name="humor_type" toName="text" choice="single" showInLine="true">
    <Choice value="Funny" html="😄"/>
    <Choice value="Not_Funny" html="😐"/>
    <Choice value="Dark_Humor" html="😈"/>
    <Choice value="Offensive" html="⚠️"/>
  </Choices>
</View>
```

## Project Settings
1. Go to Project Settings
2. Enable "Show instruction button in Label Stream"
3. Copy content from guidelines.md into instruction field
4. Set "Sampling" to "Sequential"
5. Enable "Show skip button"

## API Key Setup
1. Go to Account & Settings
2. Navigate to Access Token
3. Generate new token
4. Copy token for use in scripts