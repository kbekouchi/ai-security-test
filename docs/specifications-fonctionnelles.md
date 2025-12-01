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
**Description:** La fonction `displayUserInput()` doit accepter du contenu utilisateur non sanitizé et l'injecter directement via innerHTML  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-001  
**Source:** `static/js/frontend.js:6`

**REQ-FUNC-002** : Exposition XSS via document.write  
**Description:** La fonction `loadUserData()` doit utiliser document.write pour afficher des données utilisateur sans validation  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-001  
**Source:** `static/js/frontend.js:11-12`

**REQ-FUNC-003** : Exposition XSS via outerHTML  
**Description:** La fonction `updateProfile()` doit permettre l'injection de contenu via outerHTML sans échappement  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-001  
**Source:** `static/js/frontend.js:28-29`

### 3.2 Exigences de Command Injection
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-004** : Exécution commande système directe  
**Description:** La fonction `execute_command()` doit exécuter des commandes utilisateur via os.system() sans validation  
**Priorité:** CRITIQUE  
**Traçabilité:** OBJ-002, PÉRIM-IN-002  
**Source:** `utils/helpers.py:8-11`

**REQ-FUNC-005** : Subprocess avec shell=True  
**Description:** La fonction `run_shell_command()` doit utiliser subprocess.run avec shell=True sur input utilisateur  
**Priorité:** CRITIQUE  
**Traçabilité:** OBJ-002, PÉRIM-IN-002  
**Source:** `utils/helpers.py:16-18`

### 3.3 Exigences de Secrets Exposés
**Source:** Analyse frontend.js  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-006** : Clés API hardcodées côté client  
**Description:** Le code doit contenir des clés API, tokens secrets et clés Stripe en clair dans le JavaScript  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-005  
**Source:** `static/js/frontend.js:33-37`

**REQ-FUNC-007** : Credentials en clair dans commandes  
**Description:** La fonction `backup_database()` doit contenir username/password MySQL en clair dans la commande  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-005  
**Source:** `utils/helpers.py:33-35`

### 3.4 Exigences d'Injection de Code
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-008** : Utilisation dangereuse de eval()  
**Description:** Les fonctions `executeUserScript()` et `calculate()` doivent utiliser eval() sur input utilisateur  
**Priorité:** CRITIQUE  
**Traçabilité:** OBJ-002, PÉRIM-IN-006  
**Source:** `static/js/frontend.js:16`, `utils/helpers.py:44`

**REQ-FUNC-009** : Désérialisation pickle non sécurisée  
**Description:** La fonction `deserialize_data()` doit utiliser pickle.loads() sur données non fiables  
**Priorité:** CRITIQUE  
**Traçabilité:** OBJ-002, PÉRIM-IN-003  
**Source:** `utils/helpers.py:23-25`

**REQ-FUNC-010** : Import dynamique non contrôlé  
**Description:** La fonction `import_module_dynamic()` doit permettre l'import de modules arbitraires via __import__  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-008  
**Source:** `utils/helpers.py:39-40`

### 3.5 Exigences de Path Traversal
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-011** : Lecture fichier sans validation  
**Description:** La fonction `read_file()` doit accepter des chemins relatifs sans validation permettant ../  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-004  
**Source:** `utils/helpers.py:28-30`

### 3.6 Exigences de Transmission Non Sécurisée
**Source:** Analyse frontend.js  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-012** : Transmission HTTP de secrets  
**Description:** La fonction `sendAnalytics()` doit transmettre des tokens secrets via HTTP (non HTTPS)  
**Priorité:** HAUTE  
**Traçabilité:** OBJ-002, PÉRIM-IN-007  
**Source:** `static/js/frontend.js:39-45`

---

## SECTION 4 : USER STORIES ET CAS D'USAGE

*(Section à compléter)*

---

## SECTION 5 : RÈGLES MÉTIER

*(Section à compléter)*

---

## SECTION 6 : MATRICES DE TRAÇABILITÉ

*(Section à compléter)*

---

## SECTION 7 : ANNEXES

*(Section à compléter)*

---

## SECTION 8 : LISTE DE VALIDATION PRIORITAIRE

### Questions Critiques (🔴)
*Aucune - Code source disponible*

### Questions Importantes (🟡)
1. **Validation Périmètre Exclu** : Confirmer que les corrections automatiques sont hors scope
2. **Validation Objectifs** : Confirmer que le repository sert uniquement de benchmark de test
3. **Ajout Vulnérabilités** : D'autres types de vulnérabilités doivent-ils être ajoutés ?

### Informations Manquantes (⚪)
1. Critères de succès précis pour la détection par l'IA
2. Format attendu des rapports d'analyse
3. Métriques de performance attendues (taux de détection, faux positifs)

---

**Document généré par:** Agent Spécifications Fonctionnelles  
**Dernière mise à jour:** 2025-01-21