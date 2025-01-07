
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
