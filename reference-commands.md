# Multi-Container Application Deployment Command Reference Guide

### Project content table
- [Section 1: Core Project Workflow](#section-1-core-project-workflow)
- [Section 2: Advanced Operations](#section-2-advanced-operations)
- [Section 3: Production Guide](#section-3-production-guide)

> **Author**: [Md Toriqul Islam](https://linkedin.com/in/TheToriqul)  
> **Description**: Command reference for deploying and managing a Flask/Redis multi-container application  
> **Learning Focus**: docker-compose orchestration and container management  
> **Note**: Review all commands before execution in your environment

## Section 1: Core Project Workflow

### Step 1: Project Setup
```bash
# Create project directory
git clone https://github.com/TheToriqul/multi-container-app-deployment.git
cd multi-container-app-deployment

# Verify directory creation
pwd
ls -la
```

### Step 2: Application Deployment
```bash
# Deploy the application using docker-compose
docker-compose -f compose.yaml up -d

# Verify deployment
docker-compose ps
docker-compose logs
```

### Step 3: Service Verification
```bash
# Test the web application
curl localhost:5001

# Verify Redis connection
docker-compose exec redis redis-cli ping

# Check service logs
docker-compose logs web-fe
docker-compose logs redis
```

### Step 4: Service Management
```bash
# Stop the application
docker-compose stop

# Restart the application
docker-compose restart

# Verify service status after restart
docker-compose ps
```

### Step 5: Resource Verification
```bash
# List volumes
docker volume ls | grep counter-vol

# List networks
docker network ls | grep counter-net

# Verify service processes
docker-compose top
```

### Final Step: Cleanup
```bash
# Stop and remove all resources
docker-compose down --volumes

# Verify cleanup
docker-compose ps
docker volume ls
docker network ls
```

## Section 2: Advanced Operations

### Advanced Container Management
```bash
# Scale web service
docker-compose up -d --scale web-fe=2

# View container distribution
docker-compose ps
```

### Advanced Networking
```bash
# Inspect network details
docker network inspect counter-net

# View network connections
docker network inspect counter-net -f '{{json .Containers}}'
```

### Advanced Volume Operations
```bash
# Inspect volume details
docker volume inspect counter-vol

# Backup volume data
docker run --rm -v counter-vol:/source:ro -v $(pwd):/backup alpine tar -czf /backup/counter-vol-backup.tar.gz -C /source .
```

## Section 3: Production Guide

### Production Setup
```bash
# Build images with production tags
docker-compose -f compose.yaml build --no-cache

# Deploy with production configuration
docker-compose -f compose.yaml -f compose.prod.yaml up -d

# Verify production deployment
docker-compose ps
```

### Monitoring
```bash
# View resource usage
docker stats

# Check container health
docker-compose ps -a

# View application metrics
docker-compose logs web-fe --tail=100 -f
```

### Backup Operations
```bash
# Create volume backup
docker run --rm \
    -v counter-vol:/data \
    -v $(pwd):/backup \
    alpine tar -czf /backup/data-backup.tar.gz /data

# Verify backup file
ls -lh data-backup.tar.gz
```

## Learning Notes

1. Always verify service status after deployment operations
2. Monitor logs regularly for troubleshooting
3. Use volume backups for data persistence
4. Implement proper cleanup procedures
5. Maintain separate production configurations

---

> 💡 **Best Practice**: Always validate the compose file before deployment with `docker-compose config`

> ⚠️ **Warning**: Using `--volumes` flag with `down` command permanently deletes data

> 📝 **Note**: Some commands may require elevated privileges