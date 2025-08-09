"""
Test file pour déclencher l'analyse multi-agent AST
Contient des vulnérabilités et problèmes détectés par nos 4 agents restaurés
"""

import sqlite3
import requests

# Secret exposé (Security Agent)
API_KEY = "sk-1234567890abcdef1234567890abcdef12345678901234567890"
DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"

def vulnerable_function(param1, param2, param3, param4, param5, param6, param7, param8):
    """Fonction avec trop de paramètres (SonarQube Agent)"""
    magic_number = 42  # Magic number (SonarQube Agent)
    another_magic = 3.14159
    
    # SQL Injection vulnérabilité (Security Agent) 
    query = f"SELECT * FROM users WHERE id = {param1}"
    conn = sqlite3.connect("database.db")  # Hard-coded dependency (Architecture Agent)
    cursor = conn.execute(query)
    
    # Complexité cognitive élevée (SonarQube Agent)
    try:
        if param1 > 100:
            if param2 < 50:
                if param3 == "special":
                    if param4 is not None:
                        if param5 > magic_number:  # Deep nesting
                            result = param1 * another_magic + param6
                            # Loops imbriqués O(n²) (Performance Agent)
                            for i in range(param7):
                                for j in range(param8):
                                    if i * j == magic_number:
                                        # I/O synchrone bloquant (Performance Agent)
                                        response = requests.get("https://api.example.com/data")
                                        result += i + j
                                        break
                            return result
                        else:
                            return param1 + param2
                    else:
                        return param3
                else:
                    return param4
            else:
                return param5
        else:
            return param6
    except:
        pass  # Empty catch block (Architecture Agent)

# God Object (Architecture Agent)
class MassiveController:
    """Classe avec trop de responsabilités"""
    def method1(self): pass
    def method2(self): pass
    def method3(self): pass
    def method4(self): pass
    def method5(self): pass
    def method6(self): pass
    def method7(self): pass
    def method8(self): pass
    def method9(self): pass
    def method10(self): pass
    def method11(self): pass
    def method12(self): pass
    def method13(self): pass
    def method14(self): pass
    def method15(self): pass
    def method16(self): pass
    def method17(self): pass
    def method18(self): pass
    def method19(self): pass
    def method20(self): pass

# Memory leak potential (Performance Agent)
global_cache = {}

def leak_prone_function():
    """N+1 query problem (Performance Agent)"""
    users = [1, 2, 3, 4, 5]
    for user_id in users:
        # Chaque itération fait une requête - N+1 problem
        user_data = requests.get(f"https://api.example.com/users/{user_id}")
        global_cache[user_id] = user_data.json()  # Global state
    
    return global_cache

# Code dupliqué (SonarQube Agent)
def duplicated_logic_1():
    magic = 42
    pi = 3.14159
    try:
        if True:
            result = magic * pi
            for x in range(10):
                for y in range(10):
                    if x * y == magic:
                        result += x + y
        return result
    except:
        pass

def duplicated_logic_2():
    magic = 42  
    pi = 3.14159
    try:
        if True:
            result = magic * pi
            for x in range(10):
                for y in range(10):
                    if x * y == magic:
                        result += x + y
        return result
    except:
        pass