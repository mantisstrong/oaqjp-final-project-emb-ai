#import Flask microinfrastructure
from flask import Flask, request, jsonify

#import other needed libraries
import json
import requests

#Instantiate Flask functionality
app = Flask(__name__)

# Create function to access Emotion Predict function of the Watson NLP library and send text to be analyzed
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json = input_json )
    print(response.json())
    # convert JSON string into dictionary
    emotions_data = response.json()
    
    # Extract the emotions dictionary and confirm emotionPredictions came back from Emotion Predict function
    if 'emotionPredictions' in emotions_data and len(emotions_data['emotionPredictions']) > 0:
        emotions = emotions_data['emotionPredictions'][0]['emotion']
        # Function to find the dominant emotion
        print(f"Extracted emotions: {emotions}") #print statement to help debug
        
        #Function to find the dominant emotion
        def get_dominant_emotion(emotions):
            if emotions:
                max_emotion = max(emotions, key=emotions.get)
                
                #append dictionary with max key and value
                emotions['dominant_emotion'] = max_emotion
                                
                #format the dictionary and display
                formatted_response = json.dumps(emotions, indent = 4)
                print(f"Formated resonse: {formatted_response}")
                return max_emotion, emotions

            return None, emotions
        
        dominant_emotion, updated_emotions = get_dominant_emotion(emotions)
        print(f"Dominant Emotion: {dominant_emotion}")  # Debugging: Print dominant emotion
        print(f"Updated Emotions: {updated_emotions}")  # Debugging: Print updated emotions
        return dominant_emotion, updated_emotions
    else:
        print("No emotion data found in the responsere.")
        return None, None

# Create variable to store text to be analyzed
text_to_analyse = "I love this new technology"

# Call the emotion_detector function and pass the result to get_dominant_emotion
# old-emotions_data = emotion_detector(text_to_analyse)
dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
print(f"Dominant Emotion: {dominant_emotion}")
print(f"Updated Emotions: {updated_emotions}")


# Running the app
if __name__ == '__main__':
    app.run(debug=True)



