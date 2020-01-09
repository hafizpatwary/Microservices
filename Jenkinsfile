pipeline{
    agent any

    stages{

        stage('Build Dokcer Images'){
            steps{
                sh '''. ~/.bashrc
                        docker-compose build
                        docker-compose push
                        '''
            }
        }

        stage('Deploy Services'){
            steps{
                sh '''ssh jenkins@35.223.251.82 << BOB
                        cd microservices
                        git pull
                        git checkout frontend
                        export BUILD_NUMBER='${BUILD_NUMBER}'
                        docker stack deploy --compose-file docker-compose.yaml microservices
                        '''
            }
        }

        stage('Container Replicas'){
            stpes{
                sh '''ssh jenkins@35.223.251.82 << BOB
                    docker service update --replicas 2 microservices_countries
                    docker service update --replicas 2 microservices_frontend
                    docker service update --replicas 2 microservices_prize
                    docker service update --replicas 2 microservices_temperature
                    '''
            }
        }

    }
}
