pipeline {
    agent any

    stages {
        stage('clone') {
            steps {
               sh '''
                    echo 'Clone'
               '''
            }
        }
        stage('test') {
            steps {
                sh '''
                    cp app/.env.example app/.env
                    docker-compose down --volumes
                    docker-compose up -d --build
                    python3 -m venv favenv
                    source favenv/bin/activate
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }
         stage('docker build and push') {
            environment {
                DOCKER_TOKEN = credentials('docker-push-secret')
                DOCKER_USER = 'tsadimas'
                DOCKER_SERVER = 'ghcr.io'
                DOCKER_PREFIX = 'ghcr.io/tsadimas/pms8-fastapi'
            }

            steps {
                sh '''
                    HEAD_COMMIT=$(git rev-parse --short HEAD)
                    TAG=$HEAD_COMMIT-$BUILD_ID
                    docker build --rm -t $DOCKER_PREFIX:$TAG -t $DOCKER_PREFIX:latest -f fastapi.Dockerfile .  
                '''

                
                sh '''
                    echo $DOCKER_TOKEN | docker login $DOCKER_SERVER -u $DOCKER_USER --password-stdin
                    docker push ghcr.io/tsadimas/myfastapi --all-tags
                '''
            }
        
        }
    }

}