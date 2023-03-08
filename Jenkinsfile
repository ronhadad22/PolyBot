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
    // parameters { choice(choices: ['one', 'two'], description: 'this is just for testing', name: 'testchioce') }
//snyk container test my-image:latest --file=Dockerfile
    stages {
        stage('Test') {
            steps {
                  sh 'pip3 install -r requirements.txt'
                  sh "python3 -m pytest --junitxml results.xml tests/*.py"
            }
        }
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  sh "docker build -t ronhad/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  sh "docker login --username $user --password $pass"
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
