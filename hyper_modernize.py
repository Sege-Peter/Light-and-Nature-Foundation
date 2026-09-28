import os
import re

# 1. Update style.css
css_content = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;900&display=swap');

:root {
  --neon: #ccff00;
  --bg-dark: #000000;
  --card-bg: #0a0a0a;
}

body {
  font-family: 'Outfit', sans-serif;
  background-color: var(--bg-dark);
  color: #ffffff;
  overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6, .font-heading {
  font-family: 'Outfit', sans-serif;
  letter-spacing: -0.04em;
}

/* Hyper-Modern UI Enhancements */
.glass-panel {
  background: rgba(10, 10, 10, 0.6);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.hover-lift {
  position: relative;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.hover-lift:hover {
  transform: translateY(-8px) scale(1.02);
  z-index: 10;
}

.hover-lift::after {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border-radius: inherit;
  opacity: 0;
  box-shadow: 0 0 40px rgba(204, 255, 0, 0.15); /* Neon shadow */
  transition: opacity 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  z-index: -1;
  pointer-events: none;
}
.hover-lift:hover::after {
  opacity: 1;
}

/* Neon Text Utilities */
.text-gradient {
  color: var(--neon);
  text-shadow: 0 0 20px rgba(204,255,0,0.5);
}

/* Image Hover Effects */
img {
  transition: filter 0.5s ease, transform 0.5s ease;
}
.group:hover img {
  filter: contrast(1.2) brightness(1.1);
  transform: scale(1.05);
}

/* Scroll Reveal Animations */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(50px) scale(0.98);
  transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), 
              transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  will-change: opacity, transform;
}
.animate-on-scroll.is-revealed {
  opacity: 1;
  transform: translateY(0) scale(1);
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
              light: '#ffffff',
              DEFAULT: '#ccff00',
              dark: '#000000',
              accent: '#ccff00',
              accentLight: '#d9ff33',
              gray: '#0a0a0a',
            }
          },
          fontFamily: {
            sans: ['Outfit', 'sans-serif'],
            serif: ['Outfit', 'sans-serif'],
          }
        }
      }
    }
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" type="image/png" href="assets/images/lnf log.jpeg">
</head>"""
    content = re.sub(head_pattern, new_head, content, flags=re.DOTALL)
    
    # Replace body tags for dark mode
    content = re.sub(r'<body class="[^"]*">', '<body class="bg-black text-white font-sans antialiased selection:bg-brand-DEFAULT selection:text-black">', content)
    
    # Typography upgrades
    content = content.replace('font-serif', 'font-black tracking-tighter uppercase')
    content = content.replace('text-slate-800', 'text-white')
    content = content.replace('text-slate-600', 'text-zinc-400')
    content = content.replace('text-brand-dark', 'text-white')
    content = content.replace('text-slate-500', 'text-zinc-500')
    content = content.replace('text-slate-400', 'text-zinc-400')
    
    # Backgrounds and containers
    content = content.replace('bg-slate-50', 'bg-[#0a0a0a]')
    content = content.replace('bg-white', 'bg-[#111]')
    content = content.replace('bg-white/80', 'bg-black/80')
    content = content.replace('bg-white/95', 'bg-black/95 border-b border-white/10')
    content = content.replace('border-slate-200', 'border-white/10')
    content = content.replace('border-slate-100', 'border-white/10')
    content = content.replace('bg-brand-dark', 'bg-[#050505]')
    content = content.replace('bg-slate-950', 'bg-black')
    content = content.replace('bg-slate-900', 'bg-[#111]')
    content = content.replace('bg-slate-800', 'bg-[#222]')
    content = content.replace('border-slate-800', 'border-white/10')
    content = content.replace('border-slate-700', 'border-white/20')
    
    # Buttons and neon glows
    content = content.replace('bg-brand-accent text-white hover:bg-brand-dark', 'bg-brand-DEFAULT text-black hover:bg-white hover:shadow-[0_0_30px_rgba(204,255,0,0.4)]')
    content = content.replace('bg-brand-dark text-white hover:bg-brand-accent', 'bg-white text-black hover:bg-brand-DEFAULT hover:shadow-[0_0_30px_rgba(204,255,0,0.4)]')
    content = content.replace('bg-white text-brand-dark hover:bg-brand-light', 'bg-white text-black hover:bg-brand-DEFAULT')
    
    # Specifically fix the navbar classes
    content = content.replace('text-slate-600 hover:text-brand-accent', 'text-zinc-300 hover:text-brand-DEFAULT')
    
    # Ensure rounded corners are massive for modern feel
    content = content.replace('rounded-xl', 'rounded-[2rem]')
    content = content.replace('rounded-lg', 'rounded-2xl')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Hyper-modern style applied successfully.')
