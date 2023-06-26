import time

import pandas as pd
import requests

KEY = 'jBEK1sIZyl9AZG2tQvSit0XRYtZ9IhxB'
SECRET = 'DOvAfScJUgZPxEqR'


# Fetch some date from the endpoint
def get_request(query: str, start_date: str, end_date: str):
    params = {'api-key': KEY, 'begin_date': start_date, 'end_date': end_date, 'q': query}
    response = requests.get(url="https://api.nytimes.com/svc/search/v2/articlesearch.json", params=params)
    response.raise_for_status()  # Raises HTTPError, if one occurred.
    data = response.json()['response']['docs']
    time.sleep(5)
    return data, response


def process_record(data):
    record_info = {'headline': [], 'abstract': [], 'URL': [], 'source': [], 'publication_date': [], 'document_type': []}
    for record in data:
        if 'headline' in record and 'main' in record['headline']:
            record_info['abstract'].append(record['abstract'])
            record_info['headline'].append(record['headline']['main'])
            record_info['URL'].append(record['web_url'])
            record_info['source'].append(record['source'])
            record_info['publication_date'].append(record['pub_date'])
            record_info['document_type'].append(record['document_type'])
        else:
            continue
    df = pd.DataFrame(record_info)
    df.drop_duplicates('abstract', inplace=True)

    return df

start_date = '18880101'
end_date = '18881231'
query='Brazil'

data, response = get_request(query=query, start_date=start_date, end_date=end_date)
data_processed = process_record(data)
print(data_processed.head())