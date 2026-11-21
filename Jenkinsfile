pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest -v --junitxml=pytest-results.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true,
                          testResults: 'pytest-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t aceest-fitness-ci:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Run Pytest Inside Docker') {
            steps {
                sh '''
                    docker run --rm \
                    -v "$WORKSPACE:/results" \
                    aceest-fitness-ci:${BUILD_NUMBER} \
                    sh -c "python -m pytest -v --junitxml=/results/pytest-docker-results.xml"
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true,
                          testResults: 'pytest-docker-results.xml'
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'app.py,test_app.py,requirements.txt,Dockerfile,Jenkinsfile,pytest-results.xml,pytest-docker-results.xml',
                                 allowEmptyArchive: true,
                                 fingerprint: true
            }
        }
    }
}
