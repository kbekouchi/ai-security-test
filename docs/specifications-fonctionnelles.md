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

---

## 📖 SECTION 4 : USER STORIES
**Confiance: 85% 🟢** | **Source: Analyse objectifs + code**

### US-001: Détection XSS Reflected
**En tant que** plateforme AI de code review  
**Je veux** détecter les vulnérabilités XSS reflected dans le code  
**Afin de** protéger les applications contre l'injection de scripts malveillants

**Critères d'acceptation:**
- ✅ Détection de la route /search avec input non échappé
- ✅ Identification ligne exacte (L25-31)
- ✅ Sévérité: HAUTE

**Trace:** OBJ-001, OBJ-002 | Source: web/views.py

---

### US-002: Détection Command Injection
**En tant que** plateforme AI de code review  
**Je veux** détecter l'utilisation dangereuse de os.system() avec inputs utilisateur  
**Afin de** prévenir l'exécution de commandes arbitraires

**Critères d'acceptation:**
- ✅ Détection route /admin avec os.system()
- ✅ Identification ligne exacte (L33-42)
- ✅ Sévérité: CRITIQUE

**Trace:** OBJ-001, OBJ-002 | Source: web/views.py

---

### US-003: Benchmark de Précision
**En tant que** développeur de la plateforme AI  
**Je veux** mesurer le taux de détection sur ce repository  
**Afin de** valider la performance de l'outil

**Critères d'acceptation:**
- ✅ Taux de détection > 90%
- ✅ Aucun faux positif
- ✅ Rapport détaillé généré

**Trace:** OBJ-003 | Source: Déduction

---

## 🔐 SECTION 5 : RÈGLES MÉTIER
**Confiance: 90% 🟢**

### RG-001: Classification Sévérité
**Source:** OWASP Top 10

| Vulnérabilité | Sévérité | Justification |
|---------------|----------|---------------|
| Command Injection | 🔴 CRITIQUE | Exécution code arbitraire |
| SQL Injection | 🔴 CRITIQUE | Accès base de données |
| XSS Stored | 🟠 HAUTE | Persistance attaque |
| XSS Reflected | 🟡 MOYENNE | Impact limité |
| Path Traversal | 🟡 MOYENNE | Lecture fichiers |

---

## 📊 SECTION 6 : MATRICES DE TRAÇABILITÉ

### 6.1 Matrice OBJ ↔ US

| Objectif | US-001 | US-002 | US-003 |
|----------|--------|--------|--------|
| OBJ-001 | ✅ | ✅ | ✅ |
| OBJ-002 | ✅ | ✅ | ❌ |
| OBJ-003 | ❌ | ❌ | ✅ |

---

## 📚 SECTION 7 : GLOSSAIRE

- **XSS**: Cross-Site Scripting
- **OWASP**: Open Web Application Security Project
- **AI Code Review**: Analyse automatisée de code par intelligence artificielle

---

## 📎 SECTION 8 : ANNEXES

### 8.1 Liste de Validation Prioritaire

🔴 **CRITIQUE**
- [ ] Valider détection Command Injection (US-002)
- [ ] Confirmer sévérité CRITIQUE assignée

🟡 **HAUTE**
- [ ] Valider détection XSS (US-001)
- [ ] Vérifier taux détection > 90% (US-003)

---

**FIN DU DOCUMENT**