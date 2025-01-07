
import os
from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "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"  # Таны API түлхүүрийг энд оруулна уу

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if user_message:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        
        bot_message = response["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": bot_message})
    return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    port = os.getenv('PORT', 4000)
    app.run(debug=True, host="0.0.0.0", port=port)
