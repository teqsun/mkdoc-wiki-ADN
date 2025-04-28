document.addEventListener('keydown', function(event) {
    // Vérifie que l'utilisateur n'est pas en train de taper dans un champ texte
    const activeElement = document.activeElement;
    if (activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA' || activeElement.isContentEditable) {
        return;
    }

    // Récupère la touche pressée
    const key = event.key.toLowerCase();

    // Vérifie que c'est une lettre entre a et z
    if (key.length === 1 && key >= 'a' && key <= 'z') {
        const anchor = document.getElementById(key);
        if (anchor) {
            anchor.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
});
