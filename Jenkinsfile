pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo building...'
            }
        }
        stages('Stage II') {
               steps {
                   sh 'echo "stage II..."'
               }
           }
               stage('Stage III ...')  {
                   steps {
                       sh 'echo echo "stage III..."'
                   }
               }
           }
       }
