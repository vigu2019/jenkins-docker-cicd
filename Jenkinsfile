pipeline {
    agent {
        label 'linux-agent'
    }

    environment {
        DOCKER_IMAGE = 'vigu1926/jenkins-flask-app'
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
                sh '''
                    docker build \
                      -t ${DOCKER_IMAGE}:${BUILD_NUMBER} \
                      -t ${DOCKER_IMAGE}:latest .
                '''
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt pytest requests'
                sh './venv/bin/pytest -v test_app.py'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login \
                          -u "$DOCKERHUB_USER" --password-stdin

                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest

                        docker logout
                    '''
                }
            }
        }
    }
}
