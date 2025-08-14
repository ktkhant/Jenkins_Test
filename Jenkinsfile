pipeline {
    agent any
    triggers {
        githubPush()  // Triggered by GitHub webhook
    }
    environment {
        VENV_DIR = 'venv'
        PYTHON_PATH = 'python' // Adjust if needed, e.g., 'python3.9'
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
                        return
                    }
                }
            }
        }

        stage('Setup Virtualenv and Install Dependencies') {
            when {
                expression {
                    def changes = bat(script: "git diff --name-only HEAD HEAD~1", returnStdout: true).trim()
                    return changes.contains("app.py")
                }
            }
            steps {
                bat """
                    ${PYTHON_PATH} -m venv ${VENV_DIR}
                    call ${VENV_DIR}\\Scripts\\activate.bat
                    pip install --upgrade pip
                    if exist requirements.txt pip install -r requirements.txt
                """
            }
        }

        stage('Run app.py') {
            when {
                expression {
                    def changes = bat(script: "git diff --name-only HEAD HEAD~1", returnStdout: true).trim()
                    return changes.contains("app.py")
                }
            }
            steps {
                bat """
                    call ${VENV_DIR}\\Scripts\\activate.bat
                    ${PYTHON_PATH} app.py
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "rmdir /s /q ${VENV_DIR}"
        }
    }
}
