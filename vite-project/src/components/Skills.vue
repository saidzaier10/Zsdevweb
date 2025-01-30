<template>
    <section id="competences" class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-6">
        <h2 class="text-3xl font-bold text-gray-900 text-center mb-12" data-aos="fade-up">Compétences</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8" data-aos="fade-up" data-aos-delay="200">
          <div v-for="skill in skills" :key="skill.name" class="skill-card bg-white border border-gray-200 p-6 rounded-lg shadow-sm transition-transform duration-300">
            <div class="flex items-center space-x-4 mb-4">
              <img :src="skill.logo" :alt="skill.name" class="w-12 h-12 object-contain" />
              <h3 class="text-xl font-bold text-gray-900">{{ skill.name }}</h3>
            </div>
            <p class="text-gray-600">{{ skill.description }}</p>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: 'Skills',
    data() {
      return {
        skills: [
          {
            name: 'Node.js',
            logo: 'https://cdn.worldvectorlogo.com/logos/nodejs-icon.svg',
            description: "JavaScript runtime pour construire des applications réseau scalables.",
          },
          {
            name: 'Express',
            logo: 'https://cdn.worldvectorlogo.com/logos/express-109.svg',
            description: "Framework web pour Node.js, simplifiant la création d'API et d'applications web.",
          },
          {
            name: 'Python',
            logo: 'https://cdn.worldvectorlogo.com/logos/python-5.svg',
            description: "Langage de programmation polyvalent pour le web, l'analyse de données et l'IA.",
          },
          {
            name: 'Django',
            logo: 'https://cdn.worldvectorlogo.com/logos/django.svg',
            description: "Framework web Python pour des applications rapides et sécurisées.",
          },
          {
            name: 'Tailwind CSS',
            logo: 'https://cdn.worldvectorlogo.com/logos/tailwindcss.svg',
            description: "Framework CSS utilitaire pour des designs modernes et responsives.",
          },
          {
            name: 'UI/UX Design',
            logo: 'https://cdn.worldvectorlogo.com/logos/figma-1.svg',
            description: "Conception d'interfaces utilisateur intuitives et esthétiques.",
          },
          {
            name: 'Vue.js',
            logo: 'https://cdn.worldvectorlogo.com/logos/vue-9.svg',
            description: "Framework JavaScript progressif pour construire des interfaces utilisateur.",
          },
          {
            name: 'React',
            logo: 'https://cdn.worldvectorlogo.com/logos/react-2.svg',
            description: "Bibliothèque JavaScript pour des interfaces utilisateur interactives.",
          },
        ],
      };
    },
  };
  </script>