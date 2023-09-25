pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'python3 ops.py'
            }
        }
        stage('Testing file') {
            steps {
                sh "python3 -m pytest"
            }
        }
        stage('Deliver') {
            steps {
                script {
                    def pytestOutput = sh(script: "python3 -m pytest", returnStdout: true, returnStatus: true)
                    if (pytestOutput == 0) {
                        echo "Pytest passed"
                        echo "Pytest output: ${pytestOutput}"
                    } else {
                        echo "Pytest failed"
                        echo "Pytest output: ${pytestOutput}"
                    }
                }
            }
        } 
    }
}