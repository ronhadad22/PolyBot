pipeline {
agent any 

 //   options{
 //   buildDiscarder(logRotator(numToKeepStr: '30', artifactNumToKeepStr: '30')),
 //   buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '10')), 
 //   disableConcurrentBuilds(), 
 //   parameters([choice(choices: ['one', 'two'], description: 'this is just for testing', name: 'testchioce')]), 
 //   pipelineTriggers([githubPush()])
 //   }
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  sh "sudo docker build -t ronhad/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  sh "sudo docker login --username $user --password $pass"
                  sh "sudo docker push ronhad/private-course:poly-bot-${env.BUILD_NUMBER}"
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
