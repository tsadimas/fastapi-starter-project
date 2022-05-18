pipeline {
    agent any
    environment {
            DOCKER_TOKEN = credentials('docker-push-secret')
            DOCKER_USER = 'tsadimas'
            DOCKER_SERVER = 'ghcr.io'
            DOCKER_PREFIX = 'ghcr.io/tsadimas/pms8-fastapi'
        }
        
    parameters {
            string(name: 'HEAD_COMMIT', defaultValue: '')
            string(name: 'TAG', defaultValue: '')            
        }


    stages {

        stage('create vars') {
            steps {
                sh '''
                    head_commit =  sh (script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    env.HEAD_COMMIT = head_commit
                    tag =  sh (script: '$HEAD_COMMIT-$BUILD_ID', returnStdout: true).trim()
                    env.TAG = tag
                '''
            }
        }
        
        stage('test') {
            steps {
                sh '''
                    cp app/.env.example app/.env
                    docker-compose kill -s SIGINT
                    docker-compose up -d --build
                    python3 -m venv favenv
                    source favenv/bin/activate
                    pip install -r requirements.txt
                    pytest
                    docker-compose down --volumes
                '''
            }
        }
         stage('docker build and push') {
           

            steps {
                sh '''
                  
                    docker build --rm -t $DOCKER_PREFIX:$TAG -t $DOCKER_PREFIX:latest -f fastapi.Dockerfile .  
                '''

                
                sh '''
                    echo $DOCKER_TOKEN | docker login $DOCKER_SERVER -u $DOCKER_USER --password-stdin
                    docker push $DOCKER_PREFIX --all-tags
                '''
            }
         }

            stage('deploy to k8s') {
            steps {
                sh '''
                 
                    kubectl config use-context microk8s
                    kubectl set image deployment/fastapi-deployment fastapi=$DOCKER_PREFIX:$TAG

                '''
            }
        }
        
    }

}