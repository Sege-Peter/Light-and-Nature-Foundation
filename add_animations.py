import os
import re

# 1. Write the animations.js file
os.makedirs('assets/js', exist_ok=True)
js_content = """document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.animate-on-scroll');
    
    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('is-revealed');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // 2. Navbar Shrink on Scroll
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('py-2', 'shadow-md', 'bg-white/95');
                navbar.classList.remove('py-3', 'shadow-sm', 'bg-white/80');
            } else {
                navbar.classList.add('py-3', 'shadow-sm', 'bg-white/80');
                navbar.classList.remove('py-2', 'shadow-md', 'bg-white/95');
            }
        });
    }
});
"""
with open('assets/js/animations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Append CSS to style.css
css_addition = """
/* Scroll Reveal Animations */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), 
              transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  will-change: opacity, transform;
}

.animate-on-scroll.is-revealed {
  opacity: 1;
  transform: translateY(0);
}
"""
with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_addition)

# 3. Process all HTML files
files = ['about.html', 'contact.html', 'donate.html', 'gallery.html', 'index.html', 'leadership.html', 'projects.html', 'Resources.html']

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Insert the script tag before </body> if it doesn't exist
    if 'assets/js/animations.js' not in content:
        content = content.replace('</body>', '  <script src="assets/js/animations.js"></script>\n</body>')
    
    # Add .animate-on-scroll to major elements
    # Using regex to target <section>, cards (.bg-white that have shadows), and main images.
    
    # Target <section> tags that don't have id="home" (because hero section shouldn't fade in from bottom usually)
    content = re.sub(r'(<section\b(?![^>]*id="home")[^>]*)class="([^"]*)"', r'\1class="\2 animate-on-scroll"', content)
    # Target <section> tags that have NO class attribute
    content = re.sub(r'(<section\b(?![^>]*id="home")[^>]*)(?<!class=)(>)', r'\1 class="animate-on-scroll"\2', content)

    # Target specific UI cards and grids
    content = content.replace('class="grid md:grid-cols-2', 'class="grid md:grid-cols-2 animate-on-scroll')
    content = content.replace('class="bg-white rounded-xl shadow-lg', 'class="bg-white rounded-xl shadow-lg animate-on-scroll')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Animations added successfully.')
