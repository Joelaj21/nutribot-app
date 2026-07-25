# NutriBot 🥗

An AI-powered meal nutrition analyser that takes a meal description in **English or Malayalam** and returns calories, macros, and a health score — instantly.

🔗 **Live App:** [web-production-c914a.up.railway.app](https://web-production-c914a.up.railway.app)

## What it does

Type in what you ate (e.g. "2 dosa with sambar" or its Malayalam equivalent), and NutriBot uses an LLM to estimate:
- Calories
- Macronutrients (protein, carbs, fat)
- A health score
- Suggestions for a more balanced meal

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Groq API (llama-3.1-8b-instant)
- **Deployment:** Railway

## How to run locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Joelaj21/nutribot-app.git
   cd nutribot-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Groq API key as an environment variable:
   ```bash
   export GROQ_API_KEY=your_key_here
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open `http://localhost:5000` in your browser.

## What I learned

Building NutriBot taught me how to design prompts that reliably return structured JSON output from an LLM, handle bilingual (English/Malayalam) input, and deploy a Flask app to production on Railway.

## Author

**Joel A J** — [GitHub](https://github.com/Joelaj21)
