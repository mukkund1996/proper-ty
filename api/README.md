# PROPER-ty Flask API

This Flask API, called PROPER-ty, allows you to retrieve information about properties across the US. It uses a SQLite database to store the property data.

## Installation

To install and run the PROPER-ty Flask API, follow these steps:

1. Clone the repository:

  ```shell
  git clone https://github.com/mukkund1996/proper-ty.git
  ```

2. Navigate to the project directory:

  ```shell
  cd proper-ty
  ```

3. Create a Python virtual environment:

  ```shell
  python3 -m venv venv
  ```

4. Activate the virtual environment:

  - For macOS/Linux:

    ```shell
    source venv/bin/activate
    ```

  - For Windows (PowerShell):

    ```shell
    .\venv\Scripts\Activate.ps1
    ```

5. Install the required dependencies:

  ```shell
  pip install -r requirements.txt
  ```

6. Run the Flask API:

  ```shell
  flask run
  ```

  The API will be accessible at `http://localhost:5000`.

## Usage

View the API docs using Swagger at `http://localhost:8000/api/ui`.

### Quick start

To use the PROPER-ty Flask API, you can make HTTP requests to the available endpoints. Here are some examples:

- Retrieve all properties:

  ```http
  GET /properties
  ```

- Retrieve a specific property by ID:

  ```http
  GET /properties/{id}
  ```

- Delete a property:

  ```http
  DELETE /properties/{id}
  ```

For more details on the available endpoints and their usage, please refer to the API documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for more information.