node {
  stage 'Checkout'
  git 'ssh://https://github.com/swasthi15/Alumni-Portal.git'
 
  stage 'Docker build'
  docker.build('alumni-Portal')
 
  stage 'Docker push'
  docker.withRegistry('https://179383330071.dkr.ecr.us-east-2.amazonaws.com', 'ecr:us-east-2:ecr-credentials') {
    docker.image('alumni-Portal').push('latest')
  }
}