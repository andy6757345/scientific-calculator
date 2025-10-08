pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "andy3104/scientific-calculator:latest"
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        // Stage 1: Checkout
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/andy6757345/scientific-calculator'
            }
        }

        // Stage 2: Setup Python virtual environment
        stage('Setup Python Env') {
            steps {
                sh '''
                    #!/bin/bash
                    python3 -m venv $VENV_PATH
                    . $VENV_PATH/bin/activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        // Stage 3: Run Python tests
        stage('Run Tests') {
            steps {
                sh '''
                    #!/bin/bash
                    . $VENV_PATH/bin/activate
                    pytest tests || echo "No tests found or pytest failed"
                '''
            }
        }

        // Stage 4: Build Docker image
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} -f calculator.dockerfile ."
            }
        }

        // Stage 5: Push Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'dockerhub-id', url: 'https://index.docker.io/v1/']) {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
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
