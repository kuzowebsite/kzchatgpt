
from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "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"  # Таны API түлхүүрийг энд оруулна уу

app = Flask(__name__)

@app.route("/")
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
    app.run(debug=True)
