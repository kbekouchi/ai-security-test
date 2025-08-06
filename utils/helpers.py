"""Utilitaires - VULNÉRABILITÉS DIVERSES"""

import os
import subprocess
import pickle

def execute_command(user_cmd):
    """Exécute une commande - VULNÉRABLE Command Injection"""
    
    # VULNÉRABILITÉ: Command injection directe
    result = os.system(user_cmd)
    return result

def run_shell_command(cmd):
    """Exécute via subprocess - VULNÉRABLE aussi"""
    
    # VULNÉRABILITÉ: shell=True avec input utilisateur
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout

def deserialize_data(data):
    """Désérialise des données - VULNÉRABLE"""
    
    # VULNÉRABILITÉ: pickle.loads avec données non fiables
    return pickle.loads(data)

def read_file(filename):
    """Lit un fichier - VULNÉRABLE Path Traversal"""
    
    # VULNÉRABILITÉ: Path traversal possible
    with open(f"/app/data/{filename}", 'r') as f:
        return f.read()

def backup_database():
    """Backup base de données - VULNÉRABLE"""
    
    # VULNÉRABILITÉ: Credentials hardcodés dans commande
    cmd = "mysqldump -u admin -pSecretPass123 production_db > backup.sql"
    os.system(cmd)

# VULNÉRABILITÉ: Import dangereux
def import_module_dynamic(module_name):
    """Import dynamique - VULNÉRABLE"""
    return __import__(module_name)

# VULNÉRABILITÉ: Eval sur input utilisateur  
def calculate(expression):
    """Calculatrice - TRÈS VULNÉRABLE"""
    return eval(expression)  # Ne jamais faire ça !
