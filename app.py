from flask import Flask, jsonify

app = Flask(__name__)

# Route de test
@app.route('/health')
def health():
   return jsonify(status="L'API de Karima fonctionne !")

# Route qui affiche la liste des utilisateurs
@app.route('/users')
def users():
   return jsonify(users=["Karima", "Imane", "User1", "User2"])

if __name__ == '__main__':
   # On lance l'app sur le port 5000
   app.run(host='0.0.0.0', port=5000)
