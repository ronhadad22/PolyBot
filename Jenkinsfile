pipeline {
    agent any
    stages {
        stage('Build Bot app') {
   steps {
   withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
    // some block
       bat '''
            docker login --username $happytoast --password $myaccesstoken
            docker push happytoast/build_bot
            docker build .
       '''
       }
   }
}
        stage('Build') {
            steps {
                bat 'set'
            }
        }
    }
}