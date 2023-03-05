pipeline {

    options{
    buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '5', numToKeepStr: '10'))
    disableConcurrentBuilds()
        
   }
    agent{
     docker {
        image 'jenkins-agent:latest'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
    }
    environment{
        SNYK_TOKEN = credentials('snyk-token')
    }
    parameters { choice(choices: ['one', 'two'], description: 'this is just for testing', name: 'testchioce') }
//snyk container test my-image:latest --file=Dockerfile
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  //sh "docker build -t ronhad/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  //sh "docker login --username $user --password $pass"
                  sh 'echo unitest'
 //               sh '''
 //               docker login --username $user --password $pass
 //               docker build ...
 //               docker tag ...
 //               docker push ...
 //          '''
                }
            }
        }
        stage('snyk test') {
            steps {
                sh "snyk container test --severity-threshold=critical ronhad/private-course:poly-bot-${env.BUILD_NUMBER} --file=Dockerfile"
            }
        }
        stage('push') {
            steps {
                    sh "docker push ronhad/private-course:poly-bot-${env.BUILD_NUMBER}"
            }

        }
        
    }
}
