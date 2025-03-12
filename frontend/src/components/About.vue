<template>
    <section id="apropos" class="py-16 bg-slate-200">
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid md:grid-cols-2 gap-12 items-center" data-aos="fade-up" data-aos-duration="1000">
          <div class="flex justify-center">
            <img src="https://via.placeholder.com/400" alt="À propos" class="rounded-lg shadow-lg hover:scale-105 transition-transform duration-300" />
          </div>
          <div>
            <h2 class="text-3xl font-bold text-gray-900 mb-4">À propos de moi</h2>
            <p class="text-gray-600 mb-4">
              Passionné par le développement web, je crée des sites modernes et performants pour répondre aux besoins de mes clients.
            </p>
            <p class="text-gray-600 mb-6">
              Avec une expertise en Vue.js, Tailwind CSS et bien d'autres technologies, je suis prêt à relever tous les défis.
            </p>
            <a href="#contact" class="btn-primary">Contactez-moi</a>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: 'About',
  };
  </script>