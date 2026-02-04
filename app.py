from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Simulation d'une base de données
users_db = [
    {"id": 1, "name": "Karima", "role": "Admin Cloud"},
    {"id": 2, "name": "Imane", "role": "DevOps Engineer"}
]

@app.route('/')
def home():
    return jsonify({
        "projet": "API Cloud Advanced v2",
        "equipe": ["Karima", "Imane"],
        "status": "Online",
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({"count": len(users_db), "results": users_db})

@app.route('/api/info')
def info():
    # Cette route montre que tu maîtrises les infos système du Cloud
    return jsonify({
        "environment": "Docker Container",
        "platform": "SnapDeploy Cloud",
        "port": 5000
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
