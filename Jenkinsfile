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

//         stage('Code Checkout') {
//                 steps {
//                     checkout([
//                         $class: 'GitSCM',
//                         branches: [[name: '*/main']],
//                         userRemoteConfigs: [[url: 'https://github.com/spring-projects/spring-petclinic.git']]
//                     ])
//                 }
//             }


        stage('Build I PolyBot') {
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

        stage('Stage II PolyBot - testing with snyk plybot image') {
            steps {
                script {
                        //def data = "SNYK-DEBIAN11-AOM-1300249\nSNYK-DEBIAN11-AOM-1298721\nSNYK-DEBIAN11-TIFF-3113871"
                        //filename = env.WORKSPACE + "/snyk.txt";
                        //writeFile(file: filename, text: data)
                        sh 'echo "SNYK-DEBIAN11-AOM-1300249\nSNYK-DEBIAN11-AOM-1298721\nSNYK-DEBIAN11-TIFF-3113871" > snyk.txt'
                        sh "cat snyk.txt"
                        //sh "snyk auth $SNYK_TOKEN ; snyk ignore --id=\\'SNYK-DEBIAN11-AOM-1298721\\'"
                        sh 'while IFS= read -r line; do snyk auth $SNYK_TOKEN  ; snyk ignore --id=\\\'$line\\\'; done < snyk.txt'
                        def date = new Date()
                        def data = "Hello World\nSecond line\n" + date
                        writeFile(file: 'zorg.txt', text: data)
                        def data2 = "NYK-DEBIAN11-AOM-1300249\nSNYK-DEBIAN11-AOM-1298721\nSNYK-DEBIAN11-TIFF-3113871"
                        writeFile(file: 'snyk2.txt.txt', text: data2)
                        sh "ls -l"
                }
                sh """
                echo " --------------- testing with snyk ---------------"
                snyk container test bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID} --file=Dockerfile --severity-threshold=high || true
                """
            }
        }


        stage('Stage III PolyBot - run container') {
            steps {
                sh 'echo "Running ploybot container"'
                script {
                    //env.IMG_ID=sh(returnStdout: true, script: 'docker images --filter="reference=bibiefrat/ci_cd_1:polybot_bibi*" --quiet').trim()
                    //sh "echo --------- image ID: ${IMG_ID} -----"
                    env.CONT_ID=sh(returnStdout: true, script: 'docker run --rm --name bibi_polybot_container -d  bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID}').trim()
                }

            }
        }
        stage('Stage IV PolyBot - testing UBUNTU with snyk') {
            steps {
                sh 'echo " --------------- testing with snyk ---------------"'
                sh 'echo echo "stage III..."'
                sh 'snyk container test ubuntu --severity-threshold=high || true'
            }
        }

        stage('Stage V PolyBot - UniTests') {
            steps {
                 script {
                        sh "echo 'do some tests!!!'; sleep 2"
                        //def ret = sh script: 'docker exec ${env.CONT_ID} pytest -v  polytest.py', returnStdout: true
                        def ret=sh(returnStdout: true, script: 'docker exec bibi_polybot_container pytest -v  polytest.py').trim()
                        println ret
                       }
             }
        }


        stage('Stage VI PolyBot - stop container') {
            steps {
                    sh "docker stop ${env.CONT_ID}"
                   }
        }


    }
    post {
        always {
            sh """
            echo "removing container"
            docker rmi -f bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}
            """
        }
    }
}