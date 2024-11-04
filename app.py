from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Funksjon for å lese brukere fra JSON-filen
def load_users():
    with open("users.json") as f:
        return json.load(f)

@app.route("/")
def index():
    # Render innloggingssiden
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    # Hent JSON-data fra forespørselen
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Les brukere fra JSON-fil
    users = load_users()
    
    # Sjekk om brukeren finnes
    user = next((user for user in users if user["username"] == username and user["password"] == password), None)
    
    if user:
        # Returner suksessmelding hvis brukeren finnes
        return jsonify({"message": "Du er logget inn!"}), 200
    else:
        # Returner feilmelding hvis brukeren ikke finnes
        return jsonify({"message": "Feil brukernavn eller passord."}), 401

if __name__ == "__main__":
    # Start Flask-applikasjonen i debug-modus
    app.run(debug=True)