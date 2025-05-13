from flask import Flask, render_template_string

app = Flask(__name__)

# HTML stylisé avec Bootstrap et animations personnalisées
HTML_PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Bienvenue chez Ali</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            padding-top: 100px;
            animation: fadeIn 1s ease-in;
            overflow: hidden;
        }
        .container {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.4);
            animation: slideIn 1s ease-in;
            position: relative;
        }
        h1 {
            font-size: 3em;
            font-weight: 700;
            animation: bounceIn 1s ease-in;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        p {
            font-size: 1.3em;
            margin-top: 20px;
            font-weight: 300;
            line-height: 1.6;
        }
        .icon {
            font-size: 3em;
            margin-bottom: 20px;
            animation: rotateIn 1s ease-in;
            display: block;
        }
        .btn {
            margin-top: 30px;
            padding: 12px 25px;
            font-size: 1.2em;
            border-radius: 25px;
            background-color: #17a2b8;
            border: none;
            transition: all 0.3s ease;
        }
        .btn:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
            background-color: #138496;
        }
        .particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            animation: fadeIn 2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes bounceIn {
            from { transform: scale(0.5); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        @keyframes rotateIn {
            from { transform: rotate(-180deg); opacity: 0; }
            to { transform: rotate(0deg); opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="particles">
        <canvas id="particleCanvas"></canvas>
    </div>
    <div class="container">
        <span class="icon">👋</span>
        <h1>Bonjour à tous !</h1>
        <p>Bienvenue sur l'application <strong>Flask</strong> conteneurisée avec <strong>Docker</strong>.</p>
        <p>Développée avec ❤️ par <strong>king</strong>.</p>
        <p>🚀 Simple. Propre. Dockerisé.</p>
        <a href="#" class="btn btn-primary">Découvrir plus</a>
    </div>
    <script>
        // Animation de particules simples
        const canvas = document.getElementById('particleCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particlesArray = [];
        const numberOfParticles = 50;

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 5 + 1;
                this.speedX = Math.random() * 1 - 0.5;
                this.speedY = Math.random() * 1 - 0.5;
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.size > 0.2) this.size -= 0.1;
            }
            draw() {
                ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function init() {
            for (let i = 0; i < numberOfParticles; i++) {
                particlesArray.push(new Particle());
            }
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particlesArray.length; i++) {
                particlesArray[i].update();
                particlesArray[i].draw();
                if (particlesArray[i].size <= 0.2) {
                    particlesArray.splice(i, 1);
                    i--;
                    particlesArray.push(new Particle());
                }
            }
            requestAnimationFrame(animate);
        }

        init();
        animate();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)