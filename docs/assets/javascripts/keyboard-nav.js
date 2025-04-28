document.addEventListener('keypress', function(event) {
    const key = event.key.toLowerCase();

    // Vérifie que c'est une lettre
    if (key.length === 1 && key >= 'a' && key <= 'z') {
        const target = document.getElementById(key);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            console.log("Scroll vers :" + key);
        } else {
            console.log("Pas d'élément trouvé pour :" + key);
        }
    }
});
