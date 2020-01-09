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
                        export JENKINS_IP='$(curl ifcongig.me)'
                        #docker service update --image ${JENKINS_IP}:5000/countries_service:${BUILD_NUMBER} microservices_countries
                        docker service update --image 35.228.228.71:5000/countries_service:${BUILD_NUMBER} microservices_countries
                        '''
            }
        }

    }
}
