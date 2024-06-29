pipeline {
    agent any

    parameters {
        string(name: 'IMAGE_URL', defaultValue: '', description: 'Docker image URL to deploy')
    }

    environment {
        // Placeholder for the variable, to be set in the script block
        IMG_NAME = ''
    }

    stages {
        stage('Set Environment Variables') {
            steps {
                script {
                    // Add debug statement to check the value of IMAGE_URL
                    echo "Received IMAGE_URL: ${params.IMAGE_URL}"
                    // Set the IMG_NAME environment variable with the lowercase IMAGE_URL
                    env.IMG_NAME = params.IMAGE_URL.toLowerCase()
                    echo "IMG_NAME set to: ${env.IMG_NAME}"
                }
            }
        }

        stage('Push docker image') {
            steps {
                echo "Pushing docker image: ${env.IMG_NAME}"
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                        echo "Pushing docker image to DockerHub..."
                        docker login -u %DOCKER_USERNAME% -p %DOCKER_PASS%
                        docker push ${env.IMG_NAME}
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    echo "Pushed to DockerHub successfully."
                    echo "Deploying ${env.IMG_NAME} to the environment..."
                """
            }
        }
    }
}
