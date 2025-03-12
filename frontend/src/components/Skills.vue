<template>
  <section id="competences" class="py-20 bg-gradient-to-b from-gray-50 to-white">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-4xl font-bold text-gray-900 text-center mb-16">
        Compétences
      </h2>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="skill in skills" 
          :key="skill.name" 
          class="group relative skill-card bg-white border border-gray-200 p-6 rounded-xl shadow-sm transition-all duration-300 ease-out hover:shadow-lg hover:-translate-y-2 hover:border-transparent"
        >
          <div class="absolute inset-0 rounded-xl bg-gradient-to-br from-blue-100/50 to-purple-100/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          
          <div class="relative z-10">
            <div class="flex items-center space-x-4 mb-4">
              <div class="p-2 bg-white rounded-lg shadow-sm transition-all duration-300 group-hover:shadow-md">
                <img 
                  :src="skill.logo" 
                  :alt="skill.name" 
                  class="w-10 h-10 object-contain transition-transform duration-300 group-hover:scale-110" 
                />
              </div>
              <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors duration-300">
                {{ skill.name }}
              </h3>
            </div>
            <p class="text-gray-600 text-sm leading-relaxed transition-colors duration-300 group-hover:text-gray-800">
              {{ skill.description }}
            </p>
          </div>
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
      ]
    };
  },
};
</script>

<style>
@keyframes underline {
  0% { width: 0; left: 0; }
  50% { width: 100%; left: 0; }
  100% { width: 0; left: 100%; }
}

.animate-underline {
  animation: underline 3s ease-in-out infinite;
}

.skill-card:hover::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 0.75rem;
  padding: 2px;
  background: linear-gradient(45deg, #60a5fa, #8b5cf6);
  -webkit-mask: 
     linear-gradient(#fff 0 0) content-box, 
     linear-gradient(#fff 0 0);
  mask: 
     linear-gradient(#fff 0 0) content-box, 
     linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: border-glow 1.5s ease-in-out infinite;
}

@keyframes border-glow {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 1; }
}
</style>