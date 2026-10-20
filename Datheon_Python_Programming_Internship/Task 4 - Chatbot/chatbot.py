import re, json

# Intent Keywords (regex patterns)
INTENT_KEYWORDS = {
    "greeting": [r"\bhi\b", r"\bhello\b", r"\bhey\b"],
    "hours": [r"business hours", r"\bopen\b", r"\bhours\b"],
    "product": [r"\bproduct\b", r"\bprice\b", r"\boffer\b"],
    "contact": [r"\bcontact\b", r"\bsupport\b", r"\bhelp\b"],
    "exit": [r"\bbye\b", r"\bexit\b", r"\bquit\b"]
}

# Responses
RESPONSES = {
    "greeting": "Hello! How can I assist you? Ask about hours, product or contact.",
    "hours": "We are open Mon-Fri, 9 AM to 6 PM IST.",
    "product": "Our Python internship kit is priced at ₹999.",
    "contact": "You can reach support at support@datheon.com.",
    "fallback": "Sorry, I didn't understand. Try asking about 'hours', 'product' or 'contact'."
}

# Load FAQ from JSON (optional)
def load_faq():
    try:
        with open('faq.json', 'r') as f:
            return json.load(f)
    except:
        return {}

FAQ = load_faq()

def get_intent(text):
    text = text.lower()
    for intent, patterns in INTENT_KEYWORDS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                return intent
    return None

def chat():
    print("=== Terminal Assistant (type 'bye/exit/quit' to stop) ===")
    while True:
        user_input = input("\nYou: ").strip()
        intent = get_intent(user_input)
        
        if intent == "exit":
            print("Bot: Goodbye!")
            break
        
        response = RESPONSES.get(intent, RESPONSES["fallback"])
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
