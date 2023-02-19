pipeline {
    agent any

    stages {
        stage('Build PolyBot') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_hub_ci_cd_repo', passwordVariable: 'pass', usernameVariable: 'user')]) {

                sh """
                docker login -u $user -p $pass
                docker build -t bibiefrat/ci_cd_1:polybot_bibi .
                docker push bibiefrat/ci_cd_1:polybot_bibi
           """
                }
            }
        }
        stage('Stage II PolyBot') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III PolyBot') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}