import unittest
from unittest.mock import patch
import json
from emotion_detection import emotion_detector  # Replace 'your_module' with the actual module name

class TestEmotionDetector(unittest.TestCase):
    
    @patch('emotion_detection.requests.post')  # Mock the requests.post method
    def test_emotion_detector_success_joy(self, mock_post):
        #Mock test for "I love this new technology" expected dominant value of joy, using actual Watson Predict Emotion function results
        mock_response_data = {
            "emotionPredictions": [
                {
                    'emotion': {
                        'anger': 0.01388365,
                        'disgust': 0.00850114,
                        'fear': 0.018487887,
                        'joy': 0.83237535,
                        'sadness': 0.17257097}
                }
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Call the function
        text_to_analyse = "I love this new technology"
        dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
        
        # Check if the function returns the correct emotions dictionary
        self.assertEqual(dominant_emotion, 'joy')
        self.assertIn('dominant_emotion', updated_emotions)
        self.assertEqual(updated_emotions['dominant_emotion'], 'joy')

    
    @patch('emotion_detection.requests.post')  # Mock the requests.post method
    def test_emotion_detector_success_anger(self, mock_post):
        #Mock test for "I am really mad about this" expected dominant value of anger, using actual Watson Predict Emotion function results
        mock_response_data = {
            "emotionPredictions": [
                {
                    'emotion': {
                        'anger': 0.6674731,
                        'disgust': 0.022848725,
                        'fear': 0.09749009,
                        'joy': 0.011863918,
                        'sadness': 0.1953058}
                }
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Call the function
        text_to_analyse = "I am really mad about this"
        dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
        
        # Check if the function returns the correct emotions dictionary
        self.assertEqual(dominant_emotion, 'anger')
        self.assertIn('dominant_emotion', updated_emotions)
        self.assertEqual(updated_emotions['dominant_emotion'], 'anger')
        
       
    @patch('emotion_detection.requests.post')  # Mock the requests.post method
    def test_emotion_detector_success_disgust(self, mock_post):
        #Mock test for "I feel disgusted just hearing about this" expected dominant value of anger, using actual Watson Predict Emotion function results
        mock_response_data = {
            "emotionPredictions": [
                {
                    'emotion': {
                        'anger': 0.11452735,
                        'disgust': 0.9193782,
                        'fear': 0.055274334,
                        'joy': 0.00233425,
                        'sadness': 0.06884794}
                }
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Call the function
        text_to_analyse = "I feel disgusted just hearing about this"
        dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
        
        # Check if the function returns the correct emotions dictionary
        self.assertEqual(dominant_emotion, 'disgust')
        self.assertIn('dominant_emotion', updated_emotions)
        self.assertEqual(updated_emotions['dominant_emotion'], 'disgust')

    @patch('emotion_detection.requests.post')  # Mock the requests.post method
    def test_emotion_detector_success_sadness(self, mock_post):
        #Mock test for "I am so sad about this" expected dominant value of anger, using actual Watson Predict Emotion function results
        mock_response_data = {
            "emotionPredictions": [
                {
                    'emotion': {
                        'anger': 0.0063314,
                        'disgust': 0.005223638,
                        'fear': 0.074054584,
                        'joy': 0.004095184,
                        'sadness': 0.9819713}
                }
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Call the function
        text_to_analyse = "I am so sad about this"
        dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
        
        # Check if the function returns the correct emotions dictionary
        self.assertEqual(dominant_emotion, 'sadness')
        self.assertIn('dominant_emotion', updated_emotions)
        self.assertEqual(updated_emotions['dominant_emotion'], 'sadness')

    @patch('emotion_detection.requests.post')  # Mock the requests.post method
    def test_emotion_detector_success_fear(self, mock_post):
        #Mock test for "I am really afraid that this will happen" expected dominant value of anger, using actual Watson Predict Emotion function results
        mock_response_data = {
            "emotionPredictions": [
                {
                    'emotion': {
                        'anger': 0.0068210675,
                        'disgust': 0.00360616,
                        'fear': 0.9907291,
                        'joy': 0.0057615982,
                        'sadness': 0.073330835}
                }
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
        
        # Call the function
        text_to_analyse = "I am afraid that this will happen"
        dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
        
        # Check if the function returns the correct emotions dictionary
        self.assertEqual(dominant_emotion, 'fear')
        self.assertIn('dominant_emotion', updated_emotions)
        self.assertEqual(updated_emotions['dominant_emotion'], 'fear')

    
    @patch('emotion_detection.requests.post')  # Mock the requests.post method
    def test_emotion_detector_failed(self, mock_post):
        #Mock test for "I love this new technology" expected dominant value of joy, using actual Watson Predict Emotion function results
        mock_response_data = {
            "emotionPredictions": [
                {
                    'emotion': {
                        'anger': 0.01388365,
                        'disgust': 0.00850114,
                        'fear': 0.018487887,
                        'joy': 0.83237535,
                        'sadness': 0.17257097}
                    }
                ]
            }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response_data
            
        # Call the function
        text_to_analyse = "I love this new technology"
        dominant_emotion, updated_emotions = emotion_detector(text_to_analyse)
            
        # Check if the function returns the correct emotions dictionary
        self.assertNotEqual(dominant_emotion, 'fear')
        self.assertIn('dominant_emotion', updated_emotions)
        self.assertNotEqual(updated_emotions['dominant_emotion'], 'fear')
        

if __name__ == '__main__':
    unittest.main()