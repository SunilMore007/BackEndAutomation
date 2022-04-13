# Created by sunil.more at 3/7/2022
Feature: Verify if books are added and deleted using library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API Functionality
    Given The Book details which needs to be added to library
    When We execute the ADDBook PostAPI Method
    Then Book is successfully Added

  @library
  Scenario Outline: Verify AddBook API Functionality
    Given The Book details with <isbn> and <aisle>
    When We execute the ADDBook PostAPI Method
    Then Book is successfully Added
    Examples:
      |isbn  |aisle|
      |eewqedsdwqe      |54354ds3     |
      |ewqeqadsdwewqe      |   5435ds45  |