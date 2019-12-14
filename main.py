from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    trenutni_cas = datetime.datetime.now()
    return f"<h1>Moja prva spletna stran</h1><h2>manjši naslov</h2><p>lorem ipsum</p>{trenutni_cas}"

@app.route("/about")
def on_about():
    # Preberemo datoteko:
    mesta = ["Dunaj", "Gradec", "Trst"]
    return render_template("about.html", page_title="O meni", mesta=mesta)

@app.route("/contact")
def contact():
    # Preberemo datoteko:
    return render_template("contact.html", page_title="Contact")

@app.route("/home")
def home():
    # Preberemo datoteko:
    return render_template("Bootstrap.html")



if __name__== "__main__":
    app.run()