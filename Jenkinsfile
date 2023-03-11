pipeline {
    agent { 
        docker {
            image 'kubealon/private-course:jenkins-agent'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
 
    environment{
        SNYK_TOKEN = credentials('snyk_token')
    }
    options {
        skipDefaultCheckout(true)
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        disableConcurrentBuilds()
    }

    stages {
    stage('Build') {
    options {
                timeout(time: 10, unit: 'MINUTES')
            }
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: 'github-login',
                     passwordVariable: 'pass',
                    usernameVariable: 'user'
                ),
                string(
                    credentialsId: 'telegram-token',
                    variable: 'TELEGRAM_TOKEN'
                )
            ]) {
                sh """
                    echo $pass | docker build \
                        --build-arg TELEGRAM_TOKEN=$TELEGRAM_TOKEN \
                        -t kubealon/private-course:poly-bot-${env.BUILD_NUMBER} .
                """
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-login',
                        passwordVariable: 'DOCKERHUB_PASSWORD',
                        usernameVariable: 'DOCKERHUB_USERNAME'
                    )
                ]) {
                    sh """
                        echo $DOCKERHUB_PASSWORD | docker login \
                            --username $DOCKERHUB_USERNAME \
                            --password-stdin
                    """
                    sh """
                        docker push \
                            kubealon/private-course:poly-bot-${env.BUILD_NUMBER}
                    """
                    sh """
                        echo $pass |docker push \
                            kubealon/private-course:poly-bot-${env.BUILD_NUMBER}
                    """
                }
            }
        }
    }

     stage('snyk test') {
            steps {
                sh "echo $SNYK_TOKEN"

                sh " snyk ignore --id=SNYK-DEBIAN11-CURL-3320493"
                sh "snyk container test --severity-threshold=critical  --exclude-base-image-vulns kubealon/private-course:poly-bot-${env.BUILD_NUMBER} --file=Dockerfile"
                
            }
        }
       
    stage('Stage III ...') {
        steps {
            sh 'echo "stage III..."'
            sh 'echo "hello world"'
        }
    }
}
post {
    always {
        // Cleanup Docker images from the disk
        sh 'docker system prune -af'
        }
    }
}
