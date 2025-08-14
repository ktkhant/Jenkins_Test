pipeline {
    agent any
    triggers {
        githubPush()  // Triggered by GitHub webhook
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ktkhant/Jenkins_Test', branch: 'main'
            }
        }
        stage('Check for app.py Changes') {
            steps {
                script {
                    def changes = bat(script: "git diff --name-only HEAD HEAD~1", returnStdout: true).trim()
                    if (changes.contains("app.py")) {
                        echo "app.py has changed. Proceeding with build..."
                    } else {
                        echo "No changes in app.py. Skipping build."
                        currentBuild.result = 'SUCCESS'
                        // Exit early
                        return
                    }
                }
            }
        }
        stage('Run app.py') {
            when {
                expression {
                    // Only run if app.py changed
                    def changes = bat(script: "git diff --name-only HEAD HEAD~1", returnStdout: true).trim()
                    return changes.contains("app.py")
                }
            }
            steps {
                bat 'python app.py'
            }
        }
    }
}
