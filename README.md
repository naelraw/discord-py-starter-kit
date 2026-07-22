# 🚀 Discord.py Enterprise Starter Kit

Un template moderne, modulaire et hautement évolutif pour développer des bots Discord robustes en **Python 3.11+** avec `discord.py` v2.x.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![discord.py](https://img.shields.io/badge/discord.py-2.x-blueviolet.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-cyan.svg)

---

## 🌟 Fonctionnalités incluses

- ⚡ **Support natif des Slash Commands** via l'arbre de commandes `app_commands`.
- 🧩 **Architecture en Cogs (Modules)** pour charger/décharger facilement les fonctionnalités.
- 🎨 **Logging avancé** avec gestion des couleurs et niveaux de sévérité.
- 🐳 **Prêt pour Docker** : `Dockerfile` et `docker-compose.yml` préconfigurés.
- 🛡️ **Gestion des exceptions** et contrôle granulaire des permissions.
- ⚙️ **Séparation propre des configurations** via variables d'environnement (`.env`).

---

## 🛠️ Guide d'installation rapide

### Option A : Exécution locale

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/votre-utilisateur/discord-py-starter-kit.git](https://github.com/votre-utilisateur/discord-py-starter-kit.git)
   cd discord-py-starter-kit
   ```

2. **Créer l'environnement virtuel et installer les dépendances :**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement :**
   ```bash
   cp .env.example .env
   ```
   *Note : N'oubliez pas d'indiquer votre `DISCORD_TOKEN` dans le fichier `.env`.*

4. **Lancer le bot :**
   ```bash
   python main.py
   ```

### Option B : Exécution avec Docker

1. **Lancer le conteneur en arrière-plan :**
   ```bash
   docker-compose up -d --build
   ```

---

## 📁 Architecture du projet

```text
.
├── cogs/            # Modules de fonctionnalités (Commandes Slash)
│   ├── general.py   # Commandes utilitaires
│   └── moderation.py# Commandes de modération
├── config.py        # Configuration et initialisation des logs
├── main.py          # Point d'entrée principal du bot
├── Dockerfile       # Conteneurisation du projet
└── requirements.txt # Dépendances requises
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Veuillez consulter le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour en savoir plus sur la façon de proposer une Pull Request.

---

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
