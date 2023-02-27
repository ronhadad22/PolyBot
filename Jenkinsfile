pipeline {
    agent any
     environment {
        MY_GLOBAL_VARIABLE = 'some value'
    }
    options {
    buildDiscarder(logRotator(daysToKeepStr: '30'))
    disableConcurrentBuilds()
    timestamps()
        timeout(time: 10, unit: 'MINUTES')
}
    stages {
        stage('Build Bot app') {
   steps {
   withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
    // some block
    script {
            bat "docker login --username $happytoast --password $myaccesstoken"
            bat "def timestamp = new Date().format('yyyyMMddHHmmss')"
            bat "docker build -t build_bot:${timestamp} ."
            bat "docker tag build_bot:${timestamp} happytoast/build_bot:${timestamp}"
            bat "docker push happytoast/build_bot:${timestamp}"
            }//script
           }
       }//steps
   }//stage
        stage('Build') {
            steps {
                bat 'set'
            }
        }//stage
    }//stages
 post {
        always {
        script {
            bat "def timestamp = new Date().format('yyyyMMddHHmmss')"
            bat "docker rmi build_bot:${timestamp}"
            bat "docker rmi happytoast/build_bot:${timestamp}"
            }//script
        }
    }
}