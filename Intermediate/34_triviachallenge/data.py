import requests
import pandas as pd
import html

url = 'https://opentdb.com/api.php?amount=5&type=boolean'
response = requests.get(url)
question_data = pd.DataFrame(response.json()['results'])
question_data['question'] = question_data['question'].apply(html.unescape)
question_data = question_data.to_dict('records')
print(question_data)