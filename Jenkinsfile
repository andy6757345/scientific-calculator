pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/andy6757345/scientific-calculator.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest tests.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('andy3104/scientific-calculator:latest')
                }
            }
        }
stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-id') {
                        def app = docker.image('andy3104/scientific-calculator:latest')
                        app.push()
                    }
                }
            }
        }

    }
    


    post {
        success {
            echo 'Pipeline Succeeded!'
        }
        failure {
            echo 'Pipeline Failed!'
        }
    }
}
