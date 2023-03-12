pipeline {
    
   agent {
    docker {
        image 'jenkins-agent:latest'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
stage('Build Bot app') {
   steps {
       sh withCredentials([usernamePassword(credentialsId: '526a2c3a-6054-4f78-9f99-105a66f35790', passwordVariable: 'password', usernameVariable: 'username')]) {
    // some block
       sh "docker build -t avijwdocker/polybot-aviyaaqov-${env.BUILD_NUMBER}. "
       sh "docker login --username $user --password $pass"
       sh "docker push avijwdocker/polybot-aviyaaqov-${env.BUILD_NUMBER}"
       }
     }
   }
}
