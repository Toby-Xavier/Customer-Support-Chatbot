# Smart Customer Support Chatbot

A prompt-engineered customer support chatbot built using Python and Azure OpenAI. The chatbot is designed to answer customer questions accurately and safely by relying strictly on company-provided information, with strong controls to prevent hallucinations.

This project demonstrates the importance of practical prompt engineering.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-0078D4.svg)
![GPT-4o](https://img.shields.io/badge/Model-GPT--4o--mini-green.svg)

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Prompt Engineering Strategy](#prompt-engineering-strategy)
- [Setup Instructions](#setup-instructions)
- [Example Questions](#example-questions)
- [Model Usage](#model-usage)
- [Project Structure](#project-structure)
- [Disclaimer](#disclaimer)

## Project Overview

The Smart Customer Support Chatbot simulates a first-level customer support agent for a Nigerian fintech company (**ZeniPay Technologies Ltd**).

### The chatbot:
- ✅ Answers customer questions using only approved company information
- ✅ Refuses to answer questions outside its knowledge base
- ✅ Maintains a professional and customer-friendly tone
- ✅ Prevents hallucinations through strict prompt constraints

**This project focuses on PROMPT DESIGN and AI INTEGRATION rather than model training.**

## Key Features

- **Role-based system prompting**: Defines clear agent behavior and boundaries
- **Strict grounding**: Uses external company knowledge base for accuracy
- **Explicit refusal patterns**: Handles unsupported queries gracefully
- **Low-temperature configuration**: Reduces hallucinations and improves consistency
- **Azure OpenAI deployment**: Enterprise-grade model access
- **Simple implementation**: Clean, maintainable Python code

## Tech Stack

### Core Technologies
- **Python 3.8+**: Core programming language
- **Azure OpenAI**: Enterprise AI platform
- **GPT-4o-mini**: Language model (via Azure deployment)

### Libraries & Tools
- **openai**: Python SDK for Azure OpenAI
- **python-dotenv**: Environment variable management
- **VS Code**: Development environment

## How It Works

```
1. Company Info (company_info.txt) → 2. System Prompt → 3. User Question → 4. Azure OpenAI → 5. Response
```

### Process Flow:

1. **Company information** is stored in a plain text file (`company_info.txt`)
2. A **detailed system prompt** defines the chatbot's role, rules, and behavior
3. **User questions** are combined with the company information and passed to Azure OpenAI
4. The **model generates responses** strictly based on the provided information
5. If a question cannot be answered, the chatbot responds with a **safe refusal**

## Prompt Engineering Strategy

The chatbot uses a carefully designed system prompt that enforces:

| Strategy | Implementation |
|----------|---------------|
| **Role Definition** | Explicit customer support agent identity |
| **Hard Constraints** | Only uses provided company information |
| **Refusal Behavior** | Clear responses for unknown queries |
| **Tone Control** | Professional and customer-friendly language |
| **Safety Rules** | Avoids assumptions or regulatory claims |

This approach ensures **reliable, enterprise-grade behavior** suitable for real customer-facing systems.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Azure OpenAI account with deployment
- API key and endpoint

### Step 1: Clone the Repository
```bash
git clone <https://github.com/Toby-Xavier/Customer-Support-Chatbot/>
cd smart-chatbot
```

### Step 2: Create and Activate Virtual Environment
```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python3 -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
AZURE_OPENAI_ENDPOINT=https://YOUR-RESOURCE-NAME.openai.azure.com/
AZURE_OPENAI_KEY=your_api_key_here
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

### Step 5: Run the Chatbot
```bash
python3 app.py
```

## Example Questions

### Supported Questions (Correctly Answered)
```
- What are your support hours?
- What is the transaction limit for Level 2 KYC?
- Which banks are supported?
- Is there a fee for bank transfers?
```

### Unsupported Questions (Correctly Refused)
```
- Can I send money to Ghana?
- Do you offer crypto services?
- Is ZeniPay licensed by the CBN?
- How can I bypass KYC?
```

The chatbot will politely refuse to answer questions outside its knowledge base, maintaining safety and accuracy.

## Model Usage

This project uses **Azure OpenAI deployments** rather than hard-coded model names.

### Recommended Models:
- **GPT-4o** (Most capable)
- **GPT-4o-mini** (Cost-effective, faster)

The prompt design is **model-agnostic** and compatible with future GPT upgrades.

### Configuration:
```python
response = client.chat.completions.create(
    model=deployment_name,
    messages=[...],
    temperature=0.3,  # Low temperature for consistency
    max_tokens=500
)
```

## Project Structure

```
smart-chatbot/
├── app.py                   # Main application file
├── company_info.txt         # Company knowledge base
├── .env                     # Environment variables (not in repo)
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
```

## Disclaimer

**ZeniPay Technologies Ltd** is a **fictional company** created solely for demonstration and educational purposes.

This project is designed to showcase:
- Prompt engineering best practices
- Safe AI integration patterns
- Enterprise chatbot design
- Grounded response generation

**No real financial services are provided.**
