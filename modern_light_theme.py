import os
import re

# 1. Update style.css
css_content = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap');

:root {
  --brand-DEFAULT: #16a34a;
  --bg-light: #f8fafc;
  --card-bg: #ffffff;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-light);
  color: #1e293b;
  overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6, .font-heading {
  font-family: 'Outfit', sans-serif;
  letter-spacing: -0.02em;
}

/* Modern Light UI Enhancements */
.glass-panel {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.5);
}

.hover-lift {
  position: relative;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.hover-lift:hover {
  transform: translateY(-8px);
  z-index: 10;
}

.hover-lift::after {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border-radius: inherit;
  opacity: 0;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15); /* Soft, large shadow */
  transition: opacity 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  z-index: -1;
  pointer-events: none;
}
.hover-lift:hover::after {
  opacity: 1;
}

/* Text Gradient */
.text-gradient {
  background: linear-gradient(135deg, #14532d, #16a34a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Image Hover Effects */
img {
  transition: transform 0.7s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.group:hover img {
  transform: scale(1.03);
}

/* Scroll Reveal Animations */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.165, 0.84, 0.44, 1), 
              transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
  will-change: opacity, transform;
}
.animate-on-scroll.is-revealed {
  opacity: 1;
  transform: translateY(0);
}
"""
with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

files = ['about.html', 'contact.html', 'donate.html', 'gallery.html', 'index.html', 'leadership.html', 'projects.html', 'Resources.html']

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the tailwind config and fonts in <head>
    head_pattern = r'<head>.*?</head>'
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
              light: '#f0fdf4',
              DEFAULT: '#16a34a',
              dark: '#14532d',
              accent: '#10b981',
              accentLight: '#34d399',
              gray: '#f8fafc',
            }
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            serif: ['Outfit', 'sans-serif'],
          }
        }
      }
    }
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" type="image/png" href="assets/images/lnf log.jpeg">
</head>"""
    content = re.sub(head_pattern, new_head, content, flags=re.DOTALL)
    
    # Body replacements
    content = re.sub(r'<body class="[^"]*">', '<body class="bg-slate-50 text-slate-800 font-sans antialiased selection:bg-brand-DEFAULT selection:text-white">', content)
    
    # Text colors
    content = content.replace('text-white', 'text-slate-900')
    # Because we just replaced text-white to text-slate-900, the footer CTA button that needs white text is now text-slate-900.
    # We will fix button texts specifically later.
    content = content.replace('text-zinc-400', 'text-slate-600')
    content = content.replace('text-zinc-500', 'text-slate-500')
    content = content.replace('text-zinc-300', 'text-slate-700')
    content = content.replace('text-[#111]', 'text-slate-900')

    # Typography
    content = content.replace('font-black tracking-tighter uppercase', 'font-serif font-bold tracking-tight text-slate-900')
    
    # Backgrounds
    content = content.replace('bg-[#0a0a0a]', 'bg-slate-50')
    content = content.replace('bg-[#111]', 'bg-white')
    content = content.replace('bg-[#050505]', 'bg-slate-900')
    content = content.replace('bg-[#222]', 'bg-slate-100')
    content = content.replace('bg-black/80', 'bg-white/80')
    content = content.replace('bg-black/95', 'bg-white/95')
    content = content.replace('bg-black', 'bg-white')
    
    # Borders
    content = content.replace('border-white/10', 'border-slate-200')
    content = content.replace('border-white/20', 'border-slate-300')
    
    # Buttons
    content = content.replace('bg-brand-DEFAULT text-black hover:bg-white', 'bg-brand-DEFAULT text-white hover:bg-brand-dark')
    content = content.replace('bg-white text-black hover:bg-brand-DEFAULT', 'bg-white text-slate-900 hover:bg-slate-50 border border-slate-200')
    
    # Shadows
    content = content.replace('hover:shadow-[0_0_30px_rgba(204,255,0,0.4)]', 'hover:shadow-xl')
    content = content.replace('shadow-[0_0_40px_rgba(4,120,87,0.15)]', 'shadow-2xl')
    
    # Fix footer map text and buttons that were inverted
    # "Join our mission" area
    content = content.replace('bg-white/50 p-8', 'bg-white p-8 shadow-xl border-slate-100')
    content = content.replace('bg-slate-100 text-slate-900 px-5 py-3', 'bg-white text-slate-900 px-5 py-3 border-slate-200')
    
    # Specific fix for dark map filter to standard map or light stylized
    content = content.replace('invert(90%) hue-rotate(180deg) brightness(80%) contrast(90%)', 'brightness(95%) contrast(110%) saturate(120%)')
    
    # Fix the footer text since we replaced bg-black with bg-white but footer should still maybe be slightly separated
    # Actually, a clean modern look often has a white footer or a very light gray footer.
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Modern Light Theme applied successfully.')
