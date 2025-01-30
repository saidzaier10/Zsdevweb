<template>
  <nav :class="{'nav-hidden': !isNavVisible, 'nav-visible': isNavVisible}" class="fixed w-full z-20 bg-white shadow">
    <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
      <div class="text-2xl font-bold text-gray-900">ZSdevweb</div>
      <div class="hidden md:flex space-x-8">
        <a href="#accueil" @click="scrollToSection" class="text-gray-700 hover:text-blue-600">Accueil</a>
        <a href="#apropos" @click="scrollToSection" class="text-gray-700 hover:text-blue-600">À propos</a>
        <a href="#portfolio" @click="scrollToSection" class="text-gray-700 hover:text-blue-600">Portfolio</a>
        <a href="#competences" @click="scrollToSection" class="text-gray-700 hover:text-blue-600">Compétences</a>
        <a href="#devis" @click="showDevisSection" class="text-gray-700 hover:text-blue-600">Devis</a>
        <a href="#contact" @click="scrollToSection" class="text-gray-700 hover:text-blue-600">Contact</a>
      </div>
      <button @click="toggleMobileMenu" class="md:hidden text-gray-700 focus:outline-none" aria-label="Ouvrir/Fermer le menu">
        <i class="fas fa-bars text-2xl"></i>
      </button>
    </div>
    <div class="md:hidden fixed left-0 top-[4rem] h-full bg-white w-64 shadow-lg transform transition-transform duration-300"
         :class="isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full'">
      <div class="flex flex-col space-y-4 p-6">
        <a href="#accueil" @click="closeMobileMenu" class="text-gray-700 hover:text-blue-600">Accueil</a>
        <a href="#apropos" @click="closeMobileMenu" class="text-gray-700 hover:text-blue-600">À propos</a>
        <a href="#portfolio" @click="closeMobileMenu" class="text-gray-700 hover:text-blue-600">Portfolio</a>
        <a href="#competences" @click="closeMobileMenu" class="text-gray-700 hover:text-blue-600">Compétences</a>
        <a href="#devis" @click="showDevisSection" class="text-gray-700 hover:text-blue-600">Devis</a>
        <a href="#contact" @click="closeMobileMenu" class="text-gray-700 hover:text-blue-600">Contact</a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isNavVisible: true, // Contrôle la visibilité de la barre de navigation
      isMobileMenuOpen: false, // Contrôle l'état du menu mobile
    };
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen; // Bascule le menu mobile
    },
    closeMobileMenu() {
      this.isMobileMenuOpen = false; // Ferme le menu mobile
    },
    showDevisSection() {
      this.$emit('show-devis'); // Émet un événement pour afficher la section "Devis"
    },
    scrollToSection(event) {
      event.preventDefault(); // Empêche le comportement par défaut du lien
      const targetId = event.target.getAttribute('href').substring(1); // Récupère l'ID de la cible
      const targetElement = document.getElementById(targetId); // Trouve l'élément cible
      if (targetElement) {
        targetElement.scrollIntoView({ behavior: 'smooth' }); // Défile jusqu'à la cible
      }
    },
    handleResize() {
      if (window.innerWidth >= 768) { // Si l'écran est large
        this.isMobileMenuOpen = false; // Masque le menu mobile
      }
    },
  },
  created() {
    window.addEventListener('resize', this.handleResize); // Écoute le redimensionnement de la fenêtre
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize); // Nettoie l'écouteur d'événement
  },
};
</script>