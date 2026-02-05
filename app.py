from flask import Flask, jsonify, render_template
import datetime

app = Flask(__name__)

# Simulation d'une base de données structurée pour les deux modules
users_db = [
    {"id": 1, "name": "Karima", "role": "Admin Cloud"},
    {"id": 2, "name": "Imane", "role": "DevOps Engineer"}
]

@app.route('/')
def home():
    # Cette route affiche ton interface HTML "jolie" située dans /templates
    return render_template('index.html')

@app.route('/api/users')
def get_users():
    # Cette route technique renvoie le JSON (pour prouver que l'API fonctionne)
    return jsonify({
        "status": "success",
        "count": len(users_db),
        "results": users_db,
        "cloud_provider": "SnapDeploy",
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    # Configuration du port 5000 comme détecté par SnapDeploy
    app.run(host='0.0.0.0', port=5000)
