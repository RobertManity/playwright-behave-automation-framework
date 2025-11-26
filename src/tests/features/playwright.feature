#Playwright feature file
Feature: Playwright in web browser

@TC:31167
Scenario: Open Playwright homepage
  Given Ecosia is open in browser
  When user confirms cookie dialog
  And user adds "playwright" search term
  And user clicks on search button
  And user clicks on search result link "https://playwright.dev"
  Then page is shown with url "https://playwright.dev/"

