pipeline {
    agent any
    stages {
        stage('Build Bot app') {
   steps {
       bat '''
            docker login --username happytoast --password myaccesstoken
            docker push happytoast/build_bot
            docker build .
       '''
   }
}
        stage('Build') {
            steps {
                bat 'set'
            }
        }
    }
}