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

| Élément | Vulnérabilité | Type | Ligne |
|---------|---------------|------|-------|
| **API Key hardcodée** | Secret exposé dans code | A05:2021 Security Misconfig | L3 |
| **innerHTML dynamique** | DOM-based XSS | A03:2021 Injection | L10 |
| **eval() sur input** | Code Injection JavaScript | A03:2021 Injection | L15 |

**Périmètre IN:**
- ✅ Code JavaScript client-side
- ✅ Manipulation DOM vulnérable
- ✅ Secrets exposés

**Périmètre OUT:**
- ❌ Framework frontend moderne
- ❌ Gestion sécurisée des secrets
- ❌ Content Security Policy

---

## ⚙️ SECTION 3 : EXIGENCES NON-FONCTIONNELLES
**Confiance: 70% 🟡** | **Source: Déduction basée sur usage prévu**

### 3.1 Performance

| ID | Exigence | Valeur Cible | Priorité |
|----|----------|--------------|----------|
| NFR-PERF-001 | Temps de réponse routes HTTP | < 1s | 🟢 BASSE |
| NFR-PERF-002 | Capacité à gérer tests concurrents | 10 requêtes/s | 🟢 BASSE |

**Justification**: En tant que repo de test, la performance n'est pas critique.

### 3.2 Sécurité (Inversée)

⚠️ **ATTENTION**: Ce repository est INTENTIONNELLEMENT vulnérable.

| ID | Anti-Exigence | Statut | Source |
|----|---------------|--------|--------|
| NFR-SEC-001 | ❌ Aucune validation des inputs | REQUIS | Objectif projet |
| NFR-SEC-002 | ❌ Pas de sanitization | REQUIS | Objectif projet |
| NFR-SEC-003 | ❌ Secrets en clair acceptés | REQUIS | Objectif projet |
| NFR-SEC-004 | ❌ Debug mode en production | REQUIS | web/views.py L46 |

### 3.3 Maintenabilité

| ID | Exigence | Description | Priorité |
|----|----------|-------------|----------|
| NFR-MAINT-001 | Documentation des vulnérabilités | Chaque vulnérabilité doit être commentée | 🟡 HAUTE |
| NFR-MAINT-002 | Code lisible | Vulnérabilités facilement identifiables | 🟡 HAUTE |
| NFR-MAINT-003 | Versioning Git | Historique clair des modifications | 🟡 HAUTE |

---

## 📖 SECTION 4 : USER STORIES
**Confiance: 85% 🟢** | **Source: Analyse besoins utilisateurs**

### 4.1 Développeur de Plateforme AI

**US-001**: Tester la détection XSS  
**En tant que** développeur AI Platform  
**Je veux** analyser le code avec des XSS  
**Afin de** valider que mon outil détecte correctement les failles XSS  
**Critères d'acceptation**:  
- ✅ Le repo contient au moins 2 types de XSS (stored/reflected/DOM)  
- ✅ Les vulnérabilités sont réalistes  
- ✅ Le code est exécutable  
**Priorité**: 🔴 CRITIQUE | **Source**: Objectif principal projet

**US-002**: Évaluer la détection Command Injection  
**En tant que** développeur AI Platform  
**Je veux** tester mon outil sur des command injections  
**Afin de** mesurer le taux de détection  
**Critères d'acceptation**:  
- ✅ Présence de os.system() avec input non validé  
- ✅ Présence de subprocess avec shell=True  
- ✅ Contextes d'exploitation variés  
**Priorité**: 🔴 CRITIQUE | **Source**: utils/helpers.py

**US-003**: Benchmark OWASP Top 10  
**En tant que** développeur AI Platform  
**Je veux** un repo couvrant OWASP Top 10  
**Afin de** avoir un benchmark complet  
**Critères d'acceptation**:  
- ✅ Au moins 5 catégories OWASP couvertes  
- ✅ Documentation des types de vulnérabilités  
**Priorité**: 🟡 HAUTE | **Source**: README.md

### 4.2 Security Researcher

**US-004**: Valider la pertinence des vulnérabilités  
**En tant que** security researcher  
**Je veux** auditer le code vulnérable  
**Afin de** confirmer que les vulnérabilités sont réalistes  
**Critères d'acceptation**:  
- ✅ Code reflète des erreurs réelles  
- ✅ Vulnérabilités exploitables  
- ✅ Pas de faux positifs intentionnels  
**Priorité**: 🟡 HAUTE | **Source**: Déduction

---

*Document en cours de rédaction - Sections 5 à 8 à compléter*