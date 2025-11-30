# Spécifications Fonctionnelles - AI Security Test Repository

**Version:** 1.0  
**Date:** 2025-01-28  
**Statut:** Draft  
**Niveau de confiance global:** 🟢 95%

---

## 📋 Métadonnées du document

| Élément | Valeur |
|---------|--------|
| **Repository** | kbekouchi/ai-security-test |
| **Langage principal** | Python (Flask) + JavaScript |
| **Branche par défaut** | main |
| **Type de projet** | Repository de test - Sécurité applicative |
| **Sources analysées** | ✅ README.md, ✅ Code source (3 fichiers), ✅ Structure complète |

---

## 1. CONTEXTE ET OBJECTIFS 🎯

**Niveau de confiance:** 🟢 95%

### 1.1 Contexte général

**Source:** `README.md` (ligne 2)

Ce repository est un **environnement de test intentionnellement vulnérable** conçu pour servir de base de validation pour une plateforme d'AI Code Review. Il contient des vulnérabilités de sécurité délibérément introduites pour tester la capacité d'outils d'analyse automatisée à détecter des failles critiques.

**Traçabilité:**
- 🔗 `README.md:2` - "Contient des vulnérabilités intentionnelles"
- 🔗 `web/views.py:1` - "CONTIENT DES VULNÉRABILITÉS XSS"
- 🔗 `utils/helpers.py:1` - "VULNÉRABILITÉS DIVERSES"
- 🔗 `static/js/frontend.js:2` - "CONTIENT DES VULNÉRABILITÉS XSS"

### 1.2 Objectifs du projet

| Objectif | Description | Priorité | Source |
|----------|-------------|----------|--------|
| **OBJ-01** | Fournir un environnement de test réaliste avec vulnérabilités connues | ⭐⭐⭐ Critique | README.md |
| **OBJ-02** | Valider la détection de vulnérabilités XSS (Cross-Site Scripting) | ⭐⭐⭐ Critique | views.py, frontend.js |
| **OBJ-03** | Valider la détection de Command Injection | ⭐⭐⭐ Critique | views.py, helpers.py |
| **OBJ-04** | Tester la détection de credentials hardcodés | ⭐⭐ Haute | helpers.py:35 |
| **OBJ-05** | Tester la détection d'exposition de secrets (API keys) | ⭐⭐ Haute | frontend.js:32-36 |
| **OBJ-06** | Valider la détection de désérialisation non sécurisée | ⭐⭐ Haute | helpers.py:20-23 |
| **OBJ-07** | Tester la détection de Path Traversal | ⭐⭐ Haute | helpers.py:25-29 |
| **OBJ-08** | Identifier les mauvaises pratiques (debug mode en production) | ⭐ Moyenne | views.py:40 |

### 1.3 Parties prenantes

**Niveau de confiance:** 🟡 60% (inféré)

| Rôle | Responsabilité | Implication |
|------|----------------|-------------|
| **Équipe Sécurité** | Validation des vulnérabilités | Haute |
| **Équipe AI/ML** | Entraînement et validation des modèles de détection | Haute |
| **Développeurs** | Compréhension des patterns vulnérables | Moyenne |
| **DevSecOps** | Intégration dans les pipelines CI/CD | Moyenne |

---

## 2. PÉRIMÈTRE FONCTIONNEL 📦

**Niveau de confiance:** 🟢 98%

### 2.1 Dans le périmètre ✅

#### 2.1.1 Composants applicatifs

**Source:** Structure repository analysée via `github_get_tree`

| Composant | Fichier | Taille | Vulnérabilités incluses | Confiance |
|-----------|---------|--------|------------------------|----------|
| **Application Web Flask** | `web/views.py` | 1175 octets | XSS (×2), Command Injection, Debug mode | 🟢 100% |
| **Utilitaires Backend** | `utils/helpers.py` | 1464 octets | Command Injection (×2), Pickle deserialization, Path Traversal, Hardcoded credentials, eval() | 🟢 100% |
| **Frontend JavaScript** | `static/js/frontend.js` | 1371 octets | XSS (×4), Secrets exposés, eval(), HTTP non sécurisé | 🟢 100% |
| **Configuration** | `.gitignore` | 4688 octets | Gestion des fichiers ignorés | 🟢 100% |
| **Documentation** | `README.md` | 120 octets | Description du projet | 🟢 100% |

#### 2.1.2 Types de vulnérabilités couvertes

