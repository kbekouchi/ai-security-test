# 📋 SPÉCIFICATIONS FONCTIONNELLES
**Repository de Test pour AI Security Code Review Platform**

---

## 📊 MÉTADONNÉES

| Attribut | Valeur |
|----------|--------|
| **Projet** | ai-security-test |
| **Repository** | kbekouchi/ai-security-test |
| **Version** | 1.0 |
| **Date** | 2025 |
| **Statut** | 🟢 DRAFT |
| **Confiance globale** | 90% 🟢 |
| **Auteur** | Expert Specs Fonctionnelles |
| **Sources** | Code source GitHub, README.md |

---

## 🎯 SECTION 1 : CONTEXTE ET OBJECTIFS
**Confiance: 95% 🟢** | **Source: README.md, analyse code**

### 1.1 Contexte Projet

Le repository **ai-security-test** est un projet de test intentionnellement vulnérable destiné à servir de base d'évaluation pour une plateforme d'AI Code Review spécialisée dans la détection de vulnérabilités de sécurité.

**Type**: Repository de test / Vulnerable by Design  
**Langage principal**: Python (Flask)  
**Branche par défaut**: main  
**Statut**: Actif

### 1.2 Objectifs Principaux

| ID | Objectif | Priorité | Source |
|----|----------|----------|--------|
| OBJ-001 | Fournir un ensemble de vulnérabilités réelles pour tester les capacités de détection d'une plateforme AI | 🔴 CRITIQUE | README.md |
| OBJ-002 | Couvrir les vulnérabilités OWASP Top 10 les plus courantes | 🔴 CRITIQUE | Analyse code |
| OBJ-003 | Servir de benchmark pour évaluer la précision de détection | 🟡 HAUTE | Déduction |
| OBJ-004 | Permettre des tests reproductibles et documentés | 🟡 HAUTE | Déduction |

### 1.3 Parties Prenantes

| Rôle | Responsabilité | Interaction |
|------|----------------|-------------|
| **Développeurs AI Platform** | Utilisent le repo pour tester leur outil | Lecture code, analyse résultats |
| **Security Researchers** | Valident la pertinence des vulnérabilités | Audit code, suggestions |
| **QA/Testeurs** | Vérifient la détection des vulnérabilités | Exécution tests, validation |

### 1.4 Contraintes Identifiées

- ⚠️ **Contrainte de sécurité**: Ne JAMAIS déployer en production
- ⚠️ **Contrainte d'usage**: Uniquement à des fins éducatives et de test
- ⚠️ **Contrainte légale**: Respect des lois sur la sécurité informatique

---

## 🔍 SECTION 2 : PÉRIMÈTRE FONCTIONNEL
**Confiance: 90% 🟢** | **Source: Arborescence GitHub, analyse fichiers**

### 2.1 Vue d'Ensemble du Système

```
ai-security-test/
├── web/              → Application Flask vulnérable
│   └── views.py      → Routes HTTP avec vulnérabilités XSS, Command Injection
├── utils/            → Fonctions utilitaires vulnérables
│   └── helpers.py    → Helpers avec multiples vulnérabilités
├── static/           → Ressources frontend
│   └── js/
│       └── frontend.js → JavaScript avec XSS, secrets exposés
├── README.md         → Documentation projet
└── .gitignore        → Configuration Git
```

### 2.2 Modules Fonctionnels

#### 2.2.1 Module WEB (web/views.py)
**Confiance: 95% 🟢** | **Source: web/views.py**

| Composant | Description | Vulnérabilités Intentionnelles | Ligne |
|-----------|-------------|-------------------------------|-------|
| **Route /profile** | Page profil utilisateur | XSS via template non échappé | L8-23 |
| **Route /search** | Fonction recherche | XSS reflected dans réponse HTML | L25-31 |
| **Route /admin** | Panel administration | Command Injection via os.system() | L33-42 |
| **Configuration Flask** | Démarrage app | Debug mode activé en production | L45-46 |

---

## ⚙️ SECTION 3 : EXIGENCES NON-FONCTIONNELLES
**Confiance: 70% 🟡** | **Source: Déduction contexte test**

### 3.1 Performance

| ID | Exigence | Priorité | Confiance | Source |
|----|----------|----------|-----------|--------|
| NFR-PERF-001 | Temps de réponse < 2s pour toutes les routes | 🟢 BASSE | ⚪ 50% | Déduction |
| NFR-PERF-002 | Support de 10 requêtes simultanées minimum | 🟢 BASSE | ⚪ 50% | Déduction |

**Note**: Ce repository étant un environnement de test, les performances ne sont pas critiques.

### 3.2 Sécurité (Intentionnellement NON Respectées)

