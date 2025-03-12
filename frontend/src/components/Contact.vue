<template>
  <section id="contact" class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-gray-900 text-center mb-12" data-aos="fade-up">Contact</h2>
      
      <!-- Conteneur flex pour aligner les éléments -->
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Section gauche : Informations de contact et réseaux sociaux -->
        <div class="w-full lg:w-1/2" data-aos="fade-up">
          <div class="bg-white p-8 rounded-lg shadow hover:shadow-lg transition-shadow duration-300">
            <h3 class="text-xl font-bold text-gray-900 mb-6">Coordonnées</h3>
            <p class="text-gray-700 mb-4">Adresse: 25 rue Corneil batiment le Jacquard etage 2, Roubaix, France</p>
            <p class="text-gray-700 mb-8">Téléphone: +33 1 23 45 67 89</p>

            <!-- Réseaux sociaux -->
            <div class="flex space-x-6">
              <a href="https://github.com/votreprofil" target="_blank" class="text-gray-600 hover:text-blue-600 transition-colors duration-300">
                <i class="fab fa-github text-3xl"></i>
              </a>
              <a href="https://linkedin.com/in/votreprofil" target="_blank" class="text-gray-600 hover:text-blue-600 transition-colors duration-300">
                <i class="fab fa-linkedin text-3xl"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Section droite : Formulaire de contact -->
        <div class="w-full lg:w-1/2" data-aos="fade-up" data-aos-delay="200">
          <form @submit.prevent="validateContactForm" class="bg-white p-8 rounded-lg shadow hover:shadow-lg transition-shadow duration-300">
            <div class="mb-6">
              <label for="name" class="block text-gray-700 mb-2">Nom</label>
              <input type="text" id="name" v-model="contactForm.name" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600" />
              <p v-if="contactForm.errors.name" class="text-red-500 text-sm mt-1">{{ contactForm.errors.name }}</p>
            </div>
            <div class="mb-6">
              <label for="email" class="block text-gray-700 mb-2">Email</label>
              <input type="email" id="email" v-model="contactForm.email" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600" />
              <p v-if="contactForm.errors.email" class="text-red-500 text-sm mt-1">{{ contactForm.errors.email }}</p>
            </div>
            <div class="mb-6">
              <label for="message" class="block text-gray-700 mb-2">Message</label>
              <textarea id="message" v-model="contactForm.message" rows="5" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"></textarea>
              <p v-if="contactForm.errors.message" class="text-red-500 text-sm mt-1">{{ contactForm.errors.message }}</p>
            </div>
            <button type="submit" class="btn-primary w-full sm:w-auto">Envoyer</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Contact',
  data() {
    return {
      contactForm: {
        name: '',
        email: '',
        message: '',
        errors: {},
      },
    };
  },
  methods: {
    validateContactForm() {
      const name = this.contactForm.name.trim();
      const email = this.contactForm.email.trim();
      const message = this.contactForm.message.trim();

      // Réinitialiser les erreurs
      this.contactForm.errors = {};

      // Validation
      if (!name) this.contactForm.errors.name = "Le nom est obligatoire.";
      if (!email) {
        this.contactForm.errors.email = "L'email est obligatoire.";
      } else if (!this.validateEmail(email)) {
        this.contactForm.errors.email = "L'email est invalide.";
      }
      if (!message) this.contactForm.errors.message = "Le message est obligatoire.";

      // Si pas d'erreurs, soumettre le formulaire
      if (Object.keys(this.contactForm.errors).length === 0) {
        this.submitContactForm();
      }
    },
    validateEmail(email) {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    },
    async submitContactForm() {
  try {
    await axios.post('http://localhost:8000/api/contact/', {
      name: this.contactForm.name,
      email: this.contactForm.email,
      message: this.contactForm.message
    });
    alert('Message envoyé avec succès !');
  } catch (error) {
    console.error('Erreur:', error.response.data);
  }
},
  },
};
</script>