document.addEventListener('DOMContentLoaded', () => {
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
