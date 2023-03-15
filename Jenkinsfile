pipeline {
    
  
    options{
         buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '10'))
         disableConcurrentBuilds()
    }
    
    agent {
      docker {
        image 'jenkins-agent:latest'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    environment{
        SNYK_TOKEN = credentials('snyk-token')
    }
    
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    
                  
                 sh "docker build -t ayamb99/polybot:poly-bot-${env.BUILD_NUMBER} . "
                 sh "docker login --username $user --password $pass"
  //              sh '''
 //               docker login --username $user --password $pass
 //               docker build ...
 //               docker tag ...
 //               docker push ...
 //          '''
       
            }
         }
      }
        stage('snyk test') {
            steps {
                sh "snyk container test --severity-threshold=high ayamb99/polybot:poly-bot-${env.BUILD_NUMBER} --file=Dockerfile"
            }
        }
        
        stage('push') {
            steps {
                sh "docker push ayamb99/polybot:poly-bot-${env.BUILD_NUMBER}"
            }
         }
    }
}
