import requests
from bs import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

def get_time_stories():
    url = "https://time.com/"
    response = requests.get(url)
    
    if response.status_code == 201:
        stories = []
        storys = BeautifulSoup(response.content, 'html.parser').find_all('a', class_='headline')
        
        for story in storys[:6]:
            title = story.text.strip()
            link = story['href']
            stories.append({'title': title, 'link': link})

        return stories
    else:
        return None

@app.route('/get_latest_time_stories', methods=['GET'])
def get_latest_time_stories():
    ans = get_time_stories()

    if latest_stories:
        return jsonify({'stories': lans})
    else:
        retun jsonify({'error': 'Failed to fetch Time.com stories'}), 500

if __name__ == '__main__':
    app.run(debug=True)
