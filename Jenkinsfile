pipeline {
    agent any
    options{
        properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '80', numToKeepStr: '100')), 
        disableConcurrentBuilds(), parameters([choice(choices: ['one', 'two'], description: 'this is just for test', name: 'testchoice')]), 
        pipelineTriggers([githubPush()])])  
    }
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    
                  
                 sh "docker build -t ayamb99/polybot:poly-bot-${env.BUILD_NUMBER} . "
                 sh "docker login --username $user --password $pass"
                 sh "docker push ayamb99/polybot:poly-bot-${env.BUILD_NUMBER}"
  //              sh '''
 //               docker login --username $user --password $pass
 //               docker build ...
 //               docker tag ...
 //               docker push ...
 //          '''
       
            }
         }
      }
    }
}
