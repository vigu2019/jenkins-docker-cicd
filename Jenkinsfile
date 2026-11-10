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
    }
}
