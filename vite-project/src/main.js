import { createApp } from 'vue'
import App from './App.vue'
import './assets/tailwind.css'

// Import AOS
import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)

app.mount('#app')

// Initialiser AOS
AOS.init()
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserTie, faProjectDiagram, faFileAlt, faFileInvoice } from '@fortawesome/free-solid-svg-icons'

library.add(faUserTie, faProjectDiagram, faFileAlt, faFileInvoice)

// On importe quelques icônes (solid & brand)
import { faBars, faArrowUp, faUser, faUserTie, faFileAlt, faFileInvoice, faFileInvoiceDollar, faMoneyBillWave, faProjectDiagram, faDownload } from '@fortawesome/free-solid-svg-icons'
import { faGithub, faLinkedin, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(faBars, faArrowUp, faUser, faUserTie, faFileAlt, faFileInvoice, faFileInvoiceDollar, faMoneyBillWave, faProjectDiagram, faDownload, faGithub, faLinkedin, faTwitter)

// Déclarer le composant global
app.component('font-awesome-icon', FontAwesomeIcon)

// AOS.init() (si vous voulez init AOS ici)

import Navbar from './components/Navbar.vue'
import Home from './components/Home.vue'
import About from './components/About.vue'
import Portfolio from './components/Portfolio.vue'
import Skills from './components/Skills.vue'
import Contact from './components/Contact.vue'
import Devis from './components/Devis.vue'
import Footer from './components/Footer.vue'
