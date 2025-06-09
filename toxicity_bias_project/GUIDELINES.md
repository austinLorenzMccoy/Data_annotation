# Annotation Guidelines: Toxicity & Bias Detection

## Overview
This document provides guidelines for annotating text data for toxicity and bias detection. Each text should be labeled for both toxicity and specific types of bias if present.

## Label Categories

### 1. Toxicity Labels (Required)
- **Toxic** [🔴]
  - Harmful, offensive, or aggressive content
  - Personal attacks or insults
  - Threats or hostile language
  - Examples:
    - "You're stupid and worthless"
    - "People like you should die"

- **Non-toxic** [🟢]
  - Neutral or constructive content
  - Respectful disagreement
  - Examples:
    - "I disagree with your perspective"
    - "This policy needs improvement"

### 2. Bias Types (Apply all that match)

- **Gender Bias** [🟧]
  - Stereotypes about gender
  - Discriminatory remarks about gender roles
  - Examples:
    - "Women can't be good leaders"
    - "Men shouldn't show emotions"

- **Racial Bias** [🟣]
  - Racial stereotypes or prejudice
  - Discriminatory comments about ethnicity
  - Examples:
    - "That ethnic group is lazy"
    - "Go back to your country"

- **Religious Bias** [🔵]
  - Religious stereotypes
  - Discrimination based on faith
  - Examples:
    - "That religion promotes terrorism"
    - "People of that faith are all extremists"

- **Political Bias** [🟡]
  - Extreme political prejudice
  - Dehumanizing political opponents
  - Examples:
    - "All [party] voters are traitors"
    - "People with those political views are evil"

## Annotation Rules

1. **Multi-label Approach**
   - Each text MUST have a toxicity label (Toxic or Non-toxic)
   - Apply ALL relevant bias labels that apply
   - A text can have multiple bias types

2. **Context Matters**
   - Consider the full context of the statement
   - Look for implicit bias and subtle toxicity
   - Consider cultural and social context

3. **Edge Cases**
   - Sarcasm: Label based on intended effect
   - Jokes: Consider if they promote harmful stereotypes
   - News quotes: Label the content, not the source

4. **Severity Guidelines**
   - Focus on impact rather than intent
   - Consider both explicit and implicit harm
   - When in doubt, document your reasoning

## Keyboard Shortcuts
- `t`: Toxic
- `n`: Non-toxic
- `g`: Gender Bias
- `r`: Racial Bias
- `l`: Religious Bias
- `p`: Political Bias
- `x`: None

## Quality Control
1. Be consistent in your annotations
2. Document unclear or ambiguous cases
3. Review previous decisions periodically
4. Discuss difficult cases with team members

## Examples with Multiple Labels

1. ```
   Text: "Women can't drive and shouldn't be allowed on the road"
   Labels: [Toxic, Gender Bias]
   ```

2. ```
   Text: "All politicians from Party X are corrupt liars"
   Labels: [Toxic, Political Bias]
   ```

3. ```
   Text: "This community welcomes people of all backgrounds"
   Labels: [Non-toxic, None]
   ```