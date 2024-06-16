steps {
  bat 'python -m pylint -f parseable --reports=no *.py > pylint.log'
}
post {
  always {
    bat 'type pylint.log'
    recordIssues (
      enabledForFailure: true,
      aggregatingResults: true,
      tools: [pyLint(name: 'Pylint', pattern: '**/pylint.log')]
    )
  }
}
