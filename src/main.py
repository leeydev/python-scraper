#!/usr/bin/env python3
"""
python-scraper - Professional Web Scraper
"""

from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({
        'message': 'python-scraper is running',
        'version': '1.0.0',
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
