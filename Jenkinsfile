pipeline {
  environment {
    registry = "swasthishekhar/project"
    registryCredential = 'dockerhub'
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
         script {
            docker.withRegistry('https://179383330071.dkr.ecr.us-east-2.amazonaws.com', 'ecr:us-east-2:ecr-credentials') {
    		docker.image('alumni-portal').push('latest')
        }
    }
}
}
}
}

