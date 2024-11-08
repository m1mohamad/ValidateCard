# Credit Card Validator

This is a simple credit card validator application that validates credit card numbers using Luhn's algorithm.

## Prerequisites

- Python 3.9
- Docker

## Setup

1. Clone the repository: 

``` git clone https://github.com/your-username/credit-card-validator.git
cd credit-card-validator```

2. Create a `.secrets` file in the project's root directory and add your credit card number:

```echo "CREDIT_CARD_NUMBER=your_credit_card_number" > .secrets```

3. Create a virtual environment and activate it:

```python -m venv venv
source venv/bin/activate```

4. Install the dependencies:

pip install -r requirements.txt

## Running the Application

1. Set the environment variables:

    ```export $(cat .env | xargs)```

2. Run the application:

    ```python app.py```

3. Access the credit card validation endpoint:

    ```http://localhost:5000/api/validate```

## Running the Pipeline Locally

1. Install `act`:

     ```curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash```

2. Run the pipeline:

    ``` act push --secret-file .secrets --env-file .env ```

## Deploying with Docker

1. Build the Docker image:

    ```docker build -t credit-card-validator . ```

2. Run the Docker container:

    ```docker run -p 5000:5000 --env-file .env --env CREDIT_CARD_NUMBER=your_credit_card_number credit-card-validator```

3. Access the credit card validation endpoint:

    ```http://localhost:5000/api/validate```

## API Endpoint

### Validate Credit Card Number

- **URL**: `/api/validate`
- **Method**: `GET`
- **Description**: Validates the provided credit card number using Luhn's algorithm.
- **Request Parameters**:
- `CREDIT_CARD_NUMBER` (required): The credit card number to validate.
- **Response**:
- `200 OK`: Returns a JSON object indicating whether the credit card number is valid or not.
 ```json
 {
   "isValid": true
 }
 ```
- `400 Bad Request`: Returns an error message if the credit card number is missing or invalid.
 ```json
 {
   "error": "Credit card number must be numeric"
 }
 ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).