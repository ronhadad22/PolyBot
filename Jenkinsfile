pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  sh "sudo docker build -t aviyaaqov/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  sh "sudo docker login --username $user --password $pass"
                  sh "sudo docker push aviyaaqov/private-course:poly-bot-${env.BUILD_NUMBER}"
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
