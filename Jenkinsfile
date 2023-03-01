pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               withCredentials([usernamePassword(credentialsId: 'avijw96', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
               sh "sudo docker build -t avijdocker/PolyBot-${env.Build_NUMBER} ."
               sh "sudo docker login --username $user --password $pass"
               sh "sudo docker push avijdocker/PolyBot-${env.Build_NUMBER}"




               sh 'echo building...'
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

