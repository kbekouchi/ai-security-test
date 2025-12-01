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
| NFR-MAIN-001 | Code documenté avec commentaires explicatifs | ✅ RESPECTÉ | 🟢 95% | Code |
| NFR-MAIN-002 | Structure modulaire (web/utils/static) | ✅ RESPECTÉ | 🟢 100% | Arborescence |
| NFR-MAIN-003 | README avec instructions claires | ✅ RESPECTÉ | 🟢 100% | README.md |

---

## 📖 SECTION 4 : USER STORIES
**Confiance: 80% 🟢** | **Source: Déduction objectifs projet**

### 4.1 Epic: Évaluation Plateforme AI Security

#### US-001: Tester Détection XSS
**Confiance: 90% 🟢** | **Source: Analyse code web/views.py**

```
EN TANT QUE développeur de plateforme AI Security
JE VEUX analyser le code contenant des vulnérabilités XSS
AFIN DE vérifier que mon outil les détecte correctement
```

**Critères d'acceptation:**
- ✅ La plateforme détecte le XSS dans /profile (template non échappé)
- ✅ La plateforme détecte le XSS reflected dans /search
- ✅ La plateforme identifie les lignes exactes des vulnérabilités
- ✅ La plateforme propose des corrections appropriées

**Priorité**: 🔴 CRITIQUE  
**Effort estimé**: N/A (test)  
**Source**: web/views.py L8-31

#### US-002: Tester Détection Command Injection
**Confiance: 90% 🟢** | **Source: Analyse code utils/helpers.py**

```
EN TANT QUE développeur de plateforme AI Security
JE VEUX analyser du code avec des injections de commandes
AFIN DE valider la détection de ce type de vulnérabilité
```

**Critères d'acceptation:**
- ✅ Détection de os.system() avec input non validé
- ✅ Détection de subprocess avec shell=True
- ✅ Identification du niveau de sévérité (CRITIQUE)
- ✅ Suggestions de remédiation (subprocess sans shell, validation)

**Priorité**: 🔴 CRITIQUE  
**Source**: utils/helpers.py L8-19, web/views.py L33-42

---

## 📋 LISTE DE VALIDATION PRIORITAIRE

### ✅ Éléments Validés (Confiance 🟢)
1. Structure du repository
2. Présence des 3 modules (web, utils, static)
3. Types de vulnérabilités implémentées
4. Mapping OWASP Top 10

### 🟡 Éléments à Valider (Confiance 🟡/⚪)
1. **HAUTE PRIORITÉ**: Objectifs exacts du projet (interviewer le propriétaire)
2. **HAUTE PRIORITÉ**: Critères de succès pour les tests AI
3. **MOYENNE**: Exigences de performance
4. **BASSE**: Roadmap futures vulnérabilités

### ❌ Éléments Manquants
1. Tests unitaires pour valider les vulnérabilités
2. Documentation des scénarios d'exploitation
3. Métriques de couverture OWASP
4. Guide d'utilisation pour testeurs

---

**FIN DU DOCUMENT**  
*Dernière mise à jour: 2025*  
*Version: 1.0 DRAFT*