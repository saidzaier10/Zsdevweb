<template>
  <div id="app" class="relative">
    <Navbar @show-devis="showDevisSection" />
    <Home />
    <About />
    <Portfolio />
    <Skills />
    <Contact />
    <Devis id="devis" :isDevisSectionVisible="isDevisSectionVisible" />
    <Footer />
    <button
      @click="scrollToTop"
      :class="{'opacity-100 visible': isScrollButtonVisible, 'opacity-0 invisible': !isScrollButtonVisible}"
      class="scroll-to-top fixed bottom-4 right-4 bg-blue-600 text-white p-3 rounded-full shadow-lg hover:bg-blue-700 transition-opacity duration-300"
      aria-label="Retour en haut de la page"
    >
      <font-awesome-icon icon="arrow-up" class="text-xl"/>
    </button>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Home from './components/Home.vue';
import About from './components/About.vue';
import Portfolio from './components/Portfolio.vue';
import Skills from './components/Skills.vue';
import Contact from './components/Contact.vue';
import Devis from './components/Devis.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Home,
    About,
    Portfolio,
    Skills,
    Contact,
    Devis,
    Footer,
  },
  data() {
    return {
      isScrollButtonVisible: false,
      isDevisSectionVisible: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.isScrollButtonVisible = window.scrollY > 300;
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    showDevisSection() {
      this.isDevisSectionVisible = true;
      this.$nextTick(() => {
        const devisSection = document.getElementById('devis');
        if (devisSection) {
          devisSection.scrollIntoView({ behavior: 'smooth' });
        }
      });
    },
  },
};
</script>

<style>
/* Supprimez ce style si vous utilisez Tailwind pour les transitions */
</style>