node { 
  stage 'Docker build'
  docker.build('alumni-portal')
 
  stage 'Docker push'
  docker.withRegistry('https://179383330071.dkr.ecr.us-east-2.amazonaws.com', 'ecr:us-east-2:ecr-credentials') {
    docker.image('alumni-portal').push('latest')
  }
}
