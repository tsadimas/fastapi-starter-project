pipeline {
    agent any

    stages {

        stage('Clone') {
            step {
                git branch: 'main', url: 'git@github.com:tsadimas/fastapi-starter-project.git'
            }
        }
        stage('Test') {
            step {
                sh '''
                    cp app/.env.example app/.env
                    docker-compose -d --build
                    docker-compose exec fastapi tavern-ci tests
                '''
            }
        }
    }


}