| ID | Exigence | Statut | Confiance | Source |
|----|----------|--------|-----------|--------|
| NFR-SEC-001 | Validation des inputs utilisateur | ❌ VIOLÉ INTENTIONNELLEMENT | 🟢 100% | Code |
| NFR-SEC-002 | Échappement des outputs dans templates | ❌ VIOLÉ INTENTIONNELLEMENT | 🟢 100% | Code |
| NFR-SEC-003 | Pas d'exécution commandes shell avec input user | ❌ VIOLÉ INTENTIONNELLEMENT | 🟢 100% | Code |
| NFR-SEC-004 | Credentials en variables d'environnement | ❌ VIOLÉ INTENTIONNELLEMENT | 🟢 100% | Code |
| NFR-SEC-005 | Mode debug désactivé en production | ❌ VIOLÉ INTENTIONNELLEMENT | 🟢 100% | Code |

### 3.3 Maintenabilité

| ID | Exigence | Statut | Confiance | Source |
|----|----------|--------|-----------|--------|
| NFR-MAIN-001 | Code documenté avec commentaires explicites | ✅ RESPECTÉ | 🟢 100% | Code |
| NFR-MAIN-002 | Structure modulaire claire | ✅ RESPECTÉ | 🟢 90% | Arborescence |

---

## 👤 SECTION 4 : USER STORIES
**Confiance: 85% 🟢** | **Source: Analyse objectifs + code**

### 4.1 User Stories - Développeur AI Platform

#### US-001: Tester la détection XSS
**Confiance: 95% 🟢** | **Priorité: 🔴 CRITIQUE** | **Lié à: OBJ-001, OBJ-002**

**En tant que** développeur de plateforme AI de code review  
**Je veux** analyser le code contenant des vulnérabilités XSS  
**Afin de** vérifier que mon outil détecte correctement les failles XSS reflected et stored

**Critères d'acceptation:**
- ✅ La plateforme scanne web/views.py lignes 8-31
- ✅ Détecte XSS dans route /profile (template non échappé)
- ✅ Détecte XSS dans route /search (réponse HTML directe)
- ✅ Génère un rapport avec sévérité HAUTE
- ✅ Fournit des recommandations de correction

**Source:** web/views.py L8-31

---

#### US-002: Tester la détection Command Injection
**Confiance: 95% 🟢** | **Priorité: 🔴 CRITIQUE** | **Lié à: OBJ-001, OBJ-002**

**En tant que** développeur de plateforme AI  
**Je veux** analyser le code avec injection de commandes  
**Afin de** valider la détection des appels système dangereux

**Critères d'acceptation:**
- ✅ Détecte os.system() avec input utilisateur non validé
- ✅ Identifie la route /admin comme critique
- ✅ Suggère l'utilisation de subprocess avec validation
- ✅ Sévérité marquée CRITIQUE

**Source:** web/views.py L33-42

---

#### US-003: Tester la détection de secrets exposés
**Confiance: 90% 🟢** | **Priorité: 🟡 HAUTE** | **Lié à: OBJ-001, OBJ-002**

**En tant que** développeur de plateforme AI  
**Je veux** scanner le code JavaScript frontend  
**Afin de** détecter les API keys et secrets hardcodés

**Critères d'acceptation:**
- ✅ Scanne static/js/frontend.js
- ✅ Détecte les clés API en clair
- ✅ Identifie les tokens exposés
- ✅ Recommande l'utilisation de variables d'environnement

**Source:** static/js/frontend.js

---

### 4.2 User Stories - Security Researcher

#### US-004: Valider la pertinence des vulnérabilités
**Confiance: 80% 🟡** | **Priorité: 🟡 HAUTE** | **Lié à: OBJ-003**

**En tant que** chercheur en sécurité  
**Je veux** auditer le code du repository  
**Afin de** confirmer que les vulnérabilités sont réalistes et exploitables

**Critères d'acceptation:**
- ✅ Chaque vulnérabilité est documentée
- ✅ Les vulnérabilités suivent OWASP Top 10
- ✅ Code exploitable en conditions réelles
- ✅ Pas de faux positifs intentionnels

**Source:** Déduction objectifs

---

### 4.3 User Stories - QA/Testeur

#### US-005: Exécuter des tests de détection
**Confiance: 75% 🟡** | **Priorité: 🟡 HAUTE** | **Lié à: OBJ-004**

**En tant que** testeur QA  
**Je veux** exécuter la plateforme AI sur ce repository  
**Afin de** mesurer le taux de détection et les faux positifs

**Critères d'acceptation:**
- ✅ Tous les fichiers sont analysables
- ✅ Temps d'analyse < 5 minutes
- ✅ Rapport de résultats exploitable
- ✅ Métriques de couverture disponibles

**Source:** Déduction objectifs

---