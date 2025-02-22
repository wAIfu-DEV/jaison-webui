import asyncio
from quart import Quart, request, jsonify

app = Quart(__name__)


@app.route('/', methods=['GET'])
async def run_start():
    with open('webui.html', 'r') as file:
        page = file.read()
    return (page, 200, {'Content-Type': 'text/html', 'Access-Control-Allow-Origin': '*'})

async def main():
    await app.run_task(port=5713, debug=True)

if __name__ == '__main__':
    asyncio.run(main())