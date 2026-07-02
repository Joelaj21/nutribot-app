import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SYSTEM_PROMPT = """You are NutriBot, a friendly meal nutrition analyser for Kerala, India.
The user may describe their meal in English or Malayalam.
Return ONLY a valid JSON object, no explanation, no markdown, no backticks.
Use this exact structure:
{
  "meal_name": "Short English name",
  "meal_description": "One sentence describing the meal",
  "calories": 0,
  "protein_g": 0,
  "carbs_g": 0,
  "fat_g": 0,
  "fiber_g": 0,
  "health_score": 5,
  "health_score_reason": "One sentence",
  "tip": "One practical tip"
}"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.get_json()
    meal = data.get("meal", "").strip()
    if not meal:
        return jsonify({"error": "Please describe your meal."}), 400
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return jsonify({"error": "API key not configured."}), 500
    try:
        client = Groq(api_key=api_key)
        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Analyse this meal: {meal}"}
            ]
        )
        raw = chat.choices[0].message.content.strip()
        clean = raw.replace("```json", "").replace("```", "").strip()
        nutrition = json.loads(clean)
        return jsonify(nutrition)
    except json.JSONDecodeError:
        return jsonify({"error": "Could not parse data. Try again."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
