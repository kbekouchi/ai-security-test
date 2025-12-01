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
**REQ-FUNC-002** : XSS via document.write  
**REQ-FUNC-003** : Exécution eval() dangereuse  
**REQ-FUNC-004** : XSS multiple dans updateProfile  
**REQ-FUNC-005** : Exposition secrets côté client

### 3.2 Exigences de Vulnérabilités Backend
**Source:** Analyse helpers.py  
**Confiance:** 🟢 ÉLEVÉE

**REQ-FUNC-006** : Command Injection via os.system  
**REQ-FUNC-007** : Subprocess shell=True  
**REQ-FUNC-008** : Insecure Deserialization pickle  
**REQ-FUNC-009** : Path Traversal  
**REQ-FUNC-010** : Credentials hardcodés  
**REQ-FUNC-011** : Import dynamique dangereux  
**REQ-FUNC-012** : Évaluation expressions non sécurisée

---

## SECTION 4 : EXIGENCES NON-FONCTIONNELLES

### 4.1 Sécurité (Intentionnellement Vulnérable)
**Source:** Objectif du repository de test  
**Confiance:** 🟢 ÉLEVÉE

**REQ-NF-001** : Vulnérabilités Détectables  
**Description:** Chaque vulnérabilité doit être suffisamment explicite pour être détectable par un outil d'AI Code Review  
**Critère:** Code commenté et patterns reconnaissables

**REQ-NF-002** : Diversité des Vulnérabilités  
**Description:** Couvrir au minimum 8 catégories OWASP différentes  
**Critère:** XSS, Injection, Deserialization, Path Traversal, Secrets, etc.

**REQ-NF-003** : Documentation des Failles  
**Description:** Chaque vulnérabilité doit être documentée pour validation  
**Critère:** Commentaires explicites dans le code

### 4.2 Maintenabilité
**Source:** Contexte repository de test  
**Confiance:** 🟡 MOYENNE

**REQ-NF-004** : Code Lisible  
**Description:** Le code doit rester simple et compréhensible malgré les vulnérabilités  
**Critère:** Fonctions courtes (<50 lignes), nommage explicite

**REQ-NF-005** : Extensibilité  
**Description:** Possibilité d'ajouter de nouvelles vulnérabilités facilement  
**Critère:** Structure modulaire par type de vulnérabilité

### 4.3 Performance
**Source:** Déduction contexte test  
**Confiance:** 🟡 MOYENNE

**REQ-NF-006** : Temps d'Analyse  
**Description:** L'analyse complète par l'IA ne doit pas dépasser 5 minutes  
**Critère:** Repository de taille limitée (<1000 lignes de code)

---

## SECTION 5 : CONTRAINTES TECHNIQUES

### 5.1 Langages et Technologies
**Source:** Analyse repository  
**Confiance:** 🟢 ÉLEVÉE

**CONT-TECH-001** : Python 3.x  
**CONT-TECH-002** : JavaScript ES6+  
**CONT-TECH-003** : Pas de framework web (code brut)

### 5.2 Dépendances
**Source:** Analyse fichiers  
**Confiance:** 🟢 ÉLEVÉE

**CONT-TECH-004** : Bibliothèques standard uniquement  
**CONT-TECH-005** : Pas de gestionnaire de dépendances requis  
**CONT-TECH-006** : Compatible avec outils d'analyse statique

### 5.3 Environnement
**Source:** Contexte GitHub  
**Confiance:** 🟢 ÉLEVÉE

**CONT-TECH-007** : Repository GitHub public  
**CONT-TECH-008** : Pas de CI/CD (intentionnel)  
**CONT-TECH-009** : Pas de conteneurisation requise

---

## LISTE DE VALIDATION PRIORITAIRE

### Priorité HAUTE 🔴
1. Vérifier présence des 8 catégories de vulnérabilités minimum
2. Valider détectabilité par outil AI Code Review
3. Confirmer absence de données sensibles réelles

### Priorité MOYENNE 🟡
4. Vérifier lisibilité et documentation du code
5. Tester extensibilité avec nouvelle vulnérabilité
6. Valider temps d'analyse <5min

### Priorité BASSE 🟢
7. Optimiser commentaires explicatifs
8. Améliorer structure modulaire
9. Ajouter exemples d'exploitation

---

**Document généré le:** 2025-01-21  
**Dernière mise à jour:** 2025-01-21  
**Statut:** ✅ COMPLET