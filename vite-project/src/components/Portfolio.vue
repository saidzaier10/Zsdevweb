<template>
    <section id="portfolio" class="py-16 bg-gray-50">
      <div class="max-w-7xl mx-auto px-6">
        <h2 class="text-3xl font-bold text-gray-900 text-center mb-12" data-aos="fade-up">Portfolio</h2>
        <div class="flex justify-center flex-wrap gap-4 mb-8">
          <button @click="filterProjects('all')" class="btn-secondary">Tous</button>
          <button @click="filterProjects('site-vitrine')" class="btn-secondary">Sites vitrines</button>
          <button @click="filterProjects('e-commerce')" class="btn-secondary">E-commerce</button>
          <button @click="filterProjects('application-web')" class="btn-secondary">Applications web</button>
        </div>
        <div class="grid md:grid-cols-3 gap-8" data-aos="fade-up">
          <div v-for="project in filteredProjects" :key="project.id" class="project-card bg-white p-6 rounded-lg shadow transition-shadow duration-300">
            <img :src="project.image" :alt="project.title" class="rounded-lg mb-4 w-full h-48 object-cover" />
            <h3 class="text-xl font-bold text-gray-900 mb-2">{{ project.title }}</h3>
            <p class="text-gray-600">{{ project.description }}</p>
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
        projects: [
          { id: 1, title: 'Projet 1', description: 'Description du projet 1.', image: 'https://via.placeholder.com/400?text=Projet+1', category: 'site-vitrine' },
          { id: 2, title: 'Projet 2', description: 'Description du projet 2.', image: 'https://via.placeholder.com/400?text=Projet+2', category: 'e-commerce' },
          { id: 3, title: 'Projet 3', description: 'Description du projet 3.', image: 'https://via.placeholder.com/400?text=Projet+3', category: 'application-web' },
        ],
        filteredProjects: [],
      };
    },
    methods: {
      filterProjects(category) {
        if (category === 'all') {
          this.filteredProjects = this.projects;
        } else {
          this.filteredProjects = this.projects.filter((project) => project.category === category);
        }
      },
    },
    mounted() {
      this.filteredProjects = this.projects;
    },
  };
  </script>