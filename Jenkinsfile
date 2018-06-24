node {
    checkout scm
    //def customImage = docker.build("my-image:${env.BUILD_ID}")
    stages("Build"){
        cd ./infra
        sh 'docker-compose up -d'
    }

}
