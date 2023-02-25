node{
	    stage("Pull source code from github"){
	        git branch: 'ci_cd_1', url: 'https://github.com/bibiefart/PolyBot.git'
	     }

        stage("Build Docker file"){
	         sh 'docker image build bibiefrat/ci_cd_1:polybot_bibi_${env.BUILD_ID} .'
	     }
}


