pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'git@github.com:tsadimas/fastapi-starter-project.git'
            }
        }
        stage('Test') {
            steps {
                sh '''
                    cp app/.env.example app/.env
                    docker-compose down --volumes
                    docker-compose up -d --build
                    docker-compose exec -T fastapi tavern-ci tests
                '''
            }
        }
    }


}
