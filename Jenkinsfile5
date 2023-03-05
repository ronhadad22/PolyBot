pipeline {
    agent none
    stages {
        stage('Run Tests') {
            parallel {
                stage('Test On Windows') {
                    agent any
                    steps {
                        sh "echo 'run-tests.bat'"
                    }

                }
                stage('Test On Linux') {
                    agent any
                    steps {
                        sh "echo 'run-tests.sh'"
                    }

                }
            }
        }
    }
}

