node{
	    stage("Pull source code from github"){
	        git branch: 'ci_cd_1', url: 'https://github.com/bibiefart/PolyBot.git'
	     }

        stage("Build Docker file"){
	         sh 'docker build -t bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID} .'
	     }

	     stage(" Pushing the image to docker hub " ){
	         withCredentials([string(credentialsId: 'docker_hub_ci_cd_repo',  passwordVariable: 'pass', usernameVariable: 'user')]) {
	          sh 'docker login -u ${user} -p  ${pass}'
	          sh 'docker image push bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID}'
	          }
	    }

}


