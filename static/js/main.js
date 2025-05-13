window.addEventListener('DOMContentLoaded', () => {
    tsParticles.load('tsparticles', {
        particles: {
            number: { value: 80 },
            size: { value: 3 },
            move: { speed: 1 },
            opacity: { value: { min: 0.3, max: 0.8 } },
        },
        interactivity: {
            events: {
                onhover: { enable: true, mode: 'repulse' },
                onclick: { enable: true, mode: 'push' }
            },
            modes: { repulse: { distance: 100 }, push: { quantity: 4 } }
        }
    });
});