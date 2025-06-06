window.addEventListener("DOMContentLoaded", () => {
  const langButton = document.querySelector('.md-header__button.md-icon[aria-label*="langue"], .md-header__button.md-icon[aria-label*="language"]');
  if (!langButton) return;

  const path = window.location.pathname;
  const isEnglish = path.startsWith("/en/");
  langButton.setAttribute("data-lang", isEnglish ? "EN" : "FR");
});
