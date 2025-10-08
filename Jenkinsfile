pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "andy3104/scientific-calculator:latest"
    }

    stages {
        // Stage 1: Checkout code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/andy6757345/scientific-calculator'
            }
        }

        // Stage 2: Run Python tests (optional)
        stage('Run Tests') {
            steps {
                // If you have test files in tests/ folder
                sh 'pytest tests || echo "No tests found or pytest not installed"'
            }
        }

        // Stage 3: Build Docker image
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        // Stage 4: Push Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-andy3104', url: '']) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
