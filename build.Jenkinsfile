pipeline {
    agent any

    environment {
        IMG_NAME = "tomerp18/polybot:${BUILD_NUMBER}"
    }

    stages {
        stage('Build docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                        docker login -u %DOCKER_USERNAME% -p %DOCKER_PASS%
                        docker build -t %IMG_NAME% .
                        docker tag %IMG_NAME% tomerp18/polybot:%BUILD_NUMBER%
                    """
                    bat "echo Built image name: %IMG_NAME%"
                }
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'IMAGE_URL', value: "tomerp18/polybot:${BUILD_NUMBER}")
                ]
            }
        }
    }
}
