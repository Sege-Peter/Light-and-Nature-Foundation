import os
import re

new_footer = """<!-- FOOTER -->
<footer class="bg-brand-dark text-brand-light pt-24 pb-0 overflow-hidden rounded-t-[3rem] mt-24 relative shadow-[0_-20px_50px_-20px_rgba(0,0,0,0.1)]">
  <!-- Decorative background elements -->
  <div class="absolute -top-40 -right-40 w-[500px] h-[500px] bg-brand-DEFAULT opacity-20 rounded-full blur-[100px] pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-6 relative z-10">
    
    <!-- Edge-to-edge Map inside the rounded footer -->
    <div class="w-full h-80 rounded-[2rem] overflow-hidden mb-24 shadow-2xl relative group animate-on-scroll border border-white/10">
      <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d255306.90483863756!2d34.62957445!3d-0.1009841!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182aa410d54fa57b%3A0xc34ccf3e230f80bc!2sKisumu%2C%20Kenya!5e0!3m2!1sen!2sus!4v1695840000000!5m2!1sen!2sus" 
        width="100%" height="100%" style="border:0; filter: contrast(1.1) saturate(1.2);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
      </iframe>
      <!-- Overlay to make it feel integrated -->
      <div class="absolute inset-0 bg-brand-dark/40 pointer-events-none transition-opacity duration-700 group-hover:opacity-0 mix-blend-overlay"></div>
      <!-- Hover prompt -->
      <div class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-white/90 backdrop-blur-md px-6 py-2 rounded-full text-xs text-brand-dark shadow-xl opacity-100 transition-opacity duration-500 group-hover:opacity-0 font-bold uppercase tracking-wider pointer-events-none">
        Explore Map
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-20 animate-on-scroll delay-100">
      <div class="col-span-1 md:col-span-2 pr-0 md:pr-12">
        <h3 class="font-display font-bold text-4xl mb-6 text-white leading-tight">Let's grow a better future, together.</h3>
        <p class="text-brand-light/70 text-lg leading-relaxed mb-10 font-light">
          Join our newsletter to stay updated on our latest environmental conservation efforts and community projects across Kenya.
        </p>
        <div class="flex bg-white/10 rounded-full p-1 border border-white/20 backdrop-blur-md focus-within:border-brand-DEFAULT focus-within:bg-white/15 transition-all shadow-inner">
          <input type="email" placeholder="Your email address" class="bg-transparent border-none text-white px-6 py-4 w-full focus:outline-none placeholder-brand-light/50 font-medium" />
          <button class="bg-brand-DEFAULT hover:bg-white hover:text-brand-dark text-white rounded-full px-8 py-3 font-bold transition-colors whitespace-nowrap shadow-lg">Subscribe</button>
        </div>
      </div>
      
      <div class="col-span-1 md:pl-8">
        <h4 class="font-display font-bold text-xl text-white mb-8 relative inline-block">
          Explore
          <div class="absolute -bottom-2 left-0 w-8 h-1 bg-brand-DEFAULT rounded-full"></div>
        </h4>
        <ul class="space-y-4 text-brand-light/70 font-medium">
          <li><a href="about.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300">About Us</a></li>
          <li><a href="projects.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300">Our Projects</a></li>
          <li><a href="gallery.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300">Gallery</a></li>
          <li><a href="donate.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300 text-brand-DEFAULT">Donate Now</a></li>
        </ul>
      </div>

      <div class="col-span-1">
        <h4 class="font-display font-bold text-xl text-white mb-8 relative inline-block">
          Connect
          <div class="absolute -bottom-2 left-0 w-8 h-1 bg-brand-DEFAULT rounded-full"></div>
        </h4>
        <ul class="space-y-4 text-brand-light/70 font-medium mb-10">
          <li><a href="contact.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300">Contact Us</a></li>
          <li><a href="leadership.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300">Leadership</a></li>
          <li><a href="Resources.html" class="hover:text-white hover:translate-x-2 inline-block transition-transform duration-300">Resources</a></li>
        </ul>
        <div class="flex space-x-5">
          <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white hover:bg-brand-DEFAULT hover:text-brand-dark hover:-translate-y-1 transition-all duration-300"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white hover:bg-brand-DEFAULT hover:text-brand-dark hover:-translate-y-1 transition-all duration-300"><i class="fab fa-twitter"></i></a>
          <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white hover:bg-brand-DEFAULT hover:text-brand-dark hover:-translate-y-1 transition-all duration-300"><i class="fab fa-instagram"></i></a>
          <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white hover:bg-brand-DEFAULT hover:text-brand-dark hover:-translate-y-1 transition-all duration-300"><i class="fab fa-linkedin-in"></i></a>
        </div>
      </div>
    </div>
  </div>

  <!-- Massive Typography Footer Bottom -->
  <div class="w-full border-t border-white/10 pt-8 flex flex-col items-center overflow-hidden animate-on-scroll delay-200">
    <div class="max-w-7xl mx-auto w-full px-6 flex flex-col md:flex-row justify-between items-center text-sm text-brand-light/40 mb-12">
      <p>&copy; <span id="year"></span> Light and Nature Foundation.</p>
      <div class="flex space-x-6 mt-4 md:mt-0">
        <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
        <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
      </div>
    </div>
    
    <!-- Massive Logo Text -->
    <h1 class="text-[11vw] leading-none font-display font-black text-white/5 select-none whitespace-nowrap tracking-tighter" style="margin-bottom: -1vw;">
      LIGHT & NATURE
    </h1>
  </div>
</footer>"""

files = ['about.html', 'contact.html', 'donate.html', 'gallery.html', 'index.html', 'leadership.html', 'projects.html', 'Resources.html']

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(r'<!-- FOOTER -->.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Spectacular new footer injected.')
