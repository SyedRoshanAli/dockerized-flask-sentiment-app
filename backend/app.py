from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['text']

    # Perform sentiment analysis
    analysis = TextBlob(feedback)
    polarity = analysis.sentiment.polarity  # Ranges from -1 to 1
    subjectivity = analysis.sentiment.subjectivity  # Ranges from 0 to 1

    # Determine sentiment category
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Pass all data to results.html
    return render_template(
        'results.html',
        name=name,
        email=email,
        feedback=feedback,
        sentiment=sentiment,
        polarity=round(polarity, 2),
        subjectivity=round(subjectivity, 2)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
