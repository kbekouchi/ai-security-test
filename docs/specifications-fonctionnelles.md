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
**Confiance: 90% 🟢** | **Source: static/js/frontend.js**

| Élément | Vulnérabilité | Type OWASP | Ligne |
|---------|---------------|------------|-------|
| **API Key hardcodée** | Secrets exposés dans code client | A02:2021 Cryptographic Failures | L3 |
| **innerHTML dynamique** | DOM-based XSS | A03:2021 Injection | L7-9 |
| **eval() sur données externes** | Code Injection côté client | A03:2021 Injection | L11 |

**Périmètre IN:**
- ✅ Code JavaScript vulnérable
- ✅ Secrets exposés
- ✅ Manipulation DOM non sécurisée

**Périmètre OUT:**
- ❌ Framework frontend moderne
- ❌ Content Security Policy
- ❌ Gestion sécurisée des secrets

### 2.3 Synthèse de Couverture

**Total vulnérabilités identifiées**: 13  
**Types OWASP couverts**: 4/10

---

## ⚙️ SECTION 3 : EXIGENCES NON-FONCTIONNELLES
**Confiance: 85% 🟢** | **Source: Déduction contexte test**

### 3.1 Performance

| ID | Exigence | Critère | Priorité |
|----|----------|---------|----------|
| NFR-PERF-001 | Temps de réponse routes HTTP | < 500ms | 🟢 BASSE |
| NFR-PERF-002 | Charge supportée | N/A (repo test) | ⚪ N/A |

### 3.2 Sécurité

| ID | Exigence | Critère | Priorité |
|----|----------|---------|----------|
| NFR-SEC-001 | Isolation environnement | Jamais en production | 🔴 CRITIQUE |
| NFR-SEC-002 | Documentation vulnérabilités | Toutes documentées | 🔴 CRITIQUE |
| NFR-SEC-003 | Avertissements visibles | README + commentaires code | 🟡 HAUTE |

### 3.3 Maintenabilité

| ID | Exigence | Critère | Priorité |
|----|----------|---------|----------|
| NFR-MAIN-001 | Structure code claire | Séparation modules | 🟡 HAUTE |
| NFR-MAIN-002 | Commentaires explicites | Chaque vulnérabilité commentée | 🟡 HAUTE |
| NFR-MAIN-003 | Versioning | Git + tags | 🟢 MOYENNE |

---

## 📖 SECTION 4 : USER STORIES
**Confiance: 80% 🟡** | **Source: Déduction usage**

### US-001: Tester la détection XSS
**En tant que** développeur de plateforme AI  
**Je veux** analyser les routes /profile et /search  
**Afin de** vérifier que mon outil détecte les XSS reflected et stored

**Critères d'acceptation:**
- ✅ Détection XSS dans template Jinja2 non échappé
- ✅ Détection XSS dans réponse HTML directe
- ✅ Identification ligne précise

**Priorité**: 🔴 CRITIQUE  
**Source**: web/views.py L8-31

### US-002: Tester la détection Command Injection
**En tant que** security researcher  
**Je veux** analyser les fonctions execute_command et run_shell_command  
**Afin de** valider la détection d'injection de commandes

**Critères d'acceptation:**
- ✅ Détection os.system() avec input non validé
- ✅ Détection subprocess avec shell=True
- ✅ Suggestion de remediation

**Priorité**: 🔴 CRITIQUE  
**Source**: utils/helpers.py L8-19

---

*[Suite des sections à venir: Section 5 - Règles Métier, Section 6 - Matrices de Traçabilité, Section 7 - Annexes, Section 8 - Liste de Validation]*