pipeline {
    agent {
        label 'linux-agent'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vigu2019/jenkins-docker-cicd.git'
            }
        }

        stage('Agent Details') {
            steps {
                sh 'hostname'
                sh 'whoami'
            }
        }

        stage('Check Tools') {
            steps {
                sh 'docker --version'
                sh 'python3 --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-flask-app:latest .'
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt pytest requests'
                sh './venv/bin/pytest -v test_app.py'
            }
        }
    }
}
