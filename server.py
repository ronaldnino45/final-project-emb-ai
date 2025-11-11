"""
Flask web server for Emotion Detection.

This module defines a simple web application that analyzes emotions in text
using an external NLP API. It provides a main route for emotion detection
and a root route for rendering the index page.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotions in the given text.

    Retrieves text from the HTTP GET request, calls the emotion detection
    function, and returns either the detected emotions or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
    f"For the given statement, the system response: {response}. "
    f"The dominant emotion is {dominant_emotion}"
    )

@app.route("/")

def render_index_page():
    """
    Render the main index page of the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
