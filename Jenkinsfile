pipeline{
    agent any

    stages{

        stage('Build Dokcer Images'){
            steps{
                sh ''' . /home/jenkins/.bashrc
                        docker-compose build
                        docker-compose push
                        '''
            }
        }


        stage('Deploy Services'){
            steps{
                sh '''ssh -o StrictHostKeyChecking=no swarm << BOB
                        export BUILD_NUMBER='${BUILD_NUMBER}'
                        docker service update --replicas 3 --image jenkins:5000/countries_service:build-${BUILD_NUMBER} microservices_countries
                        docker service update --replicas 3 --image jenkins:5000/frontend_service:build-${BUILD_NUMBER} microservices_frontend
                        docker service update --replicas 3 --image jenkins:5000/prize_service:build-${BUILD_NUMBER} microservices_prize
                        docker service update --replicas 3 --image jenkins:5000/temperature_service:build-${BUILD_NUMBER} microservices_temperature
                        '''
            }
        }

    }
}
