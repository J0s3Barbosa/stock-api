# Stock Data API

Welcome to the Stock Data API! This API allows you to retrieve real-time stock data for a specific stock from the Brazilian stock market (B3).

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Features

- Retrieves real-time stock data from the B3 stock market.
- Provides data such as closing price, opening price, trading volume, and more.
- Follows best REST API practices for easy integration.

## Getting Started

### Installation

To use the Awesome Stock Data API, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/J0s3Barbosa/stock-api.git
   cd stock-api
   ```

2. Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Access the API endpoint in your web browser or using a tool like cURL:

   ```
   http://127.0.0.1:5000/api/v1/stock_data
   ```

## API Reference

### GET /api/v1/stock_data

Retrieves real-time stock data for a specific stock from the B3 stock market.

#### Response

The response is a JSON object containing various data points such as:

- "Fechamento anterior": Previous closing price.
- "Abertura": Opening price.
- "Negócios": Number of transactions.
- "Volume": Trading volume.
- "Mín — Máx (Dia)": Day's low and high prices.
- "Variação (Dia)": Day's percentage change.
- "Variação (Mês)": Month's percentage change.
- "Variação (2024)": Year's percentage change.
- "Variação (52 semanas)": Percentage change over the last 52 weeks.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository:** Click on the "Fork" button at the top right corner of the repository page on GitHub. This will create a copy of the repository in your GitHub account.

2. **Clone the repository:** Clone the forked repository to your local machine using the following command:

3. **Create a new branch:** Create a new branch for your feature or bug fix using the following command:

4. **Make your changes:** Make your desired changes to the codebase.

5. **Commit your changes:** After making changes, commit them with a descriptive commit message using the following command:

6. **Push to the branch:** Push your changes to your forked repository on GitHub using the following command:

7. **Create a new pull request:** Finally, navigate to the original repository on GitHub and click on the "New pull request" button. Compare the changes you made in your branch with the original repository's master branch and create the pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.







