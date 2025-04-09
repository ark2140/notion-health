from flask import Flask, request, jsonify
from notion_client import send_to_notion

app = Flask(__name__)

@app.route('/')
def home():
    return 'Health Notion Webhook is Live!'

@app.route('/post-health-data', methods=['POST'])
def receive_health_data():
    data = request.json
    print("Received data:", data)
    try:
        send_to_notion(data)
        return jsonify({"status": "success", "message": "Data sent to Notion"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)