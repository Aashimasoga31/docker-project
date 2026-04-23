from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

quotes = {
    "happy": [
        "Happiness is not by chance, but by choice.",
        "Smile, it confuses people.",
        "Enjoy every moment of life."
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "Every storm runs out of rain.",
        "It’s okay to not be okay."
    ],
    "motivated": [
        "Push yourself, no one else will do it for you.",
        "Dream big. Start small. Act now.",
        "Success starts with self-belief."
    ],
    "relaxed": [
        "Slow down and enjoy the moment.",
        "Peace begins with a deep breath.",
        "Relax. Refresh. Restart."
    ]
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Mood Quotes</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            height: 100vh;
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.7)),
                        url('https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d');
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .card {
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 20px;
            width: 400px;
            text-align: center;
            backdrop-filter: blur(15px);
            box-shadow: 0 0 25px rgba(0,0,0,0.5);
        }

        h1 {
            margin-bottom: 20px;
        }

        select {
            padding: 10px;
            border-radius: 10px;
            border: none;
            width: 80%;
            margin-bottom: 20px;
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            background: #ff4081;
            color: white;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background: #f50057;
            transform: scale(1.05);
        }

        .quote {
            margin-top: 25px;
            font-size: 18px;
            font-style: italic;
            color: #ffd;
        }

        .emoji {
            font-size: 30px;
            margin-top: 10px;
        }

        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: #ccc;
        }
    </style>
</head>
<body>

<div class="card">
    <h1>🎭 Mood Quotes</h1>

    <form method="POST">
        <select name="mood" required>
            <option value="">-- Select Mood --</option>
            <option value="happy">😊 Happy</option>
            <option value="sad">😢 Sad</option>
            <option value="motivated">🔥 Motivated</option>
            <option value="relaxed">🌿 Relaxed</option>
        </select>
        <br>
        <button type="submit">Get Quote</button>
    </form>

    {% if quote %}
        <div class="quote">"{{ quote }}"</div>
        <div class="emoji">
            {% if mood == "happy" %} 😊
            {% elif mood == "sad" %} 😢
            {% elif mood == "motivated" %} 🔥
            {% elif mood == "relaxed" %} 🌿
            {% endif %}
        </div>
    {% endif %}

    <div class="footer">Flask + Docker Unique UI ✨</div>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    quote = None
    mood = None

    if request.method == "POST":
        mood = request.form.get("mood")
        quote = random.choice(quotes.get(mood, ["Stay positive!"]))

    return render_template_string(HTML, quote=quote, mood=mood)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)