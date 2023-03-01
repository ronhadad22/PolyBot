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
    
        parameters { choice(choices: ['one', 'two'], description: 'this is just for testing', name: 'testchioce') }

    environment {
        SNYK_TOKEN = credentials('snyk-token')
    }
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')]) {

                  sh "docker build -t ronhad/private-course:poly-bot-${env.BUILD_NUMBER} . "
                  sh "docker login --username $user --password $pass"
                  sh "docker push ronhad/private-course:poly-bot-${env.BUILD_NUMBER}"
 //               sh '''
 //               docker login --username $user --password $pass
 //               docker build ...
 //               docker tag ...
 //               docker push ...
 //          '''
                }
            }
        }
        stage('unit test') {
            steps {                  
                  sh 'python3 -m tests/polytest.py --junitxml results.xml tests'
            }
            post {
                 always {
                     junit allowEmptyResults: true, testResults: 'results.xml'
               }
            }
        }
        stage('Snyk test') {
            steps {
   //             withCredentials([string(credentialsId: 'snyk-token', variable: 'TOKEN')]) {
   //               sh "export SNYK_TOKEN=$TOKEN"
                  
                  //sh "snyk container test  --severity-threshold=high --exclude-vulnerability=SNYK-DEBIAN10-OPENSSL-3314607 ronhad/private-course:poly-bot-${env.BUILD_NUMBER} --file=Dockerfile"
                  sh "snyk container test --ignore-policy ronhad/private-course:poly-bot-${env.BUILD_NUMBER} --file=Dockerfile"
                  
   //             }
            }
        }
        stage('Stage II') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}
