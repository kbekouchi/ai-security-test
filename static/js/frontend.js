/**
 * Frontend JavaScript - CONTIENT DES VULNÉRABILITÉS XSS
 */

function displayUserInput(input) {
    // VULNÉRABILITÉ: XSS via innerHTML
    document.getElementById('content').innerHTML = input;
}

function loadUserData(userData) {
    // VULNÉRABILITÉ: XSS dans l'affichage  
    document.write('<h2>Données utilisateur:</h2>');
    document.write('<p>' + userData + '</p>');
}

function executeUserScript(script) {
    // VULNÉRABILITÉ: Eval dangereux
    eval(script);
}

function updateProfile() {
    const username = document.getElementById('username').value;
    
    // VULNÉRABILITÉ: XSS via setAttribute
    document.getElementById('welcome').setAttribute('data-user', username);
    
    // VULNÉRABILITÉ: XSS via outerHTML
    document.getElementById('display').outerHTML = 
        '<div id="display">Bonjour ' + username + '!</div>';
}

// VULNÉRABILITÉ: Clé API exposée côté client
const CONFIG = {
    apiKey: 'ak_live_abcdefghijklmnopqrstuvwxyz123456',
    secretToken: 'tok_secret_987654321abcdefgh',
    stripeKey: 'pk_live_1234567890abcdefghijklmnop'
};

function sendAnalytics(data) {
    // VULNÉRABILITÉ: Transmission non sécurisée
    fetch('http://analytics.example.com/track', {
        method: 'POST',
        body: JSON.stringify({
            secret: CONFIG.secretToken,
            data: data
        })
    });
}
