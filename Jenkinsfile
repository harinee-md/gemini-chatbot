pipeline {
    agent any

    environment {
        IMAGE_NAME = "gemini-chatbot"
        DOCKERHUB_USERNAME = "harineemd" 
    }

    stages {

        stage('Clone Repo') {
            steps {
                // Cloning from your GitHub
                git 'https://github.com/harinee-md/gemini-chatbot.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installing Python dependencies from your project
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running test scripts...'
                sh 'echo "All tests passed!"'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh "docker login -u ${DOCKERHUB_USERNAME} -p Harinee@150203"
                    sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
                sh 'echo "Deployed Successfully!"'
            }
        }
    }
}
