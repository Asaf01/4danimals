from flask import Flask, render_template
import requests

app = Flask(__name__)


endpoint_url = 'https://4danimals.com/wp-json/wp/v2/posts/'

@app.route('/')
def get_posts():
    try:
       
        response = requests.get(endpoint_url)
        
   
        if response.status_code == 200:
          
            json_data = response.json()
          
            return render_template('posts.html', posts=json_data)
        else:
         
            return render_template('error.html', error_message='Error: ' + str(response.status_code))
    except Exception as e:
    
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
