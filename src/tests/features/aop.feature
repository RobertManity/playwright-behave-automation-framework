Feature: AoP feature file

@TC:31166
Scenario:AoP is open and navigatable
    Given AoP is open
    When user clicks on "HOME" button
    Then page has url  "https://localhost:5003/en-US/home"
    When user clicks on "RUNS" button
    Then page has url  "https://localhost:5003/en-US/run-control"
    When user clicks on "MAINTENANCE" button
    Then page has url  "https://localhost:5003/en-US/maintenance"
    When user clicks on "PROTOCOLS" button
    Then page has url  "https://localhost:5003/en-US/protocols/dashboard"


@TC:31177
Scenario: Verify that Home button is visible
    Given AoP is open
    Then HOME is visible
    Then RUNS is visible
    Then MAINTENANCE is visible
    Then PROTOCOLS is visible

@TC:86796
Scenario: The system displays current date and time in the correct format
    Given AoP is open
    When the user looks at the top header section of the application
    Then the current date and time should be visible
    And the format should match "DD-MMM-YY HH:MM"
    And the month abbreviation should start with a capital letter
    Then current date and time matches local system
    

@TC:31199
Scenario: Verify Hamilton logo is correctly displayed
    Given AoP is open
    Then Hamilton logo is visible
    #And Hamilton logo has correct size and source



@TC:31200
Scenario Outline: AoP header is changing depending on which sub menu user choose
    Given AoP is open
    When user clicks on "<menu_item>" button
    Then page header is "<header_text>"

    Examples:
    | menu_item   | header_text  |
    | HOME        | Home         |
    | RUNS        | Runs         |
    | MAINTENANCE | Maintenance  |
    | PROTOCOLS   | Protocols    |


@TC:31201
Scenario: Verify Protocols screen and NEW PROTOCOL button is visible
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    Then button "NEW PROTOCOL" is visible


@TC:31202
Scenario: New Protocol wizard tabs are visible
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    And user clicks on "NEW PROTOCOL" button
    Then wizard step "Choose Template" is visible
    And wizard step "Choose Flask" is visible
    And wizard step "Adjust Parameters" is visible
    And wizard step "Save Protocol" is visible

@TC:31203
Scenario: Verifies if NEXT button is clickable when no Protocole is chosen
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    Then button "NEW PROTOCOL" is visible
    When user clicks on "NEW PROTOCOL" button
    Then wizard step "Choose Template" is visible
    #When user clicks on "NEXT" button
    Then "NEXT" button is disabled
    And "CANCEL" button is enabled
    When user clicks on "CANCEL" button
    Then button "NEW PROTOCOL" is visible

@TC:31204
Scenario: Verifies that when user press on droping menu he is able to choose one of the options
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    Then button "NEW PROTOCOL" is visible
    When user clicks on "NEW PROTOCOL" button
    Then wizard title "Choose Template" is visible

@TC:86827
Scenario: Verify Protocols column headers are visible
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    And Protocols page is opened
    Then NEW PROTOCOL button is visible
    Then Protocols table headers are visible
    Then no protocols message is shown

@TC:13112
Scenario: Verify Existing coloumns on "NEW PROTOCOL" page are visible
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    And Protocols page is opened
    When user clicks on "NEW PROTOCOL" button
    Then wizard step "Choose Template" is visible
    Then Template column header is visible
    And Cells column header is visible

@TC:2112
Scenario: Verify Protocol name
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    And Protocols page is opened
    When user clicks on "NEW PROTOCOL" button
    Then protocol name "Passaging 2" is visible    

@TC:90916
Scenario: UI displays the correct number of protocol templates on the first page
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    When user clicks on "NEW PROTOCOL" button
    Then wizard step "Choose Template" is visible
    Then Template column header is visible
    And protocol templates list is visible
    And protocol templates list displays 5 items
    Then protocol name "Passaging 2" is visible

@TC:86828
Scenario: User press on next page button
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    When user clicks on "NEW PROTOCOL" button
    Then protocol name "Passaging 2" is visible
    When user navigates to the next page of protocol templates
    Then protocol name "Cell Migration Assay" is visible
    #Then protocol templates list displays 3 items
    When user navigates to the first page of protocol templates
    Then protocol name "Passaging 1" is visible
    #Then protocol templates list displays 5 items
    When user navigates to the last page of protocol templates
    Then protocol name "Cell Migration Assay" is visible
    When user navigates to the first page of protocol templates
    Then protocol name "Passaging 2" is visible

@TC:86866
Scenario: Wizard step states after moving to Choose Flask
    Given AoP is open
    When user clicks on "PROTOCOLS" button
    And user clicks on "NEW PROTOCOL" button
    Then wizard step "Choose Template" is active
    And wizard step "Choose Flask" is inactive
    And wizard step "Adjust Parameters" is inactive
    When user selects protocol template "Passaging 1"
    And user clicks on "NEXT" button
    Then wizard step "Choose Template" is completed
    And wizard step "Choose Flask" is active
    And wizard step "Adjust Parameters" is inactive
    And wizard header displays selected protocol "Passaging 1"
    And flask selection labels are visible and correct

    