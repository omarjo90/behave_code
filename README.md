**QA BDD Automation Test Project**

**Description**

This project is related with the web application functional testing.

The FE section focus on user interface test scenarios, that at the same time,
covers functional testing of the application.

**Technologies Used**

The FE project use the following python packages:

    - Python 3.10.7
    - Behave - Behavior-driven development
    - Allure test report tool
    - Selenium

**How to execute automation projects**

**FE project execution steps**

In order to execute the FE project, the following steps are required:

1. Installation of the required packages previously mentioned

2. Type the following command in terminal: cd ~/path-where-project-lives/ui_project_toptal_demo

3. in the terminal type:

    a. if a report is required use this command:

        behave

    a1. in order to check the report, run this:

        allure serve 

    Previous command will start a session and a web browser opens and shows the html report.

    b. if report is not required use this command:

            behave

5. Wait until the project finishes its execution.
