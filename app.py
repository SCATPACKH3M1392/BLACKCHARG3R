from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "Missing URL.", 400

    try:
        # Fetch the requested URL's content
        response = requests.get(url)
        return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
