from flask import Flask, abort, jsonify
import aiohttp
from bs4 import BeautifulSoup

app = Flask(__name__)

async def get_stock_data():
    url = "https://www.infomoney.com.br/cotacoes/b3/acao/vale-vale3/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            tables = soup.find_all('div', class_='tables')

            data = {}
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) == 2:
                        key = columns[0].text.strip()
                        value = columns[1].text.strip()
                        data[key] = value

            return data

@app.route('/api/v1/stock_data', methods=['GET'])
async def stock_data():
    try:
        stock_data = await get_stock_data()
        if not stock_data:
            abort(404)
        return jsonify(stock_data), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
