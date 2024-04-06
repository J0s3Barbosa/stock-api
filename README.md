# stock-api
stock-api

# Create a virtual environment (optional but recommended)
python -m venv env

-  Activate the virtual environment
-  On Windows
env\Scripts\activate

- upgrade pip
py -m pip install --upgrade pip

- Install the required packages
pip install -r requirements.txt

# Usage

- Run the Flask application:
python main.py

- Access the API endpoint in your web browser or using a tool like cURL:
http://127.0.0.1:5000/api/v1/stock_data

- response

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