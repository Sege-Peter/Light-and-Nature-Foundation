import os
import re

new_footer = """<!-- FOOTER -->
<footer class="bg-slate-950 text-slate-400 py-16 border-t border-slate-800 relative overflow-hidden mt-20">
  <!-- Decorative background glow -->
  <div class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-32 bg-brand-DEFAULT blur-[120px] opacity-20 pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-6 relative z-10">
    <!-- Top Call to Action -->
    <div class="flex flex-col md:flex-row justify-between items-center bg-slate-900/50 p-8 rounded-2xl border border-slate-800 mb-16 shadow-2xl backdrop-blur-md animate-on-scroll">
      <div class="mb-6 md:mb-0 text-center md:text-left">
        <h3 class="text-3xl font-serif font-bold text-white mb-2">Join our mission</h3>
        <p class="text-slate-400">Subscribe to our newsletter for updates on environmental action.</p>
      </div>
      <div class="flex w-full md:w-auto gap-3">
        <input type="email" placeholder="Enter your email" class="w-full md:w-72 bg-slate-800 text-white px-5 py-3 rounded-full border border-slate-700 focus:outline-none focus:border-brand-accent transition-colors" />
        <button class="bg-brand-accent hover:bg-brand-accentLight text-white px-8 py-3 rounded-full font-semibold transition-all duration-300 hover:shadow-[0_0_20px_rgba(217,119,6,0.4)] whitespace-nowrap hover:-translate-y-0.5">Subscribe</button>
      </div>
    </div>

    <!-- Main Footer Content -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-12 mb-16">
      
      <!-- Brand Info (Spans 4 columns) -->
      <div class="lg:col-span-4 animate-on-scroll delay-100">
        <div class="flex items-center space-x-4 mb-6">
          <div class="relative overflow-hidden rounded-full border border-brand-accent p-0.5">
            <img src="assets/images/lnf log.jpeg" alt="LNF Logo" class="w-12 h-12 rounded-full object-cover" />
          </div>
          <span class="font-serif font-bold text-2xl text-white tracking-tight">Light & Nature</span>
        </div>
        <p class="text-sm leading-relaxed mb-8 pr-4">Empowering communities through environmental conservation, sustainability, and education. We believe that by acting locally, we can impact globally.</p>
        
        <!-- Social Icons -->
        <div class="flex space-x-3">
          <a href="mailto:lightandnaturefoundation@gmail.com" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-brand-accent text-white hover:-translate-y-1 transition-all duration-300 shadow-lg group">
            <i class="fas fa-envelope group-hover:scale-110 transition-transform"></i>
          </a>
          <a href="https://facebook.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-brand-accent text-white hover:-translate-y-1 transition-all duration-300 shadow-lg group">
            <i class="fab fa-facebook-f group-hover:scale-110 transition-transform"></i>
          </a>
          <a href="https://x.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-brand-accent text-white hover:-translate-y-1 transition-all duration-300 shadow-lg group">
            <i class="fab fa-twitter group-hover:scale-110 transition-transform"></i>
          </a>
          <a href="https://instagram.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-brand-accent text-white hover:-translate-y-1 transition-all duration-300 shadow-lg group">
            <i class="fab fa-instagram group-hover:scale-110 transition-transform"></i>
          </a>
          <a href="https://linkedin.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-brand-accent text-white hover:-translate-y-1 transition-all duration-300 shadow-lg group">
            <i class="fab fa-linkedin-in group-hover:scale-110 transition-transform"></i>
          </a>
        </div>
      </div>

      <!-- Links (Spans 2 columns each) -->
      <div class="lg:col-span-2 animate-on-scroll delay-200">
        <h4 class="text-white font-serif text-lg mb-6 font-semibold relative inline-block">
          Explore
          <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-brand-accent"></span>
        </h4>
        <ul class="space-y-4 text-sm">
          <li><a href="index.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Home</a></li>
          <li><a href="about.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>About Us</a></li>
          <li><a href="projects.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Our Projects</a></li>
          <li><a href="gallery.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Gallery</a></li>
        </ul>
      </div>

      <div class="lg:col-span-2 animate-on-scroll delay-300">
        <h4 class="text-white font-serif text-lg mb-6 font-semibold relative inline-block">
          Get Involved
          <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-brand-accent"></span>
        </h4>
        <ul class="space-y-4 text-sm">
          <li><a href="donate.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Donate</a></li>
          <li><a href="contact.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Volunteer</a></li>
          <li><a href="Resources.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Resources</a></li>
          <li><a href="leadership.html" class="hover:text-brand-accentLight transition-colors group flex items-center"><span class="w-2 h-2 rounded-full bg-brand-accent mr-2 opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all duration-300"></span>Leadership</a></li>
        </ul>
      </div>

      <!-- Contact Info (Spans 4 columns) -->
      <div class="lg:col-span-4 animate-on-scroll delay-400">
        <h4 class="text-white font-serif text-lg mb-6 font-semibold relative inline-block">
          Contact Us
          <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-brand-accent"></span>
        </h4>
        <ul class="space-y-5 text-sm">
          <li class="flex items-start">
            <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-brand-accent mr-4 shrink-0">
              <i class="fas fa-map-marker-alt"></i>
            </div>
            <span class="mt-1">Kisumu, Kenya<br/>East Africa</span>
          </li>
          <li class="flex items-start">
            <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-brand-accent mr-4 shrink-0">
              <i class="fas fa-envelope"></i>
            </div>
            <a href="mailto:lightandnaturefoundation@gmail.com" class="mt-1 hover:text-brand-accentLight transition-colors">lightandnaturefoundation@gmail.com</a>
          </li>
          <li class="flex items-start">
            <div class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-brand-accent mr-4 shrink-0">
              <i class="fas fa-phone-alt"></i>
            </div>
            <span class="mt-1 hover:text-brand-accentLight transition-colors cursor-pointer">+254 (0) 123 456 789</span>
          </li>
        </ul>
      </div>

    </div>
  </div>
  
  <!-- Bottom Bar -->
  <div class="max-w-7xl mx-auto px-6 mt-8 pt-8 border-t border-slate-800/60 text-center text-sm relative z-10 flex flex-col md:flex-row justify-between items-center text-slate-500">
    <p>&copy; <span id="year"></span> Light and Nature Foundation. All rights reserved.</p>
    <div class="flex space-x-6 mt-4 md:mt-0">
      <a href="#" class="hover:text-brand-accentLight transition-colors">Privacy Policy</a>
      <a href="#" class="hover:text-brand-accentLight transition-colors">Terms of Service</a>
    </div>
  </div>
</footer>"""

files = ['about.html', 'contact.html', 'donate.html', 'gallery.html', 'index.html', 'leadership.html', 'projects.html', 'Resources.html']

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace <!-- FOOTER --> ... </footer>
    # Wait, the previous footer might have newlines or something. We use re.DOTALL
    content = re.sub(r'<!-- FOOTER -->.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Ultra-modern footer applied successfully.')
