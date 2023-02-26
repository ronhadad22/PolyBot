pipeline {
    agent any
    stages {
        stage('Build Bot app') {
   steps {
   withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
    // some block
            bat "docker login --username $happytoast --password $myaccesstoken"
            bat "docker push happytoast/build_bot"
            bat "docker build ."
       }
   }
        stage('Build') {
            steps {
                bat 'set'
            }
        }
    }
}