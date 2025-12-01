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

**Périmètre IN:**
- ✅ 3 routes HTTP vulnérables
- ✅ Gestion paramètres GET
- ✅ Rendu templates dynamiques
- ✅ Exécution commandes système

**Périmètre OUT:**
- ❌ Authentification utilisateurs
- ❌ Base de données
- ❌ API REST complète
- ❌ Tests unitaires

#### 2.2.2 Module UTILS (utils/helpers.py)
**Confiance: 95% 🟢** | **Source: utils/helpers.py**

| Fonction | Vulnérabilité | Type OWASP | Ligne |
|----------|---------------|------------|-------|
| `execute_command()` | Command Injection via os.system | A03:2021 Injection | L8-12 |
| `run_shell_command()` | shell=True avec input non validé | A03:2021 Injection | L14-19 |
| `deserialize_data()` | pickle.loads non sécurisé | A08:2021 Deserialization | L21-25 |
| `read_file()` | Path Traversal | A01:2021 Broken Access | L27-32 |
| `backup_database()` | Credentials hardcodés | A07:2021 Auth Failures | L34-38 |
| `import_module_dynamic()` | Import dynamique non sécurisé | A03:2021 Injection | L41-43 |
| `calculate()` | eval() sur input utilisateur | A03:2021 Injection | L46-48 |

**Périmètre IN:**
- ✅ 7 fonctions utilitaires vulnérables
- ✅ Couverture multiples types de vulnérabilités
- ✅ Exemples réalistes d'erreurs courantes

**Périmètre OUT:**
- ❌ Versions sécurisées des fonctions
- ❌ Validation des inputs
- ❌ Sanitization

#### 2.2.3 Module FRONTEND (static/js/frontend.js)
**Confiance: 95% 🟢** | **Source: static/js/frontend.js**

| Fonction | Vulnérabilité | Type OWASP | Ligne |
|----------|---------------|------------|-------|
| `displayUserInput()` | XSS via innerHTML | A03:2021 Injection | L5-8 |
| `loadUserData()` | XSS via document.write | A03:2021 Injection | L10-14 |
| `executeUserScript()` | eval() dangereux | A03:2021 Injection | L16-19 |
| `updateProfile()` | XSS via setAttribute + outerHTML | A03:2021 Injection | L21-30 |
| `CONFIG` object | Secrets hardcodés côté client | A02:2021 Cryptographic Failures | L33-37 |
| `sendAnalytics()` | Transmission HTTP non sécurisée | A02:2021 Cryptographic Failures | L39-47 |

**Secrets Exposés:**
- `apiKey`: ak_live_abcdefghijklmnopqrstuvwxyz123456
- `secretToken`: tok_secret_987654321abcdefgh
- `stripeKey`: pk_live_1234567890abcdefghijklmnop

**Périmètre IN:**
- ✅ 6 fonctions JavaScript vulnérables
- ✅ Manipulation DOM non sécurisée
- ✅ Secrets exposés côté client
- ✅ Transmission HTTP non chiffrée

**Périmètre OUT:**
- ❌ Content Security Policy (CSP)
- ❌ Validation côté client
- ❌ HTTPS enforcement
- ❌ Gestion sécurisée des secrets

### 2.3 Synthèse Couverture OWASP Top 10

| OWASP 2021 | Présent | Fichiers Concernés |
|------------|---------|--------------------|
| A01 - Broken Access Control | ✅ | utils/helpers.py (Path Traversal) |
| A02 - Cryptographic Failures | ✅ | frontend.js (Secrets exposés, HTTP) |
| A03 - Injection | ✅ | Tous les fichiers (XSS, Command Injection, eval) |
| A07 - Auth Failures | ✅ | utils/helpers.py (Credentials hardcodés) |
| A08 - Software Data Integrity | ✅ | utils/helpers.py (Deserialization) |
| A05 - Security Misconfiguration | ✅ | web/views.py (Debug mode) |

---