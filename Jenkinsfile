pipeline {
    agent {
        kubernetes {
            label 'slave'
        }
    }
    stages {
        stage('Hello') {
            steps {
                sh 'echo Hello World!'
            }
        }
    }
}
