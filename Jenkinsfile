pipeline {
    agent any

    stages {
          stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-login', passwordVariable: 'pass', usernameVariable: 'user'), string(credentialsId: 'telegram-token', variable: 'TELEGRAM_TOKEN')]) {
                    sh "echo $pass |   docker build --build-arg TELEGRAM_TOKEN=$TELEGRAM_TOKEN -t kubealon/private-course:poly-bot-${env.BUILD_NUMBER} ."
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                        sh "echo $DOCKERHUB_PASSWORD | sudo -S docker login --username $DOCKERHUB_USERNAME --password-stdin"
                        sh "sudo docker push kubealon/private-course:poly-bot-${env.BUILD_NUMBER}"
                        sh "echo $pass | sudo -S docker push kubealon/private-course:poly-bot-${env.BUILD_NUMBER}"
                        sh "echo $pass | sudo -S docker build ..."
                        sh "echo $pass | sudo -S docker tag ..."
                        sh "echo $pass | sudo -S docker push ..."
                    }
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
                sh 'echo "stage III..."'
            }
        }
    }
}
