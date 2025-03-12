
<template>
    <section id="inscription" class="min-h-screen flex items-center justify-center bg-gradient-to-b from-blue-50 to-white relative overflow-hidden py-20">
      
      <div class="max-w-md w-full mx-4 bg-white rounded-xl shadow-2xl p-8 relative z-10">
        <h2 class="text-3xl font-bold text-center mb-8 text-gray-800">
          Créer un compte
        </h2>
        
        <form class="space-y-6">
          <div>
            <label class="block text-gray-700 mb-2">Nom complet</label>
            <input type="text" 
                   class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          </div>
  
          <div>
            <label class="block text-gray-700 mb-2">Email</label>
            <input type="email" 
                   class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          </div>
  
          <div>
            <label class="block text-gray-700 mb-2">Mot de passe</label>
            <input type="password" 
                   class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent">
          </div>
  
          <button type="submit" 
                  class="w-full btn-primary py-3 px-6 text-lg transition-transform hover:scale-105">
            S'inscrire
          </button>
        </form>
      </div>
    </section>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        full_name: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', this.form);
        // Redirection ou gestion de la connexion
      } catch (error) {
        console.error('Erreur d\'inscription:', error.response.data);
      }
    }
  }
}
  
  </script>
  <style>
  </style>