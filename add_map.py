import os
import re

map_html = """
    <!-- Interactive Map -->
    <div class="relative w-full h-96 mb-16 overflow-hidden rounded-3xl border border-slate-800 shadow-[0_0_40px_rgba(4,120,87,0.15)] animate-on-scroll group">
      <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d255306.90483863756!2d34.62957445!3d-0.1009841!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182aa410d54fa57b%3A0xc34ccf3e230f80bc!2sKisumu%2C%20Kenya!5e0!3m2!1sen!2sus!4v1695840000000!5m2!1sen!2sus" 
        width="100%" 
        height="100%" 
        style="border:0; filter: invert(90%) hue-rotate(180deg) brightness(80%) contrast(90%); transition: filter 0.5s ease;" 
        allowfullscreen="" 
        loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade"
        class="group-hover:filter-none">
      </iframe>
      <!-- Map Overlay for better blending -->
      <div class="absolute inset-0 bg-slate-950/20 pointer-events-none transition-opacity duration-500 group-hover:opacity-0"></div>
      
      <!-- Hover prompt -->
      <div class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-slate-900/80 backdrop-blur px-4 py-2 rounded-full text-xs text-brand-accent border border-brand-accent/30 pointer-events-none opacity-100 transition-opacity duration-500 group-hover:opacity-0">
        <i class="fas fa-search-location mr-2"></i> Interact with map
      </div>
    </div>
"""

files = ['about.html', 'contact.html', 'donate.html', 'gallery.html', 'index.html', 'leadership.html', 'projects.html', 'Resources.html']

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to insert this right before "<!-- Top Call to Action -->"
    if '<!-- Interactive Map -->' not in content:
        content = content.replace('<!-- Top Call to Action -->', map_html + '\n    <!-- Top Call to Action -->')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Map added successfully.')
