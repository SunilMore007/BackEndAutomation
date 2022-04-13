# Created by sunil.more at 3/7/2022
Feature: Github API validation
  # Enter feature description here

  Scenario: Session Management check
    Given i have github auth credentials
    When i have getRepo API of github
    Then Status code of response should be 200
