# UI and API Automated Testing Demonstration with Pytest and Selenium

## Overview
This project demonstrates UI and API automated testing using Python and Selenium WebDriver. Selenium is a powerful tool for automating web browsers and is widely used for testing web applications.

## Application Under Test
The following application is used for demonstrating automation of both UI and API</br>
Link: [Test Application](https://thinking-tester-contact-list.herokuapp.com/)
## Requirements
- Python 3.x
- Selenium WebDriver (Install using `pip install selenium`)
- Pytest (Install using `pip install pytest`)
- pytest-html (Install using `pip install pytest-html`)
- Requests (Install using `pip install requests`)
- Web Browser (Chrome)
- Webdriver executable for the chosen browser (ChromeDriver)
- PyCharm as an IDE

## Setup
1. Install Python 3.x from the [official Python website](https://www.python.org/downloads/).
2. Download the appropriate version of Chrome webdriver executable for your browser and place it in the drivers folder of project directory.
3. Clone this repository to your local machine.

## Running Tests
1. Navigate to the project directory.
2. Install the dependencies using command `pip install -r requirements.txt`. The file requirements.txt is available in project repository.
3. Execute tests using command `pytest --html=report.html`
4. report.html file shall be generated in project directory

## Project Structure

- `tests/`: Contains test classes.
- `src/pages/`: Contains page object classes.
- `src/utils/`: Contains locators and api related data like endpoints etc
- `src/common/`: Contains common web element functions
- `src/api_func`: Contains API methods
- `resources`: Contains application details like URL, Username, password etc
- `drivers`: Executable driver for Chrome should be added

## Tests Covered

### UI Tests
Script: `/tests/test_ui.py`
1. Valid and Invalid login
2. Create, Read, Delete of Contact (The contact which is created is deleted too through script)

### API Tests
Script: `/tests/test_api.py`
1. Valid and Invalid Login - Post Methods
2. User Data Validation - Valid and Invalid scenario - Get Method
