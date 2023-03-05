pipeline {
    agent {
        docker {
            image 'https://hub.docker.com/layers/kubealon/private-course/poly-bot-24/images/sha256-5f3f44c18388b836d20787e4e814d48567aec85673dc6c15f546c6570b881015?context=repo'
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
                    credentialsId: 'telegramToken',
                    variable: 'TELEGRAM_TOKEN'
                )
            ]) {
                sh """
                    echo $pass | sudo -S docker build \
                        --build-arg TELEGRAM_TOKEN=$TELEGRAM_TOKEN \
                        -t chessshark1000/private-course:poly-bot-${env.BUILD_NUMBER} .
                """
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-login',
                        passwordVariable: 'DOCKERHUB_PASSWORD',
                        usernameVariable: 'DOCKERHUB_USERNAME'
                    )
                ]) {
                    sh """
                        echo $DOCKERHUB_PASSWORD | sudo -S docker login \
                            --username $DOCKERHUB_USERNAME \
                            --password-stdin
                    """
                    sh """
                        sudo docker push \
                            kubealon/private-course:poly-bot-${env.BUILD_NUMBER}
                    """
                    sh """
                        echo $pass | sudo -S docker push \
                            chessshark1000/private-course:poly-bot-${env.BUILD_NUMBER}
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
        sh 'sudo docker system prune -af'
        }
    }
}
