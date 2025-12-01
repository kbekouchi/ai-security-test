# SPÉCIFICATIONS FONCTIONNELLES
**Projet:** AI Security Test Repository  
**Repository:** kbekouchi/ai-security-test  
**Version:** 1.0  
**Date:** 2025-01-21  
**Niveau de confiance global:** 🟡 MOYEN (structure présente, code à implémenter)

---

## SECTION 1 : CONTEXTE ET OBJECTIFS

### 1.1 Contexte du Projet
**Source:** Description repository GitHub  
**Confiance:** 🟢 ÉLEVÉE

Le projet `ai-security-test` est un repository de test créé spécifiquement pour évaluer et tester une plateforme d'AI Code Review. Il s'agit d'un environnement contrôlé contenant intentionnellement des vulnérabilités de sécurité.

**Caractéristiques du repository:**
- **Création:** 21 janvier 2025
- **Langage principal:** Python
- **Type:** Repository de test public
- **Objectif déclaré:** Contenir des vulnérabilités intentionnelles pour tester des outils d'analyse

### 1.2 Objectifs Fonctionnels
**Source:** Déduction de la structure et description  
**Confiance:** 🟡 MOYENNE

**OBJ-001** : Fournir un environnement de test réaliste pour plateforme d'AI Code Review  
**OBJ-002** : Exposer différents types de vulnérabilités de sécurité courantes  
**OBJ-003** : Permettre la validation des capacités de détection d'une IA  
**OBJ-004** : Servir de benchmark pour évaluer la précision des analyses

### 1.3 Parties Prenantes
**Source:** Contexte projet  
**Confiance:** 🟡 MOYENNE

| Rôle | Responsabilité | Implication |
|------|----------------|-------------|
| Développeur/Propriétaire | Création et maintenance du repository de test | Haute |
| Plateforme AI Code Review | Analyse et détection des vulnérabilités | Haute |
| Équipe Sécurité | Validation des vulnérabilités introduites | Moyenne |
| Testeurs | Évaluation des résultats de détection | Moyenne |

---

## SECTION 2 : PÉRIMÈTRE FONCTIONNEL

### 2.1 Modules et Composants
**Source:** Analyse structure repository (frontend.js, helpers.py)  
**Confiance:** 🟢 ÉLEVÉE

#### 2.1.1 Module Frontend (JavaScript)
**Fichier:** `static/js/frontend.js`  
**Responsabilité:** Démonstration de vulnérabilités côté client

**Fonctions identifiées:**
- `displayUserInput()` - Affichage direct de contenu utilisateur (XSS)
- `loadUserData()` - Chargement de données utilisateur (XSS via document.write)
- `executeUserScript()` - Exécution de scripts dynamiques (eval dangereux)
- `updateProfile()` - Mise à jour profil utilisateur (XSS multiple)
- `sendAnalytics()` - Envoi données analytiques (exposition secrets)

**Vulnérabilités exposées:**
- XSS via innerHTML, outerHTML, document.write
- Utilisation dangereuse de eval()
- Clés API hardcodées côté client
- Transmission non sécurisée (HTTP)

#### 2.1.2 Module Utilitaires (Python)
**Fichier:** `utils/helpers.py`  
**Responsabilité:** Démonstration de vulnérabilités backend

**Fonctions identifiées:**
- `execute_command()` - Exécution commandes système (Command Injection)
- `run_shell_command()` - Subprocess avec shell=True (Command Injection)
- `deserialize_data()` - Désérialisation pickle (Code Execution)
- `read_file()` - Lecture fichiers (Path Traversal)
- `backup_database()` - Backup BDD (Credentials hardcodés)
- `import_module_dynamic()` - Import dynamique (Code Injection)
- `calculate()` - Évaluation expressions (eval dangereux)

**Vulnérabilités exposées:**
- Command Injection (os.system, subprocess.run)
- Insecure Deserialization (pickle.loads)
- Path Traversal
- Hardcoded Credentials
- Code Injection (eval, __import__)

### 2.2 Périmètre Inclus
**Source:** Analyse des fichiers de code  
**Confiance:** 🟢 ÉLEVÉE

**PÉRIM-IN-001** : Vulnérabilités XSS (Cross-Site Scripting)  
**PÉRIM-IN-002** : Vulnérabilités Command Injection  
**PÉRIM-IN-003** : Insecure Deserialization  
**PÉRIM-IN-004** : Path Traversal  
**PÉRIM-IN-005** : Hardcoded Secrets (API keys, credentials)  
**PÉRIM-IN-006** : Utilisation dangereuse de eval()  
**PÉRIM-IN-007** : Transmission non sécurisée (HTTP vs HTTPS)  
**PÉRIM-IN-008** : Import/exécution dynamique de code

### 2.3 Périmètre Exclu
**Source:** Déduction du contexte de test  
**Confiance:** 🟡 MOYENNE

