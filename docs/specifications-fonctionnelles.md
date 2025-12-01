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
**Description:** La fonction `displayUserInput()` doit injecter directement du contenu utilisateur via innerHTML sans sanitization  
**Traçabilité:** frontend.js:displayUserInput()  
**Criticité:** Haute (vulnérabilité intentionnelle)

**REQ-FUNC-002** : Exposition XSS via document.write  
**Description:** La fonction `loadUserData()` doit utiliser document.write avec données non échappées  
**Traçabilité:** frontend.js:loadUserData()  
**Criticité:** Haute

**REQ-FUNC-003** : Utilisation dangereuse de eval()  
**Description:** La fonction `executeUserScript()` doit exécuter du code JavaScript arbitraire via eval()  
**Traçabilité:** frontend.js:executeUserScript()  
**Criticité:** Critique

### 3.2 Exigences de Command Injection
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-004** : Command Injection via os.system  
**Description:** La fonction `execute_command()` doit permettre l'injection de commandes via os.system  
**Traçabilité:** helpers.py:execute_command()  
**Criticité:** Critique

**REQ-FUNC-005** : Command Injection via subprocess  
**Description:** La fonction `run_shell_command()` doit utiliser subprocess.run avec shell=True  
**Traçabilité:** helpers.py:run_shell_command()  
**Criticité:** Critique

### 3.3 Exigences d'Insecure Deserialization
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-006** : Désérialisation pickle non sécurisée  
**Description:** La fonction `deserialize_data()` doit utiliser pickle.loads sur données non fiables  
**Traçabilité:** helpers.py:deserialize_data()  
**Criticité:** Critique

### 3.4 Exigences de Path Traversal
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-007** : Path Traversal dans lecture fichiers  
**Description:** La fonction `read_file()` doit permettre la lecture de fichiers arbitraires  
**Traçabilité:** helpers.py:read_file()  
**Criticité:** Haute

### 3.5 Exigences de Hardcoded Secrets
**Source:** Analyse frontend.js et helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-008** : Clés API hardcodées côté client  
**Description:** La fonction `sendAnalytics()` doit contenir une clé API en dur  
**Traçabilité:** frontend.js:sendAnalytics()  
**Criticité:** Haute

**REQ-FUNC-009** : Credentials hardcodés backend  
**Description:** La fonction `backup_database()` doit contenir des credentials en clair  
**Traçabilité:** helpers.py:backup_database()  
**Criticité:** Critique

---

## SECTION 4 : EXIGENCES NON-FONCTIONNELLES

### 4.1 Exigences de Sécurité (Intentionnellement Non Respectées)
**Source:** Contexte repository de test  
**Confiance:** 🟢 ÉLEVÉE

**REQ-NFR-001** : Vulnérabilités détectables  
**Description:** Chaque vulnérabilité doit être suffisamment évidente pour être détectée par une plateforme d'AI Code Review  
**Criticité:** Haute  
**Validation:** Code review manuel + test plateforme IA

**REQ-NFR-002** : Diversité des vulnérabilités  
**Description:** Le repository doit couvrir au minimum 8 types de vulnérabilités différentes (XSS, Command Injection, Insecure Deserialization, Path Traversal, Hardcoded Secrets, eval(), HTTP, Dynamic Import)  
**Criticité:** Moyenne  
**Validation:** Checklist des types de vulnérabilités

**REQ-NFR-003** : Réalisme des scénarios  
**Description:** Les vulnérabilités doivent ressembler à du code réel (pas de patterns trop évidents ou artificiels)  
**Criticité:** Moyenne  
**Validation:** Review par équipe sécurité

### 4.2 Exigences de Maintenabilité
**Source:** Bonnes pratiques repository de test  
**Confiance:** 🟡 MOYENNE

**REQ-NFR-004** : Documentation des vulnérabilités  
**Description:** Chaque vulnérabilité doit être documentée avec son type, sa localisation et son impact potentiel  
**Criticité:** Moyenne  
**Validation:** Présence de documentation complète

**REQ-NFR-005** : Code commenté  
**Description:** Les sections vulnérables doivent contenir des commentaires explicatifs pour les testeurs  
**Criticité:** Faible  
**Validation:** Review du code

### 4.3 Exigences de Performance
**Source:** Déduction contexte test  
**Confiance:** 🟡 MOYENNE

**REQ-NFR-006** : Temps d'analyse acceptable  
**Description:** Le repository doit pouvoir être analysé par une plateforme IA en moins de 5 minutes  
**Criticité:** Faible  
**Validation:** Test chronométré

**REQ-NFR-007** : Taille de repository raisonnable  
**Description:** Le repository ne doit pas dépasser 100 fichiers pour faciliter les tests  
**Criticité:** Faible  
**Validation:** Comptage fichiers

### 4.4 Exigences de Compatibilité
**Source:** Analyse langages utilisés  
**Confiance:** 🟢 ÉLEVÉE

**REQ-NFR-008** : Support Python 3.x  
**Description:** Le code Python doit être compatible Python 3.7+  
**Criticité:** Moyenne  
**Validation:** Test exécution

**REQ-NFR-009** : Support JavaScript moderne  
**Description:** Le code JavaScript doit utiliser ES6+ pour refléter les pratiques actuelles  
**Criticité:** Moyenne  
**Validation:** Test navigateurs modernes

---