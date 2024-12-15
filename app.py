from flask import Flask, render_template_string
from redis import Redis
import socket
import datetime
import platform
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Container App Dashboard</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #2C3E50 0%, #3498DB 100%);
            color: #ffffff;
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .header {
            text-align: center;
            padding: 2rem 0;
            margin-bottom: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        .header h1 {
            margin: 0;
            font-size: 2.5rem;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .header p {
            margin: 0.5rem 0 0;
            font-size: 1.2rem;
            opacity: 0.9;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 10px;
            backdrop-filter: blur(5px);
            transition: transform 0.3s ease;
            height: 200px;
        }
        .stat-card:hover {
            transform: translateY(-5px);
        }
        .stat-card i {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #2ECC71;
        }
        .stat-card h3 {
            margin: 0;
            font-size: 1.2rem;
            color: #ffffff;
            opacity: 0.9;
        }
        .stat-card p {
            margin: 0.5rem 0 0;
            font-size: 1.1rem;
            color: #ffffff;
        }
        .footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem;
            font-size: 0.9rem;
            opacity: 0.7;
        }
        .service-status {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }
        .status-connected {
            background-color: #2ECC71;
        }
        .status-disconnected {
            background-color: #E74C3C;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fab fa-docker"></i> Multi-Container Application Dashboard</h1>
            <p>Docker Compose Flask-Redis Application</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <i class="fas fa-layer-group"></i>
                <h3>Container Architecture</h3>
                <p>Running on Docker Compose</p>
                <p>Network: counter-net</p>
                <p>Volume: counter-vol</p>
            </div>
            
            <div class="stat-card">
                <i class="fas fa-flask"></i>
                <h3>Flask Frontend Service</h3>
                <p>Container: {{ hostname }}</p>
                <p>Internal Port: 8080</p>
                <p>External Port: 5001</p>
            </div>
            
            <div class="stat-card">
                <i class="fas fa-database"></i>
                <h3>Redis Backend Service</h3>
                <p>Host: redis</p>
                <p>Port: 6379</p>
                <p class="service-status {{ 'status-connected' if redis_status == 'Connected' else 'status-disconnected' }}">
                    {{ redis_status }}
                </p>
            </div>

            <div class="stat-card">
                <i class="fas fa-chart-line"></i>
                <h3>Visit Statistics</h3>
                <p>Total Visits: {{ visit_count }}</p>
                <p>Container IP: {{ ip_address }}</p>
                <p>Last Visit: {{ current_time }}</p>
            </div>

            <div class="stat-card">
                <i class="fas fa-network-wired"></i>
                <h3>Network Details</h3>
                <p>Hostname: {{ hostname }}</p>
                <p>Network Mode: Bridge</p>
                <p>Domain: counter-net</p>
            </div>

            <div class="stat-card">
                <i class="fas fa-code-branch"></i>
                <h3>Environment Info</h3>
                <p>Python: {{ python_version }}</p>
                <p>Platform: {{ platform_info }}</p>
                <p>Timezone: {{ timezone }}</p>
            </div>
        </div>

        <div class="footer">
            <p>Multi-Container App Demo | Flask + Redis on Docker Compose</p>
            <p>Created by Md Toriqul Islam | <a href="https://github.com/TheToriqul" target="_blank"><i class="fab fa-github"></i> GitHub</a></p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def hello():
    try:
        visit_count = redis.incr('hits')
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        redis_status = "Connected" if redis.ping() else "Disconnected"
        
        # Environment information
        python_version = platform.python_version()
        platform_info = f"{platform.system()} {platform.machine()}"
        timezone = datetime.datetime.now().astimezone().tzname()
        
        return render_template_string(HTML_TEMPLATE,
            visit_count=visit_count,
            hostname=hostname,
            ip_address=ip_address,
            current_time=current_time,
            redis_status=redis_status,
            python_version=python_version,
            platform_info=platform_info,
            timezone=timezone
        )
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)