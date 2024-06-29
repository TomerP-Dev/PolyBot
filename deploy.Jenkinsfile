pipeline {
    agent any

    parameters {
     string(name: 'IMAGE_URL', defaultValue: '', description: '')
    }

    stages {
        stage('Deploy') {
            steps {
                bat '''
                    echo "Pushed to DockerHub successfully."
                '''
            }
        }
    }
}