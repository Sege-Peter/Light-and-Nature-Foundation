import os
import re

new_head = """<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Light and Nature Foundation</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              light: '#f8fafc',
              DEFAULT: '#047857',
              dark: '#064e3b',
              accent: '#d97706',
              accentLight: '#f59e0b',
            }
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            serif: ['Playfair Display', 'serif']
          }
        }
      }
    }
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" type="image/png" href="assets/images/lnf log.jpeg">
</head>"""

new_header = """<!-- HEADER -->
<header class="fixed w-full top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-slate-200 shadow-sm transition-all duration-300" id="navbar">
  <div class="max-w-7xl mx-auto flex justify-between items-center px-6 py-3">
    <a href="index.html" class="flex items-center space-x-3 group">
      <div class="relative overflow-hidden rounded-full border-2 border-brand-accent p-0.5 transition-transform duration-300 group-hover:scale-105">
        <img src="assets/images/lnf log.jpeg" alt="LNF Logo" class="w-12 h-12 rounded-full object-cover" />
      </div>
      <span class="font-serif font-bold text-xl tracking-tight text-brand-dark group-hover:text-brand-accent transition-colors">Light & Nature</span>
    </a>

    <!-- Desktop Menu -->
    <nav class="hidden md:flex space-x-8 text-sm font-medium items-center">
      <a href="index.html" class="text-slate-600 hover:text-brand-accent transition-colors relative group">Home
        <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-accent transition-all duration-300 group-hover:w-full"></span>
      </a>
      <a href="about.html" class="text-slate-600 hover:text-brand-accent transition-colors relative group">About
        <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-accent transition-all duration-300 group-hover:w-full"></span>
      </a>
      <a href="projects.html" class="text-slate-600 hover:text-brand-accent transition-colors relative group">Projects
        <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-accent transition-all duration-300 group-hover:w-full"></span>
      </a>
      <a href="leadership.html" class="text-slate-600 hover:text-brand-accent transition-colors relative group">Leadership
        <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-accent transition-all duration-300 group-hover:w-full"></span>
      </a>
      <a href="gallery.html" class="text-slate-600 hover:text-brand-accent transition-colors relative group">Gallery
        <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-accent transition-all duration-300 group-hover:w-full"></span>
      </a>
      <a href="Resources.html" class="text-slate-600 hover:text-brand-accent transition-colors relative group">Resources
        <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-brand-accent transition-all duration-300 group-hover:w-full"></span>
      </a>
      <a href="contact.html" class="px-5 py-2 rounded-full bg-brand-dark text-white hover:bg-brand-accent hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300">Contact Us</a>
    </nav>

    <!-- Hamburger Menu -->
    <div class="md:hidden">
      <button id="menu-toggle" class="text-brand-dark focus:outline-none p-2 rounded-md hover:bg-slate-100 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
    </div>
  </div>

  <!-- Mobile Menu -->
  <nav id="mobile-menu" class="hidden md:hidden bg-white border-t border-slate-100 px-6 py-4 space-y-4 shadow-xl absolute w-full left-0">
    <a href="index.html" class="block text-slate-600 hover:text-brand-accent transition-colors font-medium">Home</a>
    <a href="about.html" class="block text-slate-600 hover:text-brand-accent transition-colors font-medium">About</a>
    <a href="projects.html" class="block text-slate-600 hover:text-brand-accent transition-colors font-medium">Projects</a>
    <a href="leadership.html" class="block text-slate-600 hover:text-brand-accent transition-colors font-medium">Leadership</a>
    <a href="gallery.html" class="block text-slate-600 hover:text-brand-accent transition-colors font-medium">Gallery</a>
    <a href="Resources.html" class="block text-slate-600 hover:text-brand-accent transition-colors font-medium">Resources</a>
    <a href="contact.html" class="block text-brand-dark font-semibold">Contact Us</a>
  </nav>
</header>"""

