node{
	    stage("Pull source code from github"){
	        git branch: 'ci_cd_1', url: 'https://github.com/bibiefart/PolyBot.git'
	     }

        stage("Build Docker file"){
	         sh 'docker build bibiefrat/ci_cd_1:polybot_bibi_${BUILD_ID} .'
	     }
}


