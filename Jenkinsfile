pipeline {
    agent any

    stages {
        stage('Build PolyBot') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_hub_ci_cd_repo', passwordVariable: 'pass', usernameVariable: 'user')]) {

                sh """

                docker login -u $user -p $pass
                docker build -t bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID} .
                docker push bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}
           """
                }
            }
        }
        stage('Stage II PolyBot') {
            steps {
                sh 'echo "stage II..."'
                script {
                    env.IMG_ID=sh(returnStdout: true, script: 'docker images --filter="reference=bibiefrat/ci_cd_1" --quiet').trim()
                    sh "docker run --rm -it ${env.IMG_ID} sleep 10"
                }

            }
        }
        stage('Stage III PolyBot') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
    post {
        always {
            sh """
            docker rmi -f bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}
            """
        }
    }
}