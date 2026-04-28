# 🚛 RO Transport — Modèle Académique

Application web interactive permettant de résoudre le **problème de transport en Recherche Opérationnelle** grâce à une interface moderne et un backend Python.

---

## 📌 Présentation

RO Transport est un outil pédagogique conçu pour :

- saisir les données d’un problème de transport ;
- définir le nombre d’origines *(m)* et destinations *(n)* ;
- remplir automatiquement ou manuellement la matrice des coûts ;
- calculer les solutions via Python ;
- comparer plusieurs méthodes de résolution ;
- afficher le coût total optimal.

---

## 🖥️ Aperçu de l'application

### Interface principale

![Accueil](screenshots/home.png)

### Résultat Balas-Hammer

![Balas](screenshots/balas.png)

### Résultat MINICO

![Minico](screenshots/minico.png)

---

## ⚙️ Technologies utilisées

### Frontend

- HTML5
- CSS3
- JavaScript Vanilla

### Backend

- Python
- FastAPI / Flask (selon votre implémentation)
- API REST locale

---

## 📁 Structure du projet

```bash
RO-Transport/
│── backend/
│   ├── main.py
│   ├── solver.py
│   └── requirements.txt
│
│── frontend/
│   ├── js/
│   ├── screenshots/
│   │   ├── home.png
│   │   ├── balas.png
│   │   └── minico.png
│   ├── index.html
│   └── README.md
