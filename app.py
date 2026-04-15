from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Mon App Docker - Port 5001</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #282c34; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: #20232a; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); text-align: center; border-top: 4px solid #fbbc05; }
            h1 { color: #fbbc05; margin-bottom: 1rem; }
            p { font-size: 1.2rem; line-height: 1.5; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Déploiement sur Port 5001</h1>
            <p>Bonjour à tous,<br><br>Ceci est une simple application conteneurisée avec Docker par <strong>Yopa Tankoua Edmond Raoul</strong> !</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Changement du port interne de 5000 vers 5001
    app.run(host='0.0.0.0', port=5001)