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
**Description:** La fonction `displayUserInput()` doit injecter directement du contenu utilisateur via `innerHTML` sans sanitization  
**Trace:** `static/js/frontend.js` ligne displayUserInput()  
**Priorité:** P1 (Critique pour test)

**REQ-FUNC-002** : Exposition XSS via document.write  
**Description:** La fonction `loadUserData()` doit utiliser `document.write()` avec données non validées  
**Trace:** `static/js/frontend.js` ligne loadUserData()  
**Priorité:** P1

**REQ-FUNC-003** : Utilisation dangereuse de eval()  
**Description:** La fonction `executeUserScript()` doit exécuter du code via `eval()` sur input utilisateur  
**Trace:** `static/js/frontend.js` ligne executeUserScript()  
**Priorité:** P1

### 3.2 Exigences de Command Injection
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-004** : Command Injection via os.system  
**Description:** La fonction `execute_command()` doit utiliser `os.system()` avec input non sanitizé  
**Trace:** `utils/helpers.py` ligne execute_command()  
**Priorité:** P1

**REQ-FUNC-005** : Command Injection via subprocess  
**Description:** La fonction `run_shell_command()` doit utiliser `subprocess.run()` avec `shell=True`  
**Trace:** `utils/helpers.py` ligne run_shell_command()  
**Priorité:** P1

### 3.3 Exigences de Désérialisation Dangereuse
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-006** : Insecure Deserialization  
**Description:** La fonction `deserialize_data()` doit utiliser `pickle.loads()` sur données non fiables  
**Trace:** `utils/helpers.py` ligne deserialize_data()  
**Priorité:** P1

### 3.4 Exigences de Path Traversal
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-007** : Path Traversal  
**Description:** La fonction `read_file()` doit permettre accès fichiers via chemins non validés  
**Trace:** `utils/helpers.py` ligne read_file()  
**Priorité:** P2

### 3.5 Exigences de Secrets Hardcodés
**Source:** Analyse frontend.js et helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-008** : Hardcoded API Keys (Frontend)  
**Description:** La fonction `sendAnalytics()` doit contenir des clés API en clair dans le code JavaScript  
**Trace:** `static/js/frontend.js` ligne sendAnalytics()  
**Priorité:** P2

**REQ-FUNC-009** : Hardcoded Credentials (Backend)  
**Description:** La fonction `backup_database()` doit contenir identifiants BDD en clair  
**Trace:** `utils/helpers.py` ligne backup_database()  
**Priorité:** P2

---

## SECTION 4 : EXIGENCES NON-FONCTIONNELLES

### 4.1 Exigences de Sécurité (Intentionnellement Non Respectées)
**Source:** Contexte repository de test  
**Confiance:** 🟢 ÉLEVÉE

**REQ-NF-001** : Absence de Validation d'Entrées  
**Description:** Le système NE DOIT PAS valider les entrées utilisateur pour exposer les vulnérabilités  
**Justification:** Permettre la détection par l'IA des failles de validation  
**Priorité:** P1

**REQ-NF-002** : Absence de Sanitization  
**Description:** Aucune sanitization HTML/SQL/Shell ne doit être implémentée  
**Justification:** Tester la capacité de l'IA à détecter les failles de sanitization  
**Priorité:** P1

**REQ-NF-003** : Exposition de Secrets  
**Description:** Les secrets doivent être hardcodés et visibles dans le code  
**Justification:** Tester la détection de credentials exposés  
**Priorité:** P2

### 4.2 Exigences de Maintenabilité
**Source:** Bonnes pratiques repository de test  
**Confiance:** 🟡 MOYENNE

**REQ-NF-004** : Documentation des Vulnérabilités  
**Description:** Chaque vulnérabilité doit être documentée avec son type et son impact  
**Justification:** Faciliter la validation des résultats de l'IA  
**Priorité:** P2

**REQ-NF-005** : Code Lisible  
**Description:** Le code vulnérable doit rester lisible et compréhensible  
**Justification:** Permettre l'analyse manuelle et la validation  
**Priorité:** P3

### 4.3 Exigences de Testabilité
**Source:** Objectif du repository  
**Confiance:** 🟡 MOYENNE

**REQ-NF-006** : Reproductibilité  
**Description:** Les vulnérabilités doivent être reproductibles de manière déterministe  
**Justification:** Garantir des résultats de test cohérents  
**Priorité:** P2

**REQ-NF-007** : Isolation  
**Description:** Le repository doit être isolé et ne jamais être déployé en production  
**Justification:** Éviter tout risque réel de sécurité  
**Priorité:** P1

### 4.4 Exigences de Performance
**Source:** Déduction contexte test  
**Confiance:** 🟡 MOYENNE

**REQ-NF-008** : Temps d'Analyse  
**Description:** Le code doit permettre une analyse complète en moins de 5 minutes  
**Justification:** Efficacité des tests de la plateforme AI  
**Priorité:** P3

**REQ-NF-009** : Taille Raisonnable  
**Description:** Le repository doit rester de taille modérée (< 1 MB)  
**Justification:** Faciliter le clonage et l'analyse rapide  
**Priorité:** P3