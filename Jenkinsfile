pipeline {
    agent any

    environment{
        IMG_NAME = PolyBot:${BUILD_NUMBER}
    }

    stages {
        stage('Build docker image') {
            steps {
                    sh '''
                         cd polybot

                         docker build -t PolyBot:$IMG_NAME .
                         docker tag $IMG_NAME tomerp18/$IMG_NAME
                         docker push tomerp18/$IMG_NAME
                    '''

            }
        }
    }
}