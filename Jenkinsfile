pipeline {
    agent { dockerfile true }
    stages {
        stage('Build') {
            agent any
            steps {
                sh 'docker build -t my-python-app .'
            }
        }
    }
}
