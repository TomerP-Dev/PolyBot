pipeline {
    agent any

    environment{
        IMG_NAME = "PolyBot:${BUILD_NUMBER}"
    }

    stages {
        stage('Build docker image') {
            steps {
                sh '''
                    # Build the Docker image using the Dockerfile in the current directory
                    docker build -t PolyBot:$IMG_NAME .

                    # Tag the image for pushing to the registry
                    docker tag $IMG_NAME tomerp18/$IMG_NAME

                    # Push the image to the specified registry
                    docker push tomerp18/$IMG_NAME
                '''
            }
        }
    }
}