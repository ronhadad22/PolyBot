pipeline {
    agent any
     environment {
        MY_GLOBAL_VARIABLE = 'some value'
    }
    stages {
        stage('Build Bot app') {
   steps {
   withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
    // some block
            bat "docker login --username $happytoast --password $myaccesstoken"
            bat "docker build -t build_bot:${BUILD_NUMBER} ."
            bat "docker tag build_bot:${BUILD_NUMBER} happytoast/build_bot:${BUILD_NUMBER}"
            bat "docker push happytoast/build_bot:${BUILD_NUMBER}"
            }
       }//steps
   }//stage
        stage('Build') {
            steps {
                bat 'set'
            }
        }//stage
    }//stages
}