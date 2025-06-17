from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        name = request.form["name"]
        education = request.form["education"]
        experience = request.form["experience"]
        skills = request.form["skills"]

        prompt = f"Create a professional resume summary for {name} with the following:\nEducation: {education}\nWork Experience: {experience}\nSkills: {skills}"

        # NEW openai SDK (>=1.0.0) style
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        summary = response.choices[0].message.content.strip()

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
