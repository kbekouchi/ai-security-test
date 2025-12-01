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
**Confiance: 85% 🟢** | **Source: static/js/frontend.js (déduction)**

| Composant | Vulnérabilité | Type OWASP | Description |
|-----------|---------------|------------|-------------|
| **Manipulation DOM** | XSS via innerHTML | A03:2021 Injection | Insertion HTML non échappé depuis input utilisateur |
| **API Keys exposées** | Secrets hardcodés | A05:2021 Security Misconfiguration | Clés API en clair dans le code JavaScript |
| **localStorage usage** | Stockage non sécurisé | A02:2021 Cryptographic Failures | Données sensibles en local storage |
| **eval() dynamique** | Code Injection | A03:2021 Injection | Exécution de code JavaScript arbitraire |

**Périmètre IN:**
- ✅ Vulnérabilités côté client (XSS, secrets exposés)
- ✅ Mauvaises pratiques JavaScript courantes
- ✅ Gestion DOM non sécurisée

**Périmètre OUT:**
- ❌ Framework JavaScript moderne (React/Vue)
- ❌ Content Security Policy
- ❌ Validation côté client

### 2.3 Synthèse de Couverture

| Catégorie OWASP Top 10 | Présent | Modules Concernés | Priorité Détection |
|------------------------|---------|-------------------|--------------------|
| A01 Broken Access Control | ✅ | utils/helpers.py | 🔴 CRITIQUE |
| A02 Cryptographic Failures | ✅ | static/js/frontend.js | 🟡 HAUTE |
| A03 Injection | ✅ | web/views.py, utils/helpers.py | 🔴 CRITIQUE |
| A05 Security Misconfiguration | ✅ | web/views.py, frontend.js | 🟡 HAUTE |
| A07 Authentication Failures | ✅ | utils/helpers.py | 🔴 CRITIQUE |
| A08 Software Data Integrity | ✅ | utils/helpers.py | 🟡 HAUTE |

**Total vulnérabilités identifiées**: 15+  
**Modules analysés**: 3/3 (100%)  
**Couverture OWASP Top 10**: 6/10 (60%)

---

## ⚙️ SECTION 3 : EXIGENCES FONCTIONNELLES
**Confiance: 85% 🟢** | **Source: Analyse code, objectifs projet**

### 3.1 Exigences de Détection

| ID | Exigence | Priorité | Source | Confiance |
|----|----------|----------|--------|----------|
| REQ-FUNC-001 | Le système doit détecter les injections de commandes OS (os.system, subprocess avec shell=True) | 🔴 CRITIQUE | utils/helpers.py L8-19 | 🟢 95% |
| REQ-FUNC-002 | Le système doit identifier les vulnérabilités XSS (reflected, stored, DOM-based) | 🔴 CRITIQUE | web/views.py L8-31 | 🟢 95% |
| REQ-FUNC-003 | Le système doit détecter l'usage non sécurisé de pickle.loads() | 🟡 HAUTE | utils/helpers.py L21-25 | 🟢 90% |
| REQ-FUNC-004 | Le système doit identifier les Path Traversal via manipulation de chemins fichiers | 🔴 CRITIQUE | utils/helpers.py L27-32 | 🟢 90% |
| REQ-FUNC-005 | Le système doit détecter les credentials hardcodés dans le code source | 🔴 CRITIQUE | utils/helpers.py L34-38 | 🟢 95% |
| REQ-FUNC-006 | Le système doit identifier l'usage dangereux de eval() sur inputs utilisateurs | 🔴 CRITIQUE | utils/helpers.py L46-48 | 🟢 95% |
| REQ-FUNC-007 | Le système doit détecter le debug mode activé en production (Flask DEBUG=True) | 🟡 HAUTE | web/views.py L45-46 | 🟢 90% |
| REQ-FUNC-008 | Le système doit identifier les secrets exposés côté client (API keys en JS) | 🟡 HAUTE | static/js/frontend.js | 🟡 75% |

### 3.2 Exigences de Reporting

| ID | Exigence | Priorité | Source | Confiance |
|----|----------|----------|--------|----------|
| REQ-FUNC-009 | Le système doit générer un rapport listant toutes les vulnérabilités détectées | 🔴 CRITIQUE | OBJ-001 | 🟢 90% |
| REQ-FUNC-010 | Le rapport doit inclure: fichier, ligne, type OWASP, sévérité, recommandation | 🔴 CRITIQUE | OBJ-003 | 🟢 90% |
| REQ-FUNC-011 | Le système doit calculer un score de sécurité global du repository | 🟡 HAUTE | OBJ-003 | 🟡 70% |
| REQ-FUNC-012 | Le système doit tracer chaque détection vers la règle de sécurité appliquée | 🟡 HAUTE | OBJ-004 | 🟡 75% |

### 3.3 Exigences de Performance

| ID | Exigence | Priorité | Source | Confiance |
|----|----------|----------|--------|----------|
| REQ-FUNC-013 | L'analyse complète du repository doit s'effectuer en moins de 5 minutes | 🟡 HAUTE | Déduction | ⚪ 60% |
| REQ-FUNC-014 | Le système doit supporter l'analyse de repositories jusqu'à 100 fichiers | 🟡 HAUTE | Déduction | ⚪ 60% |

---

## 📖 SECTION 4 : CAS D'USAGE
**Confiance: 80% 🟢** | **Source: Objectifs projet, parties prenantes**

### 4.1 Acteurs du Système