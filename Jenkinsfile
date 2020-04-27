pipeline {
  environment {
    registry = "swasthishekhar/project"
    registryCredential = 'dockerhub'
    customimage = "${registry}" + ':' + "$BUILD_NUMBER"
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          docker.build customimage
        }
      }
    }
    stage('Deploy Image') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            docker.image(customimage).push("$BUILD_NUMBER")
        }
    }
}
}
}
}
