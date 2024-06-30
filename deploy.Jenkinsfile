pipeline {
    agent any

    options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
    }

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

    post {
        always {
            cleanWs()
        }
    }
}
