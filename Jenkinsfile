pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/utkarshamahajan27/jenkins-automation.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m venv $VIRTUAL_ENV'
                sh 'source $VIRTUAL_ENV/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'source $VIRTUAL_ENV/bin/activate && pytest tests/'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'nohup python app.py &'
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed"
        }
    }
}
