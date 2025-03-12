<template>
  <section 
    id="portfolio" 
    class="relative overflow-hidden bg-gray-900 py-20"
    @mouseenter="pauseAutoScroll"
    @mouseleave="resumeAutoScroll"
  >
    <div class="px-6">
      <h2 class="mb-16 text-center text-4xl font-bold text-white" data-aos="fade-up">Portfolio</h2>

      <!-- Carousel -->
      <div class="relative h-[700px]">
        <div 
          class="flex space-x-8 overflow-x-auto pb-14"
          ref="carousel"
          :style="{ scrollBehavior: 'smooth' }"
        >
          <div 
            v-for="(project, index) in infiniteProjects" 
            :key="index"
            class="group relative h-[600px] w-[90vw] shrink-0 transition-transform duration-500 ease-in-out hover:scale-95"
          >
            <div class="h-full overflow-hidden rounded-3xl bg-black shadow-2xl">
              <img 
                :src="project.image" 
                :alt="project.title" 
                class="h-full w-full object-cover opacity-90 transition-opacity duration-300 group-hover:opacity-100"
              />
              <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black p-8">
                <h3 class="mb-2 text-3xl font-bold text-white">{{ project.title }}</h3>
                <p class="text-gray-300">{{ project.description }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contrôles -->
        <div class="absolute left-0 right-0 top-1/2 flex -translate-y-1/2 justify-between px-6">
          <button 
            @click="previousProject"
            class="rounded-full bg-white/10 p-4 backdrop-blur transition-all hover:bg-white/20"
          >
            <svg class="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
          </button>

          <button 
            @click="nextProject"
            class="rounded-full bg-white/10 p-4 backdrop-blur transition-all hover:bg-white/20"
          >
            <svg class="h-8 w-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </button>
        </div>

        <!-- Pagination -->
        <div class="absolute bottom-8 left-0 right-0 flex justify-center space-x-2">
          <div 
            v-for="(_, index) in projects" 
            :key="index"
            class="h-2 w-8 rounded-full transition-all duration-300"
            :class="index === realIndex ? 'bg-white' : 'bg-gray-600'"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Portfolio',
  data() {
    return {
      realIndex: 0,
      autoScrollInterval: null,
      projects: [
        { 
          id: 1,
          title: 'Portfolio Artistique',
          description: 'Site vitrine moderne pour photographe professionnel',
          image: 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80'
        },
        { 
          id: 2,
          title: 'Boutique en ligne',
          description: 'Plateforme e-commerce pour marque de luxe',
          image: 'https://images.unsplash.com/photo-1607082350899-7e105aa886ae?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1920&q=80'
        },
        { 
          id: 3,
          title: 'Dashboard Analytics',
          description: 'Application web de gestion de données en temps réel',
          image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1920&q=80'
        }
      ]
    }
  },
  computed: {
    infiniteProjects() {
      return [...this.projects, ...this.projects, ...this.projects];
    }
  },
  methods: {
    nextProject() {
      this.realIndex = (this.realIndex + 1) % this.projects.length;
      this.scrollToProject();
    },
    previousProject() {
      this.realIndex = (this.realIndex - 1 + this.projects.length) % this.projects.length;
      this.scrollToProject();
    },
    scrollToProject() {
      const container = this.$refs.carousel;
      const projectWidth = container.offsetWidth * 0.9 + 32; // 90vw + gap
      const middleSection = this.projects.length; // Section médiane des clones
      const targetScroll = (middleSection + this.realIndex) * projectWidth;
      
      container.scrollTo({
        left: targetScroll,
        behavior: 'smooth'
      });
    },
    startAutoScroll() {
      this.autoScrollInterval = setInterval(() => {
        this.nextProject();
      }, 5000);
    },
    pauseAutoScroll() {
      clearInterval(this.autoScrollInterval);
    },
    resumeAutoScroll() {
      this.startAutoScroll();
    }
  },
  mounted() {
    this.startAutoScroll();
    // Position initiale au milieu des clones
    this.$nextTick(() => {
      const container = this.$refs.carousel;
      const projectWidth = container.offsetWidth * 0.9 + 32;
      container.scrollLeft = this.projects.length * projectWidth;
    });
  }
}
</script>

<style scoped>
/* Masquer la barre de défilement */
::-webkit-scrollbar {
  display: none;
}

/* Animation fluide pour le défilement infini */
html {
  scroll-behavior: smooth;
}
</style>