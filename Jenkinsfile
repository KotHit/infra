pipeline{
    agent any
    stages{
	stage('Compose Down'){
	    steps{
		echo "Close old services"
		sh 'docker-compose down'	
	    }
	}
        stage('MySQL'){
            steps{
                echo "Run MySQL"
                sh 'docker-compose up -d mysql'

            }
        }
	stage('Python'){
            steps{
                echo "Run Python"
                sh 'docker-compose up -d python'
		echo "Python logs"
		sh 'docker logs python-app'
            }
        }
    }
}
