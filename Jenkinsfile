
pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                echo 'Source code is available from GitHub'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test Electricity Bill') {
            steps {
                bat 'python -c "from app import calculate_bill; assert calculate_bill(250) == 600.0; print(\'Electricity Bill Test Passed\')"'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t electricity-bill-app:latest .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                bat 'docker images electricity-bill-app'
            }
        }
    }

    post {
        success {
            echo 'Electricity Bill application Docker image created successfully!'
        }

        failure {
            echo 'Build failed. Check the Jenkins Console Output.'
        }
    }
}
