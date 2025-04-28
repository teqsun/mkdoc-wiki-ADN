console.log("Liste des IDs présents :");
document.querySelectorAll('a[id]').forEach(a => {
    console.log(a.id);
});


document.addEventListener('keydown', function(event) {
    // Vérifie que l'utilisateur n'est pas en train de taper dans un champ texte
    const activeElement = document.activeElement;
    if (activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA' || activeElement.isContentEditable) {
        return;
    }

    // Affiche une alerte pour vérifier (optionnel)
    // alert('Touche pressée : ' + event.key);

    // Récupère la touche pressée
    const key = event.key.toLowerCase();

    // Vérifie que c'est une lettre
    if (key.length === 1 && key >= 'a' && key <= 'z') {
        // Cherche l'ancre correspondante
        let anchor = document.getElementById(key);

        // Si l'ancre est trouvée, cherche le titre suivant
        if (anchor) {
            let nextHeading = anchor.nextElementSibling;
            while (nextHeading && nextHeading.tagName !== 'H2') {
                nextHeading = nextHeading.nextElementSibling;
            }
            if (nextHeading) {
                nextHeading.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }
});
