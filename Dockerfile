# Utilisation de l'image officielle Python
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des dépendances et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application
COPY . .

# Exposition du port utilisé par Flask
EXPOSE 5000

# Commande de démarrage de l'application Flask
CMD ["python", "app.py"]
