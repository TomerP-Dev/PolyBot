pipeline {
    agent any

    parameters {
        string(name: 'IMAGE_URL', defaultValue: '', description: 'Docker image URL to deploy')
    }

    stages {
        stage('Push docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                        echo "Pushing docker image to DockerHub..."
                        docker login -u %DOCKER_USERNAME% -p %DOCKER_PASS%
                        docker push ${IMAGE_URL}
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    echo "Pushed to DockerHub successfully."
                    echo "Deploying ${IMAGE_URL} to the environment..."
                '''
            }
        }
    }
}
