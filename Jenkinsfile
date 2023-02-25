try {
    pipeline()
} catch (e) {
    postFailure(e)
} finally {
    postAlways()
}


def pipeline(){
node{
	    stage("Pull source code from github"){
	        git branch: 'ci_cd_1', url: 'https://github.com/bibiefart/PolyBot.git'
	     }

        stage("Build Docker file"){
	         sh 'docker build -t bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID} .'
	     }

	     stage(" Pushing the image to docker hub " ){
	         withCredentials([string(credentialsId: 'dockerhubpassword', variable: 'dockerhubpassword')]) {
	          sh 'docker login -u bibiefrat -p  ${dockerhubpassword}'
	          sh 'docker push bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID}'
	          }
	    }

    stage(" Deployment of docker container on Docker host"){
            sh 'docker container rm -f bibi_polybot'
            sh 'docker container run -d --name bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID}'
            sh "echo 'do some tests!!!'; sleep 30"
            }
}
}

def postFailure(e) {
    println "Failed because of $e"
    println 'This will run only if failed'

}

def postAlways() {
node{
   sh """
        docker rmi -f bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID}
      """
    }
}
