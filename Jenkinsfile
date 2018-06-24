node {
    checkout scm
    //def customImage = docker.build("my-image:${env.BUILD_ID}")
    stage("Build"){
        cd ./Infra
        sh 'docker-compose up -d'
    }

}
