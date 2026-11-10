
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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest requests
                    pytest -v
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                            -u "$DOCKER_USER" \
                            --password-stdin

                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Node2') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'node2-ssh-credentials',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {
                    sh '''
                        ssh -i "$SSH_KEY" \
                            -o StrictHostKeyChecking=accept-new \
                            "$SSH_USER@172.31.13.201" '
                            
                            docker pull vigu1926/jenkins-flask-app:latest

                            docker rm -f flask-deployment || true

                            docker run -d \
                                --name flask-deployment \
                                --restart unless-stopped \
                                -p 5000:5000 \
                                vigu1926/jenkins-flask-app:latest
                        '
                    '''
                }
            }
        }
    }
}
