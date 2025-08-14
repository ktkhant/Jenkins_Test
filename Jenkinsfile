pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/ktkhant/Jenkins_Test.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }

    post {
	 success { 
		echo "pipeline done"
	 }
	 failure {
		echo "pipeline failed"
	}
	
	}
}
