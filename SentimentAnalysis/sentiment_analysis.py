import requests
import json

def sentiment_analyzer(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Create the payload with the text to be analyzed
    send_text = { "raw_document": { "text": text_to_analyse } }
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = send_text, headers = header)

    # If the response status code is 200, extract the label and score from the response# If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None
    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {"label": label, "score": score}