**PÉRIM-EX-001** : Correction automatique des vulnérabilités (hors scope)  
**PÉRIM-EX-002** : Déploiement en production (environnement de test uniquement)  
**PÉRIM-EX-003** : Gestion d'utilisateurs réels  
**PÉRIM-EX-004** : Traitement de données sensibles réelles  
**PÉRIM-EX-005** : Tests de performance ou charge  
**PÉRIM-EX-006** : Intégration avec systèmes externes réels

---

## SECTION 3 : EXIGENCES FONCTIONNELLES DÉTAILLÉES

### 3.1 Exigences de Vulnérabilités XSS
**Source:** Analyse frontend.js  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-001** : Exposition XSS via innerHTML  
**Description:** La fonction `displayUserInput()` doit permettre l'injection de code HTML/JavaScript via innerHTML sans sanitization  
**Priorité:** HAUTE  
**Traçabilité:** frontend.js:L1-L5

**REQ-FUNC-002** : XSS via document.write  
**Description:** La fonction `loadUserData()` doit utiliser document.write pour injecter du contenu non échappé  
**Priorité:** HAUTE  
**Traçabilité:** frontend.js:L7-L11

**REQ-FUNC-003** : Exécution eval() dangereuse  
**Description:** La fonction `executeUserScript()` doit permettre l'exécution de code JavaScript arbitraire via eval()  
**Priorité:** CRITIQUE  
**Traçabilité:** frontend.js:L13-L17

### 3.2 Exigences Command Injection
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-004** : Command Injection via os.system  
**Description:** La fonction `execute_command()` doit permettre l'injection de commandes système via os.system  
**Priorité:** CRITIQUE  
**Traçabilité:** helpers.py:L5-L8

**REQ-FUNC-005** : Shell Injection via subprocess  
**Description:** La fonction `run_shell_command()` doit utiliser subprocess.run avec shell=True sans validation  
**Priorité:** CRITIQUE  
**Traçabilité:** helpers.py:L10-L13

### 3.3 Exigences Désérialisation
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-006** : Insecure Deserialization  
**Description:** La fonction `deserialize_data()` doit utiliser pickle.loads sur des données non fiables  
**Priorité:** CRITIQUE  
**Traçabilité:** helpers.py:L15-L18

---

## SECTION 4 : EXIGENCES NON-FONCTIONNELLES

### 4.1 Exigences de Sécurité (Intentionnelles)
**Source:** Objectif du repository de test  
**Confiance:** 🟢 ÉLEVÉE

**REQ-NF-001** : Vulnérabilités Authentiques  
**Description:** Les vulnérabilités doivent être réalistes et représentatives des failles courantes en production  
**Critère:** Correspondance avec OWASP Top 10  
**Priorité:** CRITIQUE

**REQ-NF-002** : Isolation Environnement  
**Description:** Le repository ne doit jamais être déployé en production ou contenir de vraies données sensibles  
**Critère:** Marquage clair "TEST ONLY" dans README  
**Priorité:** CRITIQUE

**REQ-NF-003** : Documentation Vulnérabilités  
**Description:** Chaque vulnérabilité doit être documentée avec son type, sa localisation et son impact  
**Critère:** Commentaires dans le code ou fichier VULNERABILITIES.md  
**Priorité:** HAUTE

### 4.2 Exigences de Maintenabilité
**Source:** Contexte projet de test  
**Confiance:** 🟡 MOYENNE

**REQ-NF-004** : Lisibilité du Code  
**Description:** Le code doit rester lisible malgré les vulnérabilités pour faciliter la compréhension des testeurs  
**Critère:** Fonctions courtes (<50 lignes), noms explicites  
**Priorité:** MOYENNE

**REQ-NF-005** : Modularité  
**Description:** Chaque type de vulnérabilité doit être isolé dans une fonction distincte  
**Critère:** Une fonction = une vulnérabilité  
**Priorité:** HAUTE

**REQ-NF-006** : Évolutivité  
**Description:** Possibilité d'ajouter facilement de nouvelles vulnérabilités sans impacter les existantes  
**Critère:** Architecture modulaire, pas de dépendances croisées  
**Priorité:** MOYENNE

### 4.3 Exigences de Performance
**Source:** Déduction contexte test  
**Confiance:** 🟡 MOYENNE

**REQ-NF-007** : Temps d'Analyse  
**Description:** Le code doit pouvoir être analysé par l'AI en moins de 5 minutes  
**Critère:** <1000 lignes de code total  
**Priorité:** BASSE

**REQ-NF-008** : Légèreté Repository  
**Description:** Le repository doit rester léger pour faciliter les clones et tests répétés  
**Critère:** <10 MB total  
**Priorité:** BASSE

### 4.4 Exigences de Compatibilité
**Source:** Technologies utilisées  
**Confiance:** 🟢 ÉLEVÉE

**REQ-NF-009** : Compatibilité Python  
**Description:** Code Python compatible avec versions 3.8+  
**Critère:** Pas de dépendances à des features Python 3.11+  
**Priorité:** MOYENNE

**REQ-NF-010** : Compatibilité JavaScript  
**Description:** Code JavaScript compatible avec navigateurs modernes (ES6+)  
**Critère:** Pas de features expérimentales  
**Priorité:** MOYENNE