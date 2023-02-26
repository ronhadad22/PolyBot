pipeline {

    options {
        buildDiscarder(logRotator(daysToKeepStr: '1', numToKeepStr: '3'))
        disableConcurrentBuilds()
        timestamps()
        timeout(time: 10, unit: 'MINUTES')
    }

    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }

    agent {
    docker {
        image 'bibiefrat/ci_cd_1:docker-slave'
        args  '-v /var/run/docker.sock:/var/run/docker.sock -u root'
        }
    }
    environment {
    // get the snyk token from the jenkins general credentials
        SNYK_TOKEN = credentials('synk_token')
    }

    stages {
        stage('Build I PolyBot') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_hub_ci_cd_repo', passwordVariable: 'pass', usernameVariable: 'user')]) {
                sh """
                docker login -u $user -p $pass
                docker build -t bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID} .
                docker push bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}
                echo " --------------- testing with snyk ---------------"
                snyk container test bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID} --file=Dockerfile --severity-threshold=high || true
           """
                }
            }
        }
        stage('Stage II PolyBot') {
            steps {
                sh 'echo "stage II..."'
                script {
                    env.IMG_ID=sh(returnStdout: true, script: 'docker images --filter="reference=bibiefrat/ci_cd_1:polybot_bibi*" --quiet').trim()
                    sh "echo --------- image ID: ${IMG_ID} -----"
                    env.CONT_ID=sh(returnStdout: true, script: 'docker run --rm -d ${IMG_ID}').trim()
                    sh "echo 'do some tests!!!'; sleep 5"
                    sh "docker stop ${env.CONT_ID}"
                }

            }
        }
        stage('Stage III PolyBot') {
            steps {
                sh 'echo " --------------- testing with snyk ---------------"'
                sh 'echo echo "stage III..."'
                sh 'snyk container test ubuntu --severity-threshold=high || true'
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