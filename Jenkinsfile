pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-login', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  sh "docker build -t kubealon/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  sh "docker login --username $user --password $pass"
                  sh "docker push kubealon/private-course:poly-bot-${env.BUILD_NUMBER}"
 //               sh '''
 //               docker login --username $user --password $pass
 //               docker build ...
 //               docker tag ...
 //               docker push ...
 //          '''
                }
            }
        }
        stage('Stage II') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}
