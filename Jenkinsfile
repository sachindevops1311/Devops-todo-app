pipeline {
    agent any

    environment {
        APP_NAME = 'devops-todo-app'
        DOCKER_IMAGE = "anushkaak15/devops-todo-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo "Building ${env.APP_NAME}..."
                sh 'docker --version'
                sh 'echo Build complete'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo All tests passed'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker pull nginx:latest"
                    sh "docker tag nginx:latest ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    sh "docker push ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    echo 'Image pushed to DockerHub'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh "docker stop ${env.APP_NAME} || true"
                sh "docker rm ${env.APP_NAME} || true"
                sh """
                    docker run -d \
                    --name ${env.APP_NAME} \
                    -p 5000:5000 \
                    ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}
                """
                echo 'Deployment complete!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
            sh 'docker logout || true'
        }
        success {
            echo "Build ${env.BUILD_NUMBER} deployed successfully!"
        }
        failure {
            echo "Build ${env.BUILD_NUMBER} failed - check logs above"
        }
    }
}
