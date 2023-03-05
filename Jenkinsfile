pipeline {
    agent {
        docker {
            image 'https://hub.docker.com/layers/kubealon/private-course/poly-bot-22/images/sha256-510d4f31c24cb82254529f022bfd827c9a47d3565d235d2bedfd7e0eb6cd78f3?context=repo'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }


    options {
    buildDiscarder(logRotator(daysToKeepStr: '30'))
    disableConcurrentBuilds()
    timestamps()
    }

   
    
    
    stages {
          stage('Build') {
              options {
                  timeout(time: 10, unit: 'MINUTES')
                  }
            steps {
                    withCredentials([usernamePassword(credentialsId: 'github-login', passwordVariable: 'pass', usernameVariable: 'user'), string(credentialsId: 'telegram-token', variable: 'TELEGRAM_TOKEN')]) {
                    sh "echo $pass |  sudo -S docker build --build-arg TELEGRAM_TOKEN=$TELEGRAM_TOKEN -t kubealon/private-course:poly-bot-${env.BUILD_NUMBER} ."
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                        sh "echo $DOCKERHUB_PASSWORD | sudo -S docker login --username $DOCKERHUB_USERNAME --password-stdin"
                        sh "sudo docker push kubealon/private-course:poly-bot-${env.BUILD_NUMBER}"
                        sh "echo $pass | sudo -S docker push kubealon/private-course:poly-bot-${env.BUILD_NUMBER}"
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
    post {
        always {
            // Cleanup Docker images from the disk
            sh 'sudo docker system prune -af'
        }
    }
}
