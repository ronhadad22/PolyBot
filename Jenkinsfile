node{
	    stage("Pull source code from github"){
	        git branch: 'ci_cd_1', url: 'https://github.com/bibiefart/PolyBot.git'
	     }
	    stage("Build Docker file"){
	         sh 'docker image build bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID} .'
	     }
	    stage(" Pushing the image to docker hub " ){
	         withCredentials([string(credentialsId: 'docker_hub_ci_cd_repo', variable: 'docker_hub_ci_cd_repo')]) {
	          sh 'docker login -u bibiefrat -p  ${dockerhubpassword}'
	          sh 'docker image push bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}'
	          }
	    }
	    stage(" Deployment of docker container on Docker host"){
	    def dockerrm  = 'docker container rm -f bibi_polybot'
	    def dockerrun = 'docker container run -d --name bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}'
	    sh "echo 'do some tests!!!'; sleep 30"
	    def docker_image = ' docker image rmi -f bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}'	    

	}

}


