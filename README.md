# API Cloud Advanced - Docker & PaaS Deployment
**Réalisées par :** Karima Amezgou & Imane Moustakimi

## Présentation du Projet
Ce projet consiste en la conception, la conteneurisation et le déploiement automatisé d'une API REST Flask.
L'objectif est de démontrer une maîtrise complète du cycle de vie DevOps, de la gestion de code source au déploiement sur une infrastructure Cloud.

## Stack Technique
* **Langage :** Python 3.9 (Flask Framework)
* **Conteneurisation :** Docker
* **Versionnage :** Git / GitHub
* **Infrastructure Cloud :** SnapDeploy (Container as a Service)
* **Pipeline :** CI/CD automatisé via GitHub Webhooks

## Expertise Module : Cloud Computing Advanced

### 1. Architecture & Conteneurisation (Docker)
* **Portabilité :** Grâce au `Dockerfile`, l'environnement d'exécution est indépendant de l'infrastructure physique. "Write once, run anywhere" (Local, Codespaces, ou Cloud).
* **Isolation & Micro-services :** L'application est isolée dans un conteneur, exposant uniquement le **Port 5000** pour une communication réseau sécurisée et optimisée.
### 2. Automatisation & CI/CD
* **Déploiement Continu :** Chaque "Commit" sur la branche `main` déclenche automatiquement un nouveau cycle de "Build" et de "Deploy" sur SnapDeploy.
* **Zéro Temps d'Arrêt :** Le pipeline assure une mise à jour fluide de l'API sans interruption de service pour l'utilisateur final.
### 3. Gestion Cloud & FinOps
* **Injection de Configuration :** Utilisation de variables d'environnement (`SECRET_KEY`) injectées dynamiquement au déploiement, séparant le code de la configuration.
* **Optimisation des Ressources :** Gestion active du cycle de vie des instances (Start/Stop) pour minimiser l'empreinte carbone et les coûts d'infrastructure.

## Accès à l'API
L'API est accessible publiquement à l'adresse suivante :
[https://kimaapp.containers.snapdeploy.dev/api/users]

--
*Projet réalisé dans le cadre de la formation Cloud Advanced - 2026*
