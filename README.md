# 🚀 KING Flask App - Dockerisé

Une simple application Flask conteneurisée avec Docker, créée par **Ali**.

## 📦 Fonctionnalité

- Flask app simple
- Dockerisé avec `Dockerfile`
- Déployable facilement

## 📂 Structure

```bash
KING-flask-app/
│
├── app.py # Code source Flask
├── Dockerfile # Image Docker de l'application
├── requirements.txt # Dépendances Python
├── README.md # Ce fichier
└── cmd_history # Historique des commandes Docker
```

---

## 🛠️ Prérequis

- Docker installé ([télécharger ici](https://www.docker.com/get-started))
- Python (optionnel pour tests locaux)

---

## 🚀 Lancer l’application

### 1. Cloner le projet

```bash
git clone https://github.com/king29k/first-docker.git
cd first-docker.git
```

## 2. Construire l’image Docker

```bash
docker build -t king1-flask-app .
``` 

## 3. Lancer le conteneur

```bash
docker run -d -p 5000:5000 king1-flask-app
```

* Ou, si le port 5000 est déjà utilisé :

```bash
docker run -d -p 5050:5000 king1-flask-app
```

Accéder à l’app via : http://localhost:5000


## 📸 Résultats attendus
* ✅ Application accessible via un navigateur

* ✅ Dockerfile fonctionnel

* ✅ Image pushée sur DockerHub

* ✅ Ce README bien rempli

* ✅ cmd_history contenant les commandes utilisées

* ✅ Capture écran du site et lien fonctionnel

