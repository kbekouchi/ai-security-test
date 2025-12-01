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
| NFR-MAIN-001 | Code documenté avec commentaires explicites | ✅ RESPECTÉ | 🟢 90% | Code |
| NFR-MAIN-002 | Structure modulaire claire | ✅ RESPECTÉ | 🟢 85% | Arborescence |

---

## 👤 SECTION 4 : USER STORIES
**Confiance: 85% 🟢** | **Source: Analyse code, déduction usage**

### 4.1 Epic: Détection de Vulnérabilités XSS

#### US-001: Détection XSS Stored (Route /profile)
**En tant que** plateforme AI de code review  
**Je veux** détecter les vulnérabilités XSS Stored dans les templates Flask  
**Afin de** identifier les risques d'injection de scripts malveillants persistants

**Priorité**: 🔴 CRITIQUE  
**Confiance**: 🟢 95%  
**Source**: web/views.py L8-23  
**Trace**: OBJ-001, OBJ-002

**Critères d'acceptation**:
- ✅ Identifier l'absence d'échappement dans `render_template_string()`
- ✅ Détecter l'interpolation directe de `user_data` sans validation
- ✅ Signaler la sévérité comme HAUTE/CRITIQUE
- ✅ Fournir la ligne exacte du code vulnérable

#### US-002: Détection XSS Reflected (Route /search)
**En tant que** plateforme AI de code review  
**Je veux** détecter les vulnérabilités XSS Reflected dans les réponses HTTP  
**Afin de** identifier les risques d'injection via paramètres URL

**Priorité**: 🔴 CRITIQUE  
**Confiance**: 🟢 95%  
**Source**: web/views.py L25-31  
**Trace**: OBJ-001, OBJ-002

**Critères d'acceptation**:
- ✅ Identifier l'absence de validation sur `request.args.get()`
- ✅ Détecter l'insertion directe dans HTML sans échappement
- ✅ Signaler le vecteur d'attaque (paramètre GET)

### 4.2 Epic: Détection Command Injection

#### US-003: Détection Command Injection (Route /admin)
**En tant que** plateforme AI de code review  
**Je veux** détecter l'utilisation dangereuse de `os.system()` avec input utilisateur  
**Afin de** prévenir l'exécution de commandes système arbitraires

**Priorité**: 🔴 CRITIQUE  
**Confiance**: 🟢 100%  
**Source**: web/views.py L33-42  
**Trace**: OBJ-001, OBJ-002, NFR-SEC-003

**Critères d'acceptation**:
- ✅ Identifier `os.system()` avec concaténation d'input utilisateur
- ✅ Détecter l'absence de validation/sanitization
- ✅ Proposer des alternatives sécurisées (subprocess avec shell=False)

### 4.3 Epic: Détection Mauvaises Configurations

#### US-004: Détection Debug Mode en Production
**En tant que** plateforme AI de code review  
**Je veux** détecter l'activation du mode debug Flask  
**Afin de** prévenir l'exposition d'informations sensibles

**Priorité**: 🟡 HAUTE  
**Confiance**: 🟢 100%  
**Source**: web/views.py L45-46  
**Trace**: OBJ-002, NFR-SEC-005

**Critères d'acceptation**:
- ✅ Identifier `app.run(debug=True)`
- ✅ Signaler le risque d'exposition du debugger Werkzeug
- ✅ Recommander debug=False pour production

---