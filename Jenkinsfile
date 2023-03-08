pipeline {
    agent any
    
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
        stage('push') {
               steps {
                   sh "docker push ayamb99/polybot:poly-bot-${env.BUILD_NUMBER}"
               }
           }
        stage('Stage III ...')  {
                   steps {
                       sh "docker push ayamb99/polybot:poly-bot-${env.BUILD_NUMBER}"
                   }
               }
         post {
           always {
               sh 'docker rmi myapp'
               }
           }
       }
}
