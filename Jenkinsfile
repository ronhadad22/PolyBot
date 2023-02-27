pipeline {
    agent any
     environment {
        MY_GLOBAL_VARIABLE = 'some value'
        timestamp = '%date:~10,4%%date:~4,2%%date:~7,2%%time:~0,2%%time:~3'
    }
    options {
    buildDiscarder(logRotator(daysToKeepStr: '7'))
    disableConcurrentBuilds()
    timestamps()
        timeout(time: 10, unit: 'MINUTES')
}
    stages {
        stage('Build Bot app') {
   steps {
   withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
    // some block
            bat "docker login --username $happytoast --password $myaccesstoken"
            bat "docker build -t build_bot:${timestamp} ."
            bat "docker tag build_bot:${timestamp} happytoast/build_bot:${timestamp}"
            bat "docker push happytoast/build_bot:${timestamp}"
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
            bat "docker rmi happytoast/build_bot:${timestamp}"
        }
    }
}