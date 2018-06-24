pipeline{
    agent any
    stages{
      stage("Remove old"){
        steps{
            script {
            try {
                sh 'docker rm -f python-app mysql-server; docker rmi python-con_python python-con_mysql; docker volume rm `docker volume ls | awk \'{print $2}\'`; docker network rm python-con_infra_net'
            } catch (err) {
                echo err
            }
           }
      }
        stage('Build'){
            steps{
                echo "Start"
                sh 'docker-compose up -d'

            }
        }
    }
}
