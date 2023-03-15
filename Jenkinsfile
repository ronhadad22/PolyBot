pipeline {
    
    agent {
      docker {
        image 'Jenkins-agent:latest'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
        

   
    options{
        disableConcurrentBuilds()
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
        stage('Stage II...') {
            steps {
                sh 'echo "Stage II..."'
            }
        }
        
        stage('Stage III..') {
            steps {
                sh 'echo "Stage III..."'
            }
         }
    }
}
