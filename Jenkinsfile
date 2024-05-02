pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Welcome to the timetable management system"
            }
        }
        
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install tk'
            }
        }
        
        stage('Run main.py') {
            steps {
                bat 'python main.py'
            }
        }
    }
}
