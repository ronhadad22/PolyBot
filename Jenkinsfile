pipeline {
    agent { 
        docker {
            image 'kubealon/private-course:jenkins-agent'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
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
                        credentialsId: 'dockerhub-login',
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
                        sudo docker push \
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

    stage('Stage II') {
        steps {
            sh 'echo "stage II..."'
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