new_footer = """<!-- FOOTER -->
<footer class="bg-brand-dark text-slate-300 py-12 border-t-4 border-brand-accent relative overflow-hidden">
  <div class="absolute inset-0 opacity-5 bg-[url('assets/images/tree.jpg')] bg-cover bg-center mix-blend-overlay"></div>
  <div class="max-w-7xl mx-auto px-6 relative z-10 grid md:grid-cols-3 gap-8">
    <div>
      <div class="flex items-center space-x-3 mb-4">
        <img src="assets/images/lnf log.jpeg" alt="LNF Logo" class="w-10 h-10 rounded-full object-cover border border-brand-accentLight" />
        <span class="font-serif font-bold text-xl text-white">Light & Nature</span>
      </div>
      <p class="text-sm leading-relaxed mb-6 pr-4">Empowering communities through environmental conservation, sustainability, and education.</p>
    </div>
    
    <div>
      <h4 class="text-white font-serif text-lg mb-4 font-semibold">Quick Links</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="about.html" class="hover:text-brand-accentLight transition-colors inline-block hover:translate-x-1">About Us</a></li>
        <li><a href="projects.html" class="hover:text-brand-accentLight transition-colors inline-block hover:translate-x-1">Our Projects</a></li>
        <li><a href="contact.html" class="hover:text-brand-accentLight transition-colors inline-block hover:translate-x-1">Get Involved</a></li>
        <li><a href="donate.html" class="hover:text-brand-accentLight transition-colors inline-block hover:translate-x-1">Donate</a></li>
      </ul>
    </div>

    <div>
      <h4 class="text-white font-serif text-lg mb-4 font-semibold">Connect With Us</h4>
      <div class="flex space-x-4">
        <a href="mailto:lightandnaturefoundation@gmail.com" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-brand-accent hover:-translate-y-1 transition-all duration-300 shadow-lg">
          <i class="fas fa-envelope text-white"></i>
        </a>
        <a href="https://facebook.com" target="_blank" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-brand-accent hover:-translate-y-1 transition-all duration-300 shadow-lg">
          <i class="fab fa-facebook-f text-white"></i>
        </a>
        <a href="https://x.com" target="_blank" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-brand-accent hover:-translate-y-1 transition-all duration-300 shadow-lg">
          <i class="fab fa-twitter text-white"></i>
        </a>
        <a href="https://instagram.com" target="_blank" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-brand-accent hover:-translate-y-1 transition-all duration-300 shadow-lg">
          <i class="fab fa-instagram text-white"></i>
        </a>
        <a href="https://linkedin.com" target="_blank" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-brand-accent hover:-translate-y-1 transition-all duration-300 shadow-lg">
          <i class="fab fa-linkedin-in text-white"></i>
        </a>
      </div>
    </div>
  </div>
  
  <div class="max-w-7xl mx-auto px-6 mt-12 pt-6 border-t border-white/10 text-center text-sm relative z-10 flex flex-col md:flex-row justify-between items-center text-slate-400">
    <p>&copy; <span id="year"></span> Light and Nature Foundation. All rights reserved.</p>
    <p class="mt-2 md:mt-0 text-xs">Designed with <i class="fas fa-heart text-brand-accent mx-1"></i> for nature</p>
  </div>
</footer>"""

files = ['about.html', 'contact.html', 'donate.html', 'gallery.html', 'index.html', 'leadership.html', 'projects.html', 'Resources.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace <head> ... </head>
    content = re.sub(r'<head>.*?</head>', new_head, content, flags=re.DOTALL)
    
    # Replace <!-- HEADER --> ... </header>
    content = re.sub(r'<!-- HEADER -->.*?</header>', new_header, content, flags=re.DOTALL)
    
    # Replace <!-- FOOTER --> ... </footer>
    content = re.sub(r'<!-- FOOTER -->.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    # Body background adjustments
    content = content.replace('bg-green-50', 'bg-slate-50 text-slate-800 font-sans antialiased selection:bg-brand-accent selection:text-white pt-20')
    
    # Enhancing cards and blocks with micro-interactions
    content = re.sub(r'class="([^"]*rounded-lg[^"]*shadow-md[^"]*)"', r'class="\1 hover:shadow-xl hover:-translate-y-2 transition-all duration-300 border border-slate-100"', content)
    content = re.sub(r'class="([^"]*rounded-xl[^"]*shadow-2xl[^"]*)"', r'class="\1 hover:shadow-2xl hover:scale-[1.02] transition-all duration-500"', content)
    
    # Button enhancements
    content = re.sub(r'class="([^"]*bg-green-900[^"]*text-white[^"]*px-6[^"]*)"', r'class="\1 hover:bg-brand-accent hover:shadow-lg hover:-translate-y-1 transition-all duration-300"', content)
    content = re.sub(r'class="([^"]*bg-yellow-400[^"]*text-green-900[^"]*px-6[^"]*)"', r'class="\1 bg-brand-accent text-white hover:bg-brand-dark hover:shadow-lg hover:-translate-y-1 transition-all duration-300"', content)

    # General replacements for colors
    content = content.replace('green-text', 'text-brand-dark')
    content = content.replace('gold-text', 'text-brand-accent')
    content = content.replace('gold-bg', 'bg-brand-accent')
    content = content.replace('green-bg', 'bg-brand-dark')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Refactoring complete.")
