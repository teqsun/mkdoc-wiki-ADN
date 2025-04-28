document.addEventListener('keypress', function(event) {
    // Vérifie que l'utilisateur n'est pas en train de taper dans un champ texte
    const activeElement = document.activeElement;
    if (activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA' || activeElement.isContentEditable) {
        return;
    }

    // Récupère la touche pressée
    const key = event.key.toLowerCase();

    // Vérifie que c'est une lettre
    if (key.length === 1 && key >= 'a' && key <= 'z') {
        event.preventDefault(); // 🔥 Empêche le comportement par défaut du navigateur si possible

        const target = document.getElementById(key);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            console.log("Scroll vers :" + key);
        } else {
            console.log("Pas d'élément trouvé pour :" + key);
        }
    }
});
