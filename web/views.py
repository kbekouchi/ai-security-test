"""Vues web - CONTIENT DES VULNÉRABILITÉS XSS"""

from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/profile')
def user_profile():
    """Page de profil utilisateur - VULNÉRABLE XSS"""
    
    username = request.args.get('name', 'Anonymous')
    
    # VULNÉRABILITÉ: XSS via template non échappé
    template = f"""
    <html>
    <body>
        <h1>Profil de {username}</h1>
        <p>Bienvenue {username}!</p>
    </body>
    </html>
    """
    
    return render_template_string(template)

@app.route('/search')  
def search():
    """Recherche - VULNÉRABLE XSS"""
    
    query = request.args.get('q', '')
    
    # VULNÉRABILITÉ: XSS dans la réponse
    return f"<h1>Résultats pour: {query}</h1>"

@app.route('/admin')
def admin_panel():
    """Panel admin - VULNÉRABLE Command Injection"""
    
    command = request.args.get('cmd', 'ls')
    
    # VULNÉRABILITÉ: Command injection
    result = os.system(command)
    
    return f"Commande exécutée: {command}"

# VULNÉRABILITÉ: Debug activé en production
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Dangereux !
