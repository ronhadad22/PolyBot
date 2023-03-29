pipeline {
    agent {
        docker {
            image 'jenkins-agent:latest'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        MY_GLOBAL_VARIABLE = 'some value'
        timestamp = sh(script: 'date "+%Y%m%d%H%M%S"', returnStdout: true).trim()
        SNYK_TOKEN = credentials('SnykToken')
        TELEGRAM_TOKEN = credentials('telegramToken')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        disableConcurrentBuilds()
        timestamps()
        timeout(time: 10, unit: 'MINUTES')
    }
    stages {
            stage('Installations') {
            steps {
                sh "apt-get update && apt-get install -y python3"
                sh "apt-get install -y python3-pip"
                sh "pip3 install pytest"
                sh "pip3 install pylint"
                sh "pip3 install -r requirements.txt"
            }
        }
    stage('Tests') {
    parallel {
    stage('PylintTest') {
                    steps {
                            sh "python3 -m pylint --exit-zero -f parseable --reports=no *.py > pylint.log"
                    }
                    }
    stage('PolyTest') {
            steps {
                withCredentials([string(credentialsId: 'telegramToken', variable: 'TELEGRAM_TOKEN')]) {
                sh "touch .telegramToken"
                sh "echo ${TELEGRAM_TOKEN} > .telegramToken"
                sh "python3 -m pytest --junitxml results.xml tests/polytest.py"
                }
            }
        }
        }
        }
    stage('Build Bot App') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerTokenID', passwordVariable: 'myaccesstoken', usernameVariable: 'happytoast')]) {
                    sh "docker login --username $happytoast --password $myaccesstoken"
                    sh "docker build -t build_bot:${BUILD_NUMBER} ."
                    sh "docker tag build_bot:${BUILD_NUMBER} happytoast/build_bot:${BUILD_NUMBER}"
                }
            }
        }
        stage('Snyk Test') {
            steps {
                withCredentials([string(credentialsId: 'SnykToken', variable: 'SNYK_TOKEN')]) {
                    sh "snyk container test --severity-threshold=critical build_bot:${BUILD_NUMBER} --file=Dockerfile --token=${SNYK_TOKEN} --exclude-base-image-vulns"
                }
            }
        }
        stage('Push Bot App') {
            steps {
                sh "docker push happytoast/build_bot:${BUILD_NUMBER}"
            }
        }
    }
    post {
        always {
            sh "docker rmi happytoast/build_bot:${BUILD_NUMBER}"
            junit allowEmptyResults: true, testResults: 'results.xml'
            sh 'cat pylint.log'
    recordIssues (
      enabledForFailure: true,
      aggregatingResults: true,
      tools: [pyLint(name: 'Pylint', pattern: '**/pylint.log')]
    )
        }
    }
}