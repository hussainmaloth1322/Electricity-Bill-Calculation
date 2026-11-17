pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t electricity-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f electricity-container 2>NUL || exit /b 0'
                // Host port 5001 avoids conflict with Q9's default port 5000.
                bat 'docker run -d -p 5001:5000 --name electricity-container electricity-app'
            }
        }
    }

    post {
        success {
            echo 'Electricity bill container started. Test http://localhost:5001/bill?units=250'
        }
    }
}
