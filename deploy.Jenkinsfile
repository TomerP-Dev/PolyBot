pipeline {
    agent any

    parameters {
        string(name: 'IMAGE_URL', defaultValue: '', description: 'Docker image URL')
    }

    stages {
        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                        docker login -u %DOCKER_USERNAME% -p %DOCKER_PASS%
                        docker push ${IMAGE_URL}
                        echo "Pushed ${IMAGE_URL} to DockerHub successfully."
                    '''
                }
            }
        }
    }
}
