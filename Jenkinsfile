pipeline {
    agent any
    stages {
        stage ('bake') {
            steps {
                build job: 'bake'
            }
        }

        stage ('launch') {
            steps {
                build job: 'launch'
            }
        }
    }
}