**Traçabilité complète:**

1. **XSS (Cross-Site Scripting)** - 6 instances
   - 🔗 `views.py:14` - Template non échappé avec f-string
   - 🔗 `views.py:27` - Retour HTML direct avec input utilisateur
   - 🔗 `frontend.js:6` - innerHTML avec input utilisateur
   - 🔗 `frontend.js:11-12` - document.write() avec données utilisateur
   - 🔗 `frontend.js:23` - setAttribute() avec input non sanitisé
   - 🔗 `frontend.js:26-27` - outerHTML avec concaténation

2. **Command Injection** - 4 instances
   - 🔗 `views.py:35` - os.system() avec paramètre utilisateur
   - 🔗 `helpers.py:9` - os.system() avec commande utilisateur
   - 🔗 `helpers.py:15` - subprocess.run() avec shell=True
   - 🔗 `helpers.py:35` - os.system() avec credentials hardcodés

3. **Code Injection** - 2 instances
   - 🔗 `frontend.js:16` - eval() sur script utilisateur
   - 🔗 `helpers.py:47` - eval() sur expression utilisateur

4. **Désérialisation non sécurisée** - 1 instance
   - 🔗 `helpers.py:22` - pickle.loads() sur données non fiables

5. **Path Traversal** - 1 instance
   - 🔗 `helpers.py:28` - open() avec concaténation de filename utilisateur

6. **Secrets exposés** - 4 instances
   - 🔗 `helpers.py:35` - Mot de passe MySQL en clair
   - 🔗 `frontend.js:32` - Clé API exposée
   - 🔗 `frontend.js:33` - Token secret exposé
   - 🔗 `frontend.js:34` - Clé Stripe exposée

7. **Mauvaises pratiques** - 2 instances
   - 🔗 `views.py:40` - Debug mode activé en production
   - 🔗 `frontend.js:41` - Transmission HTTP non sécurisée

### 2.2 Hors périmètre ❌

**Niveau de confiance:** 🟢 90%

| Élément | Raison | Confiance |
|---------|--------|----------|
| **Tests unitaires** | Aucun fichier de test détecté | 🟢 100% |
| **Configuration Docker** | Aucun Dockerfile ou docker-compose.yml | 🟢 100% |
| **Base de données** | Aucun schéma ou migration détecté | 🟢 100% |
| **API REST complète** | Seulement 3 routes de démonstration | 🟢 100% |
| **Authentification** | Non implémentée | 🟢 100% |
| **Logging** | Non implémenté | 🟢 100% |
| **Environnement de production réel** | Repository de test uniquement | 🟢 100% |
| **Vulnérabilités infrastructure** | Focus sur le code applicatif | 🟡 80% |

### 2.3 Limites et contraintes

**Source:** Analyse du code et structure

| Type | Contrainte | Impact | Source |
|------|-----------|--------|--------|
| **Technique** | Python Flask requis | Installation des dépendances nécessaire | views.py:3 |
| **Sécurité** | ⚠️ NE JAMAIS déployer en production | Vulnérabilités intentionnelles critiques | README.md |
| **Usage** | Environnement isolé obligatoire | Risque d'exploitation réelle | Toutes les vulnérabilités |
| **Scope** | Limité aux vulnérabilités applicatives | Pas de tests infrastructure | Structure projet |

### 2.4 Dépendances identifiées

**Niveau de confiance:** 🟡 70% (inféré du code)

```python
# Dépendances Python détectées
Flask           # views.py:3
os              # views.py:4, helpers.py:3
subprocess      # helpers.py:4
pickle          # helpers.py:5
```

**Note:** ⚪ Aucun fichier `requirements.txt` ou `pyproject.toml` détecté - Confiance 60%

---

## 📊 Statistiques du périmètre

| Métrique | Valeur | Source |
|----------|--------|--------|
| **Fichiers Python** | 2 | Structure repository |
| **Fichiers JavaScript** | 1 | Structure repository |
| **Total lignes de code** | ~100 lignes | Estimation basée sur tailles |
| **Vulnérabilités uniques** | 20 instances | Analyse complète |
| **Catégories de vulnérabilités** | 7 types | Classification OWASP |
| **Criticité moyenne** | Critique/Haute | Évaluation sécurité |

---

**Prochaines sections:** 3. Exigences fonctionnelles, 4. Cas d'usage, 5. Exigences de sécurité
