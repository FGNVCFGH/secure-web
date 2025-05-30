from flask import Flask, render_template_string, request, redirect, url_for, session, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ADMIN_PASSWORD = 'R@J192856'

@app.route('/auto-login', methods=['POST'])
def auto_login():
    session['logged_in'] = True
    return ('', 204)

@app.route('/', methods=['GET', 'POST'])
def home():
    is_admin = session.get('logged_in', False)

    if request.method == 'POST' and is_admin:
        file = request.files.get('file')
        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return redirect(url_for('home'))

    files = os.listdir(UPLOAD_FOLDER)
    file_links = ''.join(f'<li><a href="/download/{f}">{f}</a></li>' for f in files)

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Secure Hacker Web</title>
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        body {
            font-family: 'Share Tech Mono', monospace;
        }


        html, body {
            margin: 0;
            padding: 0;
            background: black;
            color: #00ff00;
            font-family: 'Share Tech Mono', monospace;
            overflow: hidden;
        }

        canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: 0;
            opacity: 0.1;
        }

        .content {
            position: relative;
            z-index: 1;
            text-align: center;
            padding: 20px;
        }

        .glitch {
            text-shadow: 0 0 5px #0f0;
            font-size: 2.8em;
            animation: flicker 1.5s infinite;
        }

        .dev-name {
            font-size: 1.6em;
            text-shadow: 0 0 4px #0f0;
        }

        @keyframes flicker {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        ul {
            list-style: none;
            padding: 0;
            margin-top: 30px;
        }

        li {
            margin-bottom: 10px;
            font-size: 18px;
        }

        
        
        li a {
            display: inline-block;
            margin: 5px;
            padding: 4px 10px;
            color: #00ff00;
            background: transparent;
            border: none;
            border-radius: 0;
            text-decoration: none;
            font-family: 'Share Tech Mono', monospace;
            font-size: 16px;
            transition: all 0.3s ease-in-out;
        }

        li a:hover {
            color: #ff0000;
            background: none;
            text-shadow: 0 0 8px #ff0000;
            transform: scale(1.1);
        }

        .download-animation {
            animation: vibrate 0.2s linear 1;
        }

        @keyframes vibrate {
            0% { transform: translateX(0); }
            25% { transform: translateX(-3px); }
            50% { transform: translateX(3px); }
            75% { transform: translateX(-3px); }
            100% { transform: translateX(0); }
        }
    
            display: inline-block;
            margin: 5px;
            padding: 4px 10px;
            color: #00ff00;
            background: transparent;
            border: none;
            border-radius: 0;
            text-decoration: none;
            transition: 0.3s ease-in-out;
        }

        li a:hover {
            color: #ff0000;
            transform: scale(1.1);
            text-shadow: 0 0 5px #ff0000;
        }

        .download-animation {
            animation: vibrate 0.2s linear 1;
        }

        @keyframes vibrate {
            0% { transform: translateX(0); }
            25% { transform: translateX(-2px); }
            50% { transform: translateX(2px); }
            75% { transform: translateX(-2px); }
            100% { transform: translateX(0); }
        }

            color: inherit;
            text-decoration: none;
            border: 1px solid #00ff00;
            padding: 5px 10px;
            border-radius: 5px;
        }

        .upload-form {
            margin-top: 30px;
            border: 1px solid #0f0;
            padding: 10px;
            display: inline-block;
        }

        input[type=file], button {
            background: black;
            font-family: 'Share Tech Mono', monospace;
            font-size: 14px;
            color: #00ff00;
            border: 1px solid #00ff00;
            padding: 10px;
            margin: 10px;
            cursor: pointer;
            transition: 0.3s;
        }

        input[type=file]:hover, button:hover {
            background: #ff0000;
            color: #ffffff;
            border-color: #ff0000;
        }
            background: transparent;
            color: #0f0;
            border: none;
            border-bottom: 1px solid #0f0;
            margin: 5px;
            padding: 10px;
            font-size: 14px;
        }

        .secret-heart {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 24px;
            cursor: pointer;
            opacity: 0.3;
            z-index: 100;
        }

        .secret-heart:hover {
            opacity: 1;
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 200;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.9);
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background-color: black;
            padding: 30px;
            border: 1px solid #00ff00;
            color: #0f0;
        }

        .modal input, .modal button {
            padding: 10px;
            margin-top: 10px;
            border: 1px solid #0f0;
            background: black;
            color: #0f0;
        }
        
        .file-box {
            margin: 30px auto 0 auto;
            width: fit-content;
            padding: 20px;
            border: 1px solid #00ff00;
            box-shadow: 0 0 10px #00ff00;
            background-color: rgba(0, 0, 0, 0.6);
        }

        .file-title {
            font-size: 1.5em;
            margin-bottom: 15px;
            color: #00ff00;
            text-shadow: 0 0 5px #00ff00;
        }

        
        
        li a {
            display: inline-block;
            margin: 5px;
            padding: 4px 10px;
            color: #00ff00;
            background: transparent;
            border: none;
            border-radius: 0;
            text-decoration: none;
            font-family: 'Share Tech Mono', monospace;
            font-size: 16px;
            transition: all 0.3s ease-in-out;
        }

        li a:hover {
            color: #ff0000;
            background: none;
            text-shadow: 0 0 8px #ff0000;
            transform: scale(1.1);
        }

        .download-animation {
            animation: vibrate 0.2s linear 1;
        }

        @keyframes vibrate {
            0% { transform: translateX(0); }
            25% { transform: translateX(-3px); }
            50% { transform: translateX(3px); }
            75% { transform: translateX(-3px); }
            100% { transform: translateX(0); }
        }
    
            display: inline-block;
            margin: 5px;
            padding: 4px 10px;
            color: #00ff00;
            background: transparent;
            border: none;
            border-radius: 0;
            text-decoration: none;
            transition: 0.3s ease-in-out;
        }

        li a:hover {
            color: #ff0000;
            transform: scale(1.1);
            text-shadow: 0 0 5px #ff0000;
        }

        .download-animation {
            animation: vibrate 0.2s linear 1;
        }

        @keyframes vibrate {
            0% { transform: translateX(0); }
            25% { transform: translateX(-2px); }
            50% { transform: translateX(2px); }
            75% { transform: translateX(-2px); }
            100% { transform: translateX(0); }
        }

            display: inline-block;
            margin: 5px;
            padding: 6px 12px;
            color: #00ff00;
            border: 1px solid #00ff00;
            border-radius: 5px;
            text-decoration: none;
            transition: 0.3s;
        }

        li a:hover {
            background-color: #00ff00;
            color: black;
        }
    </style>
    </head>
    <body>
        <canvas id="matrixCanvas"></canvas>

        <div class="content">
            <h1 class="glitch">⚠ Secure Hacker Web ⚠</h1>
            <h2 class="glitch dev-name">⚠ Developed by Raj Panchal ⚠</h2>

            <div class="file-box">
                <h3 class="file-title">💾 Uploaded Files</h3>
                <ul>
                {{ file_links|safe }}
            </ul>
            </div>

            {% if is_admin %}
            <div class="upload-form">
                <form method="POST" enctype="multipart/form-data" onsubmit="playUploadEffect()">
                    <input type="file" name="file" required>
                    <button type="submit">Upload</button>
                </form>
            </div>
            {% endif %}
        </div>

        <div class="secret-heart" onclick="showModal()">❤️</div>

        <div class="modal" id="loginModal">
            <div class="modal-content">
                <h3>Admin Access</h3>
                <input type="password" id="secretPassword" placeholder="Enter Password"><br>
                <button onclick="submitPassword()">Login</button>
            </div>
        </div>

        <script>
            function showModal() {
                document.getElementById("loginModal").style.display = "flex";
            }

            function submitPassword() {
                const entered = document.getElementById("secretPassword").value;
                const correct = "{{ password }}";

                if (entered === correct) {
                    fetch("/auto-login", { method: "POST" })
                        .then(() => location.reload());
                } else {
                    alert("Wrong password!");
                }
            }

            function playUploadEffect() {
                const beep = new Audio("https://www.soundjay.com/button/sounds/button-29.mp3");
                beep.play();
                document.body.style.boxShadow = "0 0 60px #0f0 inset";
                setTimeout(() => {
                    document.body.style.boxShadow = "none";
                }, 300);
            }

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    document.getElementById("loginModal").style.display = "none";
                }
            });

            // Matrix effect
            const canvas = document.getElementById("matrixCanvas");
            const ctx = canvas.getContext("2d");
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const letters = "01";
            const fontSize = 12;
            const columns = canvas.width / fontSize * 1.1;
            const drops = Array.from({ length: columns }).fill(1);

            function drawMatrix() {
                ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = "#0f0";
                ctx.font = fontSize + "px monospace";
                for (let i = 0; i < drops.length; i++) {
                    const text = letters[Math.floor(Math.random() * letters.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    drops[i]++;
                }
            }

            setInterval(drawMatrix, 40);
            document.querySelectorAll("a").forEach(link => {
                link.addEventListener("click", (e) => {
                    link.classList.add("download-animation");
                    setTimeout(() => link.classList.remove("download-animation"), 300);
                });
            });
document.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", (e) => {
                link.classList.add("download-animation");
                setTimeout(() => link.classList.remove("download-animation"), 300);
            });
        });
        </script>
    </body>
    </html>
    ''', file_links=file_links, is_admin=is_admin, password=ADMIN_PASSWORD)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
