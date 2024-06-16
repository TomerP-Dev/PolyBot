pipeline {
    agent any

    environment {
        IMG_NAME = "polybot:${BUILD_NUMBER}"
    }

    stages {
        stage('Build docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                        echo Current directory:
                        dir
                        echo Polybot directory:
                        dir polybot
                        docker login -u %DOCKER_USERNAME% -p %DOCKER_PASS%
                        docker build -t %IMG_NAME% .
                        docker tag %IMG_NAME% tomerp18/%IMG_NAME%
                        docker push tomerp18/%IMG_NAME%
                    '''
                }
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'IMAGE_URL', value: "tomerp18/${IMG_NAME}")
                ]
            }
        }
    }
}
