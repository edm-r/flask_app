# Utilisation de l'image officielle Python comme base
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier des dépendances
COPY requirements.txt /app/

# Installation des dépendances
RUN pip install -r requirements.txt

# Copie des fichiers de l'application dans l'image
COPY app.py /app/

# Définition de la commande de lancement
CMD ["python", "app.py"]
