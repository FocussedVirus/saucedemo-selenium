# SauceDemo Login Tests

![Selenium Tests](https://github.com/FocussedVirus/saucedemo-selenium/actions/workflows/selenium.yml/badge.svg)

Automated tests for the login page of [SauceDemo](https://www.saucedemo.com), a practice online store.

I built this project to start moving from manual testing to test automation. In my internship I test web applications by hand, and I wanted to learn how to automate that same work.

## What it does

The tests open Chrome, go to the login page, type different usernames and passwords, and check that the page reacts the right way. Each test checks one case.

## What I tested

| Test Case               | Expected result                        |
| ----------------------- | -------------------------------------- |
| Valid user and password | The user enters the store              |
| Locked out user         | An error says the user is locked out   |
| Wrong password          | An error says the data does not match  |
| Empty username          | An error says the username is required |
| Empty password          | An error says the password is required |

## Result

All 5 tests pass. They also run on their own in GitHub Actions every time I push code. The badge at the top shows if the last run passed.

## Tools

Python, Selenium, pytest, Git and GitHub Actions.

## How it is organized

```
pages/
  login_page.py     Page Object for the login page
tests/
  conftest.py       browser setup (fixture)
  test_login.py     login test cases
.github/workflows/
  selenium.yml      pipeline that runs the tests
requirements.txt    project dependencies
.gitignore          files Git should not upload
```

I used the Page Object Model so that the page locators live in one place and the tests are easy to read.

## How to run it

```bash
git clone https://github.com/FocussedVirus/saucedemo-selenium.git
cd saucedemo-selenium
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v
```

## What I learned

- How to write browser tests in Python with Selenium and pytest
- How to find elements in a page with the browser inspector and choose stable locators (`data-test` before `id`, `name` or `class`)
- How the Page Object Model keeps locators and actions in one place
- Why explicit waits are better than fixed sleeps
- How to use pytest fixtures to open and close the browser for each test
- How to run the same test with different data using `parametrize`
- How to run Chrome without a window (headless) so tests work in a pipeline
- How to use a virtual environment and `requirements.txt` to make the project easy to reproduce
- How to use Git and GitHub: add, commits, push and `.gitignore`
- How to set up a basic CI pipeline with GitHub Actions

## Next steps

I am adding tests for products, cart and checkout.

## Author

Sergio Torres Gallardo
