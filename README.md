# QAAuto2.0
> Hi! This is a kind of my portfolio of tests written with pytest.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Structure](#structure)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Here you can see a framework for running automation tests with pytest. There is a structured repository configured for different kinds of tests: API, Database, UI.


## Technologies Used
- Python - version 3.11.3
- Pytest - version 7.4.0


## Structure
The repository consists of:
- config folder with config.py file where I can configure the authorization strategy or place token (I don't push it to GitHub for security reasons)
- modules folder which contains some other ones (api, common, ui), where I prepare the class and methods for my tests accordingly
- tests folder contains 3 folders as well (api, database, ui) where the tests are placed
- .gitignore file with info that should be ignored for commit
- become_qa_auto.db - file with some test data for database tests
- chromedriver.exe - this file is necessary for running ui tests
- conftest.py file contains all the fixtures for the tests
- pytest.ini file contains all the marks for the tests


## Usage
To run all the tests from repository navigate to the proper directory (QAAuto2.0) at your machine and use this command

`pytest`

To run all the API tests from repository navigate to the proper directory (QAAuto2.0) at your machine and use this command

`pytest -m api`

To run all the Database tests from repository navigate to the proper directory (QAAuto2.0) at your machine and use this command

`pytest -m database`

To run all the UI tests from repository navigate to the proper directory (QAAuto2.0) at your machine and use this command

`pytest -m ui`

To run the specific test from repository navigate to the proper directory (QAAuto2.0) at your machine and use this command

`pytest -k <keyword>`


## Project Status
The repository is not finished yet, so some new tests will appear here from time to time.


## Acknowledgements
- This project was inspired by "Automation Software Testing by GlobalLogic" course and based on its tasks.


## Contact
Created by [@olhafedak](linkedin.com/in/olha-fedak-7a4aa0206) - feel free to contact me!
