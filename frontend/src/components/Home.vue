<template>
  <section id="accueil" class="h-screen flex flex-col items-center justify-center bg-gradient-to-b from-blue-50 to-white relative overflow-hidden">
    <!-- Particules en arrière-plan -->
    <div 
      v-for="(particle, index) in particles"
      :key="index"
      :style="{
        left: particle.x + 'px',
        top: particle.y + 'px',
        width: particle.size + 'px',
        height: particle.size + 'px',
        background: `hsl(${particle.hue}, 70%, 50%)`,
        transform: `translate(${particle.dx}px, ${particle.dy}px)`
      }"
      class="absolute rounded-full blur-sm opacity-40 transition-transform duration-1000 particle"
      :class="{'!rounded-none rotate-45': particle.type === 'triangle'}"
    ></div>

    <div class="text-center px-4 relative z-10">
      <h1 class="text-5xl font-extrabold mb-4 text-gray-800 animate-fade-in-down">
        Bienvenue sur ZSdevweb
      </h1>
      <p class="text-xl mb-8 text-gray-600">
        Développeur web passionné, créateur de solutions modernes et performantes.
      </p>
      <a href="#portfolio" class="btn-primary inline-block">
        Voir mon travail
      </a>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      particles: [],
      mouseX: 0,
      mouseY: 0
    }
  },
  mounted() {
    this.createParticles()
    this.setupEventListeners()
    this.animate()
  },
  beforeUnmount() {
    this.removeEventListeners()
  },
  methods: {
    createParticles() {
      const particleCount = 30
      for (let i = 0; i < particleCount; i++) {
        this.particles.push({
          x: Math.random() * window.innerWidth,
          y: Math.random() * window.innerHeight,
          size: Math.random() * 50 + 20,
          dx: Math.random() * 2 - 1,
          dy: Math.random() * 2 - 1,
          hue: Math.random() * 360,
          type: Math.random() > 0.5 ? 'circle' : 'triangle'
        })
      }
    },
    setupEventListeners() {
      window.addEventListener('mousemove', this.handleMouseMove)
      window.addEventListener('scroll', this.handleScroll)
      window.addEventListener('resize', this.handleResize)
    },
    removeEventListeners() {
      window.removeEventListener('mousemove', this.handleMouseMove)
      window.removeEventListener('scroll', this.handleScroll)
      window.removeEventListener('resize', this.handleResize)
    },
    handleMouseMove(e) {
      this.mouseX = e.clientX
      this.mouseY = e.clientY
    },
    handleScroll() {
      this.particles.forEach(particle => {
        particle.dy += window.scrollY * 0.005
      })
    },
    handleResize() {
      this.particles = this.particles.map(particle => ({
        ...particle,
        x: Math.min(particle.x, window.innerWidth),
        y: Math.min(particle.y, window.innerHeight)
      }))
    },
    animate() {
      this.particles.forEach(particle => {
        // Réaction au mouvement de la souris
        const dx = particle.x - this.mouseX
        const dy = particle.y - this.mouseY
        const distance = Math.sqrt(dx * dx + dy * dy)
        const force = (200 - distance) / 200
        
        if (distance < 200) {
          particle.dx += (dx / distance) * force * 2
          particle.dy += (dy / distance) * force * 2
        }

        // Mouvement naturel
        particle.x += particle.dx
        particle.y += particle.dy
        particle.dx *= 0.99
        particle.dy *= 0.99

        // Rebond sur les bords
        if (particle.x < 0 || particle.x > window.innerWidth) particle.dx *= -1
        if (particle.y < 0 || particle.y > window.innerHeight) particle.dy *= -1
      })

      requestAnimationFrame(this.animate)
    }
  }
}
</script>

<style>
.particle {
  transition: transform 0.3s ease-out, opacity 0.5s ease;
  will-change: transform;
}

.particle:hover {
  transform: scale(1.2) !important;
  opacity: 0.6 !important;
}

.animate-fade-in-down {
  animation: fadeInDown 0.6s ease-out;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>