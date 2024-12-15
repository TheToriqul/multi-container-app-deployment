# 🐳 Multi-Container Application Deployment with Docker Compose

[![GitHub Repository](https://img.shields.io/badge/GitHub-multi--container--app--deployment-blue?style=flat&logo=github)](https://github.com/TheToriqul/multi-container-app-deployment)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)

## 📋 Project Overview

This project demonstrates my expertise in deploying and managing multi-container applications using Docker Compose. I've built a scalable web application that combines a Python Flask frontend with a Redis backend, showcasing modern containerization practices and microservices architecture.

## 🎯 Key Objectives

- Implement a multi-container application architecture using Docker Compose
- Develop a Flask web application with Redis integration for state management
- Configure container networking for secure service communication
- Implement persistent storage using Docker volumes
- Create a production-ready container deployment workflow

## 🏗️ Project Architecture

```mermaid
graph TB
    subgraph Docker Host
        subgraph "Docker Compose Environment"
            subgraph "Web Frontend Container"
                F[Flask Application
                Port 8080]
            end
            
            subgraph "Redis Container"
                R[Redis Server 
                Port 6379]
            end
            
            subgraph "Persistent Storage"
                V[counter-vol 
                /app]
            end
            
            subgraph "Network Layer"
                N[counter-net]
            end
        end
        
        P[Host Port 5001]
    end
    
    U[User] --> P
    P --> F
    F --> N
    N --> R
    F --> V
    
    style F fill:#9CBCE2,stroke:#333,stroke-width:2px
    style R fill:#DC382D,stroke:#333,stroke-width:2px
    style V fill:#FFA500,stroke:#333,stroke-width:2px
    style N fill:#85C1E9,stroke:#333,stroke-width:2px
    style P fill:#90EE90,stroke:#333,stroke-width:2px
    style U fill:#FFE4B5,stroke:#333,stroke-width:2px
```

## 💻 Technical Stack

- **Frontend**: Python Flask application
- **Backend**: Redis for data persistence
- **Container Runtime**: Docker Engine
- **Orchestration**: Docker Compose
- **Base Images**: 
  - Python 3.9 Alpine
  - Redis Alpine

## 🚀 Getting Started

<details>
<summary>🐳 Prerequisites</summary>

- Docker Engine (version 20.10.0 or higher)
- Docker Compose V2
- Git (for cloning the repository)
- curl (for testing the deployment)

</details>

<details>
<summary>⚙️ Installation</summary>

1. Clone the repository:
   ```bash
   git clone https://github.com/TheToriqul/multi-container-app-deployment.git
   cd multi-container-app-deployment
   ```

2. Review the configuration files:
   - `app.py`: Flask application code
   - `Dockerfile`: Container image definition
   - `compose.yaml`: Multi-container orchestration configuration

3. Deploy the application:
   ```bash
   docker compose -f compose.yaml up -d
   ```

</details>

<details>
<summary>🎮 Usage</summary>

1. Access the application:
   ```bash
   curl localhost:5001
   ```

2. Monitor the services:
   ```bash
   docker-compose ps
   docker-compose logs
   ```

3. Stop the application:
   ```bash
   docker-compose down --volumes
   ```

For detailed commands and operations, refer to the [reference-commands.md](reference-commands.md) file.

</details>

## 💡 Key Learnings

### Technical Mastery:

1. Docker Compose configuration and service orchestration
2. Container networking and inter-service communication
3. Volume management for persistent storage
4. Multi-stage builds and image optimization
5. Service discovery and load balancing

### Professional Development:

1. Microservices architecture design
2. Infrastructure as Code (IaC) practices
3. DevOps workflow optimization
4. System debugging and troubleshooting
5. Documentation and technical writing

## 🔄 Future Enhancements

<details>
<summary>View Planned Improvements</summary>

1. Implement Docker Swarm for container orchestration
2. Add Nginx reverse proxy for load balancing
3. Implement health checks and automatic container recovery
4. Add monitoring with Prometheus and Grafana
5. Implement CI/CD pipeline with GitHub Actions
6. Add automated testing framework

</details>

## 🙌 Contribution

Contributions are welcome! Feel free to [open an issue](https://github.com/TheToriqul/multi-container-app-deployment/issues) or submit a [pull request](https://github.com/TheToriqul/multi-container-app-deployment/pulls).

## 📧 Connect with Me

- 📧 Email: toriqul.int@gmail.com
- 📱 Phone: +65 8936 7705, +8801765 939006
- 🌐 LinkedIn: [@TheToriqul](https://www.linkedin.com/in/thetoriqul/)
- 🐙 GitHub: [@TheToriqul](https://github.com/TheToriqul)
- 🌍 Portfolio: [TheToriqul.com](https://thetoriqul.com)

## 👏 Acknowledgments
- [Poridhi for providing comprehensive labs and inspiring this project](https://devops.poridhi.io/) 
- The Docker and Docker Compose communities for their excellent documentation
- The Flask and Redis teams for their robust and reliable technologies
- The open-source community for continuous inspiration and learning resources

---

Thank you for exploring this project! I hope it demonstrates my practical experience with container orchestration and microservices architecture. Feel free to reach out if you have any questions or would like to discuss collaboration opportunities! 🚀