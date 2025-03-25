# CIS 3500 — Password Validator

This repository contains my completed implementation of the Password Validator assignment for CIS 3500 at the University of Pennsylvania. The goal of this project was to build and deploy a simple password validation API endpoint that verifies whether a given password meets the following criteria:

- **Length:** At least 8 characters  
- **Uppercase:** Contains at least one uppercase letter  
- **Digit:** Contains at least one digit  
- **Special Character:** Contains at least one of the following: `!@#$%^&*`

The endpoint is available at `/v1/checkPassword` and accepts a POST request with a JSON body containing the password. It returns a JSON response with two keys:
- `valid`: a boolean indicating if the password meets the criteria.
- `reason`: a string explaining why the password is invalid (empty if the password is valid).

Additionally, the API always returns an HTTP status code of 200, even when the password does not meet the validation rules.

## Implementation Summary

- **Password Validation:**  
  Implemented in `main.py`, the password validator checks for all the required conditions. Detailed error messages are concatenated and returned in the JSON response if the password is invalid.

- **HTTP Response:**  
  The API endpoint always responds with a 200 status code, ensuring that even when a password fails validation, the response is properly formatted.

- **Testing:**  
  I have added a comprehensive test suite using `pytest` in `test_main.py` to cover:
  - The root endpoint returning the correct greeting.
  - Various password scenarios including valid passwords and different invalid cases (too short, missing uppercase, missing digit, and missing special character).

## Deployment

### Render Deployment

1. **Repository Setup:**  
   I forked/imported the repository into my GitHub account with the name `my-password-validator`.

2. **Render.com:**  
   I created an account on [Render.com](https://www.render.com/), used the "Blueprint" option to deploy from my public Git repository, and confirmed that the initial deployment was successful. The deployed app displays the greeting message:
   
   > Hello from my Password Validator! — `aluk@seas.upenn.edu`

3. **Configuration:**  
   The deployment configuration is stored in `render.yaml`, ensuring that the deployment process is version-controlled and reproducible.

### Local Development

To run the project locally, follow these steps:

1. **Clone the Repository:**  
   Clone the repository to your local machine.

2. **Install Dependencies:**  
   Use `pipenv` to install the required packages:
   ```bash
   pipenv install
   ```

3. **Run the App Locally:**
   Activate the environment and run the server with:
   ```bash
   pipenv run gunicorn main:app --bind 0.0.0.0:1234
   ```
   Visit `http://localhost:1234` to see the greeting message.

## Testing the Endpoint

After deployment (or when running locally), you can test the password validation endpoint:

1. **Browser Test:**  
   Visit your deployed URL (or `http://localhost:1234`) to confirm the greeting is displayed.

2. **API Test:**  
   Send a POST request to `/v1/checkPassword` with a JSON payload. For example:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"password":"Abcdef1!"}' \
        https://your-deployed-app-url/v1/checkPassword
   ```
   A valid password returns:
   ```json
   {"valid": true, "reason": ""}
   ```
   Invalid passwords will return a reason message indicating the failed validations.

## Test Suite

The project includes a test suite (`test_main.py`) built with `pytest` that verifies:
- The root endpoint is functioning.
- The `/v1/checkPassword` endpoint validates passwords correctly, providing detailed error messages when the password does not meet one or more criteria.

To run the tests, simply execute:
```bash
pipenv run pytest
```

## Credits

This project was completed for CIS 3500 — Software Design/Engineering with Professor Lumbroso at the University of Pennsylvania.
Feel free to reach out if you have any questions or suggestions.
