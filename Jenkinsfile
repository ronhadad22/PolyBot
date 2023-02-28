pipeline {

    options{
    buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '10'))
    disableConcurrentBuilds()

   }
    agent{
     docker {
        image 'jenkins-agent:latest'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
    }
    
        parameters { choice(choices: ['one', 'two'], description: 'this is just for testing', name: 'testchioce') }

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  sh "docker build -t ronhad/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  sh "docker login --username $user --password $pass"
                  sh "docker push ronhad/private-course:poly-bot-${env.BUILD_NUMBER}"
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
