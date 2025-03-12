<template>
  <section id="devis" class="py-16 bg-gray-100">
    <div class="max-w-7xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-gray-900 text-center mb-12">Demandez un devis</h2>
      <div class="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
        <form @submit.prevent="validateForm" class="space-y-6">
          <!-- Section Prestataire -->
          <fieldset class="border-2 border-gray-200 rounded-lg p-6 bg-gray-50 hover:border-blue-500 transition-all duration-300">
            <legend class="text-xl font-semibold text-gray-800 mb-4">
              <font-awesome-icon icon="user-tie" class="mr-2"/>
              Informations Prestataire
            </legend>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div v-for="(field, key) in providerFields" :key="key">
                <label :for="key" class="block text-gray-700 mb-2">{{ field.label }}</label>
                <input :type="field.type" :id="key" v-model="formData.provider[key]" 
                      class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                      :class="{ 'border-red-500': errors.provider?.[key] }">
                <p v-if="errors.provider?.[key]" class="text-red-500 text-sm mt-1">{{ errors.provider[key] }}</p>
              </div>
            </div>
          </fieldset>

          <!-- Section Destinataire (optionnel) -->
          <fieldset class="border-2 border-gray-200 rounded-lg p-6 bg-gray-50 hover:border-blue-500 transition-all duration-300">
            <legend class="text-xl font-semibold text-gray-800 mb-4">
              <font-awesome-icon icon="user" class="mr-2"/>
              Informations Destinataire (Optionnel)
            </legend>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div v-for="(field, key) in recipientFields" :key="key">
                <label :for="key" class="block text-gray-700 mb-2">{{ field.label }}</label>
                <input :type="field.type" :id="key" v-model="formData.recipient[key]" 
                      class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600">
              </div>
            </div>
          </fieldset>

          <!-- Section Configuration Projet -->
          <fieldset class="border-2 border-gray-200 rounded-lg p-6 bg-gray-50 hover:border-blue-500 transition-all duration-300">
            <legend class="text-xl font-semibold text-gray-800 mb-4">
              <font-awesome-icon icon="project-diagram" class="mr-2"/>
              Configuration du Projet
            </legend>
            <div class="space-y-6">
              <!-- Type de site -->
              <div>
                <label class="block text-gray-700 mb-2">Type de site</label>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <button 
                    v-for="(option, key) in siteTypeOptions" 
                    :key="key"
                    @click.prevent="formData.project.type = key"
                    class="p-4 border rounded-lg text-left hover:border-blue-500 transition-all"
                    :class="{'border-blue-500 bg-blue-50': formData.project.type === key}"
                  >
                    <h3 class="font-semibold mb-2">{{ option.label }}</h3>
                    <p class="text-sm text-gray-600">{{ option.description }}</p>
                    <p class="mt-2 text-blue-600 font-medium">{{ option.basePrice }} € HT</p>
                  </button>
                </div>
                <p v-if="errors.project?.type" class="text-red-500 text-sm mt-2">{{ errors.project.type }}</p>
              </div>

              <!-- Design -->
              <div>
                <label class="block text-gray-700 mb-2">Design</label>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <button 
                    v-for="(design, key) in designOptions" 
                    :key="key"
                    @click.prevent="formData.project.design = key"
                    class="p-4 border rounded-lg text-center hover:border-blue-500 transition-all"
                    :class="{'border-blue-500 bg-blue-50': formData.project.design === key}"
                  >
                    <div class="h-8 mb-2 text-blue-500">
                      <font-awesome-icon :icon="design.icon" class="text-xl"/>
                    </div>
                    <h3 class="font-semibold">{{ design.label }}</h3>
                    <p class="text-sm text-gray-600 mt-1">+ {{ design.price }} € HT</p>
                  </button>
                </div>
                <p v-if="errors.project?.design" class="text-red-500 text-sm mt-2">{{ errors.project.design }}</p>
              </div>

              <!-- Complexité dynamique -->
              <div>
                <label class="block text-gray-700 mb-2">Complexité</label>
                <div class="space-y-2">
                  <div 
                    v-for="complexity in availableComplexities" 
                    :key="complexity.value"
                    @click.prevent="formData.project.complexity = complexity.value"
                    class="p-3 border rounded-lg cursor-pointer hover:border-blue-500 transition-all"
                    :class="{'border-blue-500 bg-blue-50': formData.project.complexity === complexity.value}"
                  >
                    <div class="flex justify-between items-center">
                      <div>
                        <h3 class="font-semibold">{{ complexity.label }}</h3>
                        <p class="text-sm text-gray-600">{{ complexity.description }}</p>
                      </div>
                      <span class="text-blue-600 font-medium">+ {{ complexity.price }} € HT</span>
                    </div>
                  </div>
                  <p v-if="availableComplexities.length === 0" class="text-sm text-gray-500">
                    Sélectionnez d'abord le type et le design
                  </p>
                </div>
                <p v-if="errors.project?.complexity" class="text-red-500 text-sm mt-2">{{ errors.project.complexity }}</p>
              </div>

              <!-- Options supplémentaires -->
              <div>
                <label class="block text-gray-700 mb-2">Options supplémentaires</label>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div 
                    v-for="option in supplementaryOptions" 
                    :key="option.id"
                    class="p-4 border rounded-lg hover:border-blue-500 transition-all"
                  >
                    <label class="flex items-start space-x-3 cursor-pointer">
                      <input 
                        type="checkbox" 
                        v-model="option.selected"
                        class="mt-1 custom-checkbox"
                      >
                      <div class="flex-1">
                        <h3 class="font-semibold">{{ option.label }}</h3>
                        <p class="text-sm text-gray-600 mt-1">{{ option.description }}</p>
                        <p class="mt-2 text-blue-600 font-medium">+ {{ option.price }} € HT</p>
                      </div>
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </fieldset>

          <button 
            type="submit" 
            class="btn-primary w-full sm:w-auto transition-all duration-300 hover:scale-105"
          >
            <font-awesome-icon icon="file-alt" class="mr-2"/>
            Générer le devis
          </button>
        </form>

        <!-- Devis Généré -->
        <div 
          v-if="showDevis" 
          class="mt-6 transition-all duration-500 ease-in-out transform opacity-0 translate-y-4"
          :class="{'opacity-100 translate-y-0': showDevis}"
        >
          <div id="pdf-template" class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-2xl font-bold mb-6">
              <font-awesome-icon icon="file-invoice" class="mr-2"/>
              Votre Devis
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
              <!-- Prestataire -->
              <div class="p-4 bg-gray-50 rounded-lg">
                <h4 class="text-xl font-semibold mb-3">
                  <font-awesome-icon icon="user-tie" class="mr-2"/>
                  Prestataire
                </h4>
                <dl class="space-y-2">
                  <div 
                    v-for="(value, key) in formData.provider" 
                    :key="key" 
                    class="flex justify-between"
                  >
                    <dt class="text-gray-600">{{ providerFields[key].label }}:</dt>
                    <dd class="font-medium">{{ value }}</dd>
                  </div>
                </dl>
              </div>

              <!-- Destinataire -->
              <div 
                class="p-4 bg-gray-50 rounded-lg" 
                v-if="hasRecipientInfo"
              >
                <h4 class="text-xl font-semibold mb-3">
                  <font-awesome-icon icon="user" class="mr-2"/>
                  Destinataire
                </h4>
                <dl class="space-y-2">
                  <div 
                    v-for="(value, key) in formData.recipient" 
                    :key="key" 
                    class="flex justify-between"
                  >
                    <dt class="text-gray-600">{{ recipientFields[key].label }}:</dt>
                    <dd class="font-medium">{{ value }}</dd>
                  </div>
                </dl>
              </div>

              <!-- Projet -->
              <div class="p-4 bg-gray-50 rounded-lg col-span-full">
                <h4 class="text-xl font-semibold mb-3">
                  <font-awesome-icon icon="project-diagram" class="mr-2"/>
                  Détails du Projet
                </h4>
                <dl class="space-y-2">
                  <div class="flex justify-between">
                    <dt class="text-gray-600">Type de site:</dt>
                    <dd class="font-medium">{{ siteTypeOptions[formData.project.type]?.label }}</dd>
                  </div>
                  <div class="flex justify-between">
                    <dt class="text-gray-600">Design:</dt>
                    <dd class="font-medium">{{ designOptions[formData.project.design]?.label }}</dd>
                  </div>
                  <div class="flex justify-between">
                    <dt class="text-gray-600">Complexité:</dt>
                    <dd class="font-medium">{{ complexityOptions[formData.project.complexity]?.label }}</dd>
                  </div>
                  <div 
                    class="flex justify-between" 
                    v-for="option in selectedSupplementary" 
                    :key="option.id"
                  >
                    <dt class="text-gray-600">{{ option.label }}:</dt>
                    <dd class="font-medium">+ {{ option.price }} € HT</dd>
                  </div>
                </dl>
              </div>

              <!-- Détails financiers -->
              <div class="p-4 bg-gray-50 rounded-lg col-span-full">
                <h4 class="text-xl font-semibold mb-3">
                  <font-awesome-icon icon="file-invoice-dollar" class="mr-2"/>
                  Détails Financiers
                </h4>
                <dl class="space-y-2">
                  <div class="flex justify-between">
                    <dt class="text-gray-600">Total HT:</dt>
                    <dd class="font-medium">{{ totalHT.toFixed(2) }} €</dd>
                  </div>
                  <div class="flex justify-between">
                    <dt class="text-gray-600">TVA ({{ (tvaRate * 100).toFixed(0) }}%):</dt>
                    <dd class="font-medium">{{ totalTVA.toFixed(2) }} €</dd>
                  </div>
                  <div class="flex justify-between border-t pt-2">
                    <dt class="text-gray-600 font-semibold">Total TTC:</dt>
                    <dd class="font-semibold text-blue-600">{{ totalTTC.toFixed(2) }} €</dd>
                  </div>
                </dl>
              </div>

              <!-- Phases de paiement -->
              <div class="p-4 bg-gray-50 rounded-lg col-span-full">
                <h4 class="text-xl font-semibold mb-3">
                  <font-awesome-icon icon="money-bill-wave" class="mr-2"/>
                  Échéancier de Paiement
                </h4>
                <ul class="list-disc ml-5 space-y-2">
                  <li v-for="(phase, index) in paymentPhases" :key="index">
                    <strong>{{ phase.label }}:</strong> {{ phase.amount }} €
                  </li>
                </ul>
              </div>
            </div>

            <!-- Bouton Téléchargement -->
            <div class="border-t pt-6">
              <button 
                @click="generatePDF" 
                class="btn-secondary w-full"
                :disabled="isGeneratingPDF"
              >
                <font-awesome-icon icon="download" class="mr-2"/>
                {{ isGeneratingPDF ? 'Génération en cours...' : 'Télécharger le PDF' }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import html2pdf from 'html2pdf.js'

export default {
  name: 'Devis',
  props: {
    isDevisSectionVisible: Boolean,
  },
  data() {
    return {
      showDevis: false,
      isGeneratingPDF: false,
      tvaRate: 0.2,
      errors: {},
      formData: {
        provider: {
          name: "ZSdevweb",
          juridicalStatus: "Auto-Entrepreneur",
          siret: "123 456 789 00010",
          email: "contact@zsdevweb.com"
        },
        recipient: {},
        project: {
          type: '',
          design: '',
          complexity: ''
        }
      },
      siteTypeOptions: {
        'vitrine-simple': {
          label: 'Site Vitrine Simple',
          basePrice: 800,
          description: 'Site présentation basique (5 pages max)'
        },
        'vitrine-avance': {
          label: 'Site Vitrine Avancé',
          basePrice: 1200,
          description: 'Site avec animations et formulaire'
        },
        'ecommerce-standard': {
          label: 'E-commerce Standard',
          basePrice: 2400,
          description: 'Boutique en ligne avec paiement sécurisé'
        },
        'ecommerce-complet': {
          label: 'E-commerce Complet',
          basePrice: 3500,
          description: 'Solution complète avec gestion de stock'
        },
        'webapp': {
          label: 'Application Web',
          basePrice: 5000,
          description: 'Application métier sur mesure'
        }
      },
      designOptions: {
        'standard': {
          label: 'Standard',
          icon: 'palette',
          price: 0
        },
        'leger': {
          label: 'Personnalisé',
          icon: 'brush',
          price: 300
        },
        'surmesure': {
          label: 'Sur Mesure',
          icon: 'drafting-compass',
          price: 700
        }
      },
      complexityOptions: {
        'simple': { 
          label: 'Basique', 
          price: 0, 
          description: 'Fonctionnalités standard' 
        },
        'intermediaire': { 
          label: 'Intermédiaire', 
          price: 500, 
          description: 'Intégrations spécifiques' 
        },
        'avancee': { 
          label: 'Avancée', 
          price: 1000, 
          description: 'Développement complexe' 
        }
      },
      supplementaryOptions: [
        {
          id: 'seo',
          label: 'Référencement SEO',
          price: 300,
          selected: false,
          description: 'Optimisation pour les moteurs de recherche'
        },
        {
          id: 'maintenance',
          label: 'Maintenance 12 mois',
          price: 600,
          selected: false,
          description: 'Mises à jour et support technique'
        },
        {
          id: 'hosting',
          label: 'Hébergement Premium',
          price: 200,
          selected: false,
          description: 'Hébergement haute performance'
        },
        {
          id: 'training',
          label: 'Formation',
          price: 150,
          selected: false,
          description: 'Session de formation utilisateur'
        }
      ],
      complexityRules: {
        'vitrine-simple': {
          'standard': ['simple'],
          'leger': ['simple', 'intermediaire'],
          'surmesure': ['intermediaire']
        },
        'vitrine-avance': {
          'standard': ['simple', 'intermediaire'],
          'leger': ['intermediaire'],
          'surmesure': ['intermediaire', 'avancee']
        },
        'ecommerce-standard': {
          'standard': ['intermediaire'],
          'leger': ['intermediaire'],
          'surmesure': ['avancee']
        },
        'ecommerce-complet': {
          '*': ['avancee']
        },
        'webapp': {
          '*': ['avancee']
        }
      }
    }
  },
  computed: {
    providerFields() {
      return {
        name: { label: 'Nom/Entreprise', type: 'text' },
        juridicalStatus: { label: 'Statut juridique', type: 'text' },
        siret: { label: 'N° SIRET', type: 'text' },
        email: { label: 'Email', type: 'email' }
      }
    },
    recipientFields() {
      return {
        name: { label: 'Nom', type: 'text' },
        company: { label: 'Entreprise', type: 'text' },
        email: { label: 'Email', type: 'email' }
      }
    },
    availableComplexities() {
      const type = this.formData.project.type
      const design = this.formData.project.design
      if (!type || !design) return []

      const rules = this.complexityRules[type]
      const allowed = rules[design] || rules['*'] || []
      
      return allowed.map(value => ({
        ...this.complexityOptions[value],
        value
      })).sort((a, b) => ['simple', 'intermediaire', 'avancee'].indexOf(a.value) - ['simple', 'intermediaire', 'avancee'].indexOf(b.value))
    },
    totalHT() {
      const base = this.siteTypeOptions[this.formData.project.type]?.basePrice || 0
      const design = this.designOptions[this.formData.project.design]?.price || 0
      const complexity = this.complexityOptions[this.formData.project.complexity]?.price || 0
      const supplements = this.supplementaryOptions
        .filter(opt => opt.selected)
        .reduce((sum, opt) => sum + opt.price, 0)
      
      return base + design + complexity + supplements
    },
    totalTVA() {
      return this.totalHT * this.tvaRate
    },
    totalTTC() {
      return this.totalHT + this.totalTVA
    },
    selectedSupplementary() {
      return this.supplementaryOptions.filter(opt => opt.selected)
    },
    hasRecipientInfo() {
      return Object.values(this.formData.recipient).some(value => value.trim() !== '')
    },
    paymentPhases() {
      return [
        { label: 'Acompte de 30% à la signature', amount: (this.totalTTC * 0.3).toFixed(2) },
        { label: 'Phase intermédiaire de 40%', amount: (this.totalTTC * 0.4).toFixed(2) },
        { label: 'Solde de 30% à la livraison', amount: (this.totalTTC * 0.3).toFixed(2) }
      ]
    }
  },
  methods: {
    validateForm() {
      this.errors = {}
      let isValid = true

      // Validation prestataire
      Object.keys(this.providerFields).forEach(field => {
        if (!this.formData.provider[field]?.trim()) {
          this.errors.provider = {
            ...this.errors.provider,
            [field]: 'Ce champ est obligatoire'
          }
          isValid = false
        }
      })

      // Validation projet
      const requiredProjectFields = {
        type: 'Sélectionnez un type de site',
        design: 'Sélectionnez un design',
        complexity: 'Sélectionnez une complexité'
      }

      Object.entries(requiredProjectFields).forEach(([field, message]) => {
        if (!this.formData.project[field]) {
          this.errors.project = {
            ...this.errors.project,
            [field]: message
          }
          isValid = false
        }
      })

      if (isValid) {
        this.showDevis = true
        window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })
      }
    },

    async generatePDF() {
      try {
        this.isGeneratingPDF = true
        const element = document.getElementById('pdf-template')
        
        const opt = {
          margin: [10, 10],
          filename: `Devis_${this.formData.provider.name.replace(/\s+/g, '_')}.pdf`,
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: { 
            scale: 2,
            useCORS: true,
            logging: true 
          },
          jsPDF: { 
            unit: 'mm', 
            format: 'a4', 
            orientation: 'portrait' 
          }
        }

        await html2pdf().set(opt).from(element).save()
      } catch (error) {
        console.error('Erreur de génération PDF:', error)
        alert("Une erreur est survenue lors de la génération du PDF")
      } finally {
        this.isGeneratingPDF = false
      }
    },
    async saveDevis() {
  try {
    await axios.post('http://localhost:8000/api/devis/', {
      provider: this.formData.provider,
      recipient: this.formData.recipient,
      project: this.formData.project,
      total_ttc: this.totalTTC,
      payment_phases: this.paymentPhases
    }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    });
    alert('Devis sauvegardé !');
  } catch (error) {
    console.error('Erreur:', error.response.data);
  }
}
  }
}
</script>

<style scoped>
.btn-primary {
  background-color: #2563eb;
  color: #ffffff;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  border-radius: 0.5rem;
  transition-property: background-color;
  transition-duration: 300ms;
}

.btn-primary:hover {
  background-color: #1d4ed8;
}

.btn-secondary {
  background-color: #374151;
  color: #ffffff;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  border-radius: 0.5rem;
  transition-property: background-color;
  transition-duration: 300ms;
}

.btn-secondary:hover {
  background-color: #1f2937;
}

.custom-checkbox {
  height: 1.25rem;
  width: 1.25rem;
  border-width: 2px;
  border-color: #d1d5db;
  border-radius: 0.375rem;
  cursor: pointer;
}

.custom-checkbox:checked {
  background-color: #2563eb;
  border-color: #2563eb;
  background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>