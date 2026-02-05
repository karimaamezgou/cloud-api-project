# 1. Utiliser une version légère de Python
FROM python:3.9-slim
# 2. Créer un dossier "app" dans l'ordinateur virtuel
WORKDIR /app
# 3. Copier la liste de courses et l'installer
COPY requirements.txt .
RUN pip install -r requirements.txt
# 4. Copier ton code dans la boîte
COPY app.py .
COPY templates/ ./templates/
# 5. Dire que l'app utilise le port 5000
EXPOSE 5000
# 6. La commande pour démarrer l'API
CMD ["python", "app.py"]
