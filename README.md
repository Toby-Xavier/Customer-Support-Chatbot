SMART CUSTOMER SUPPORT CHATBOT
=================================================

This is a prompt-engineered customer support chatbot built using Python and Azure OpenAI. The chatbot is designed to answer customer questions accurately and safely by relying strictly on company-provided information, with strong controls to prevent hallucinations.

This project is built to demonstrate the importance of practical prompt engineering.

-------------------------------------------------
PROJECT OVERVIEW
-------------------------------------------------
The Smart Customer Support Chatbot simulates a first-level customer support agent for a Nigerian fintech company (ZeniPay Technologies Ltd).

The chatbot:
- Answers customer questions using only approved company information
- Refuses to answer questions outside its knowledge base
- Maintains a professional and customer-friendly tone
- Prevents hallucinations through strict prompt constraints

This project focuses on PROMPT DESIGN and AI INTEGRATION rather than model training.

-------------------------------------------------
KEY FEATURES
-------------------------------------------------
- Role-based system prompting
- Strict grounding using external company knowledge
- Explicit refusal patterns for unsupported queries
- Low-temperature configuration to reduce hallucinations
- Azure OpenAI deployment-based model usage
- Simple and clear Python implementation

-------------------------------------------------
TECH STACK
-------------------------------------------------
- Python 3
- Azure OpenAI
- GPT-4o-mini (via Azure deployment)
- openai Python SDK
- python-dotenv
- VS Code

-------------------------------------------------
PROJECT STRUCTURE
-------------------------------------------------
customer-support-chatbot/
│
├── app.py                # Main chatbot application
├── prompts.py            # Prompt templates (system + user)
├── company_info.txt      # Grounding knowledge for the chatbot
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not committed)
└── README.txt            # Project documentation

-------------------------------------------------
HOW IT WORKS
-------------------------------------------------
1. Company information is stored in a plain text file (company_info.txt).
2. A detailed system prompt defines the chatbot’s role, rules, and behavior.
3. User questions are combined with the company information and passed to Azure OpenAI.
4. The model generates responses strictly based on the provided information.
5. If a question cannot be answered using the company data, the chatbot responds with a safe refusal.

-------------------------------------------------
PROMPT ENGINEERING STRATEGY
-------------------------------------------------
The chatbot uses a carefully designed system prompt that enforces:

- Explicit role definition (customer support agent)
- Hard constraints on allowed information
- Clear refusal behavior for unknown or unsupported queries
- Controlled tone and response formatting
- Safety rules to avoid assumptions or regulatory claims

This approach ensures reliable, enterprise-grade behavior suitable for real customer-facing systems.

-------------------------------------------------
SETUP INSTRUCTIONS
-------------------------------------------------

1. Clone the repository
   git clone <your-repo-url>
   cd smart-chatbot

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate   (Mac/Linux)
   venv\Scripts\activate      (Windows)

3. Install dependencies
   pip install -r requirements.txt

4. Create a .env file in the project root with the following values:

   AZURE_OPENAI_ENDPOINT=https://YOUR-RESOURCE-NAME.openai.azure.com/
   AZURE_OPENAI_KEY=your_api_key_here
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   AZURE_OPENAI_API_VERSION=2024-02-15-preview

5. Run the chatbot
   python app.py

-------------------------------------------------
EXAMPLE QUESTIONS
-------------------------------------------------
Supported:
- What are your support hours?
- What is the transaction limit for Level 2 KYC?
- Which banks are supported?
- Is there a fee for bank transfers?

Unsupported (correctly refused):
- Can I send money to Ghana?
- Do you offer crypto services?
- Is ZeniPay licensed by the CBN?
- How can I bypass KYC?

-------------------------------------------------
MODEL USAGE
-------------------------------------------------
This project uses Azure OpenAI deployments rather than hard-coded model names.

Recommended models:
- GPT-4o
- GPT-4o-mini

The prompt design is model-agnostic and compatible with future GPT upgrades.

-------------------------------------------------
DISCLAIMER
-------------------------------------------------
ZeniPay Technologies Ltd is a fictional company created solely for demonstration and educational purposes.
