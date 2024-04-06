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

To use the Stock Data API, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/J0s3Barbosa/stock-api.git
   cd stock-api
   ```

2. Install the required Python packages:
   
   ```bash
      pip install -r requirements.txt
   ```

   2.1 Create a virtual environment (optional but recommended)
   ```bash

      python -m venv env

   -  Activate the virtual environment
   -  On Windows
      env\Scripts\activate

   - upgrade pip
      py -m pip install --upgrade pip

   - Install the required packages
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

{
  "Abertura": "60,28",
  "Ativo Total": "R$ 455,98 B",
  "D\u00edvida Bruta": "R$ 67,4 B",
  "D\u00edvida L\u00edquida": "R$ 49,68 B",
  "Ebitda": "R$ 86 B",
  "Fechamento anterior": "60,37",
  "Lucro L\u00edquido (LL)": "R$ 40,55 B",
  "Margem Ebitda": "41.33%",
  "Margem L\u00edquida": "19.48%",
  "M\u00edn \u2014 M\u00e1x (Dia)": "59,61 - \n                                    60,48",
  "Neg\u00f3cios": "39.589,00",
  "Patrim\u00f4nio L\u00edquido (PL)": "R$ 198,32 B",
  "Receita L\u00edquida": "R$ 208,06 B",
  "Retorno sobre o Capital (ROIC)": "+17.55%",
  "Retorno sobre o PL (ROE)": "+20.44%",
  "Varia\u00e7\u00e3o (2024)": "-19.19%",
  "Varia\u00e7\u00e3o (52 semanas)": "-14.2%",
  "Varia\u00e7\u00e3o (Dia)": "-1.09%",
  "Varia\u00e7\u00e3o (M\u00eas)": "-1.84%",
  "Volume": "$ 918,34 M",
  "\u00cdndice de pre\u00e7o sobre lucro (P/L)": "6,40"
}

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







