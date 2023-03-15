pipeline {
agent {
    docker {
        image 'jenkins/agent:latest'
        args  '--user root -v "//./pipe/docker_engine:/var/run/docker.sock"'
    }
}
     environment {
        MY_GLOBAL_VARIABLE = 'some value'
        timestamp = '%date:~10,4%%date:~4,2%%date:~7,2%%time:~0,2%%time:~3,2%%time:~6,2%'
    }
    options {
    buildDiscarder(logRotator(daysToKeepStr: '3'))
    disableConcurrentBuilds()
    timestamps()
        timeout(time: 10, unit: 'MINUTES')
}
    stages {
        stage('Build Bot app') {
   steps {
   withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
    // some block
            sh docker login --username $happytoast --password $myaccesstoken
            sh docker build -t build_bot:${BUILD_NUMBER} .
            sh docker tag build_bot:${BUILD_NUMBER} happytoast/build_bot:${BUILD_NUMBER}
            sh docker push happytoast/build_bot:${BUILD_NUMBER}
           }
       }//steps
   }//stage
    }//stages
 post {
        always {
            sh docker rmi happytoast/build_bot:${BUILD_NUMBER}
        }
    }
}