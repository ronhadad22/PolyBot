pipeline {
    agent any

    stages {
        stage('Build PolyBot') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')]) {


                sh '''

                docker login --username $user --password $pass
                docker build ...
                docker tag ...
                docker push ...
           '''
                }
            }
        }
        stage('Stage II PolyBot') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III PolyBot') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}