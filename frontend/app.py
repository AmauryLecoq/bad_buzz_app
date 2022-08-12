import pandas as pd
import streamlit as st
import requests


def request_prediction(model_uri, data):
    headers = {"Content-Type": "application/json"}

    data_json = {'tweet': data}
    response = requests.request(
                method='POST',
                headers=headers,
                url=model_uri,
                json=data_json)

    if response.status_code != 200:
                raise Exception("Request failed with status \
                    {}, {}\
                        ".format(response.status_code, 
                        response.text))

    return response.json()


def main():
    APP_URI = 'http://fastapi:8000/predict'

    st.title('Prediction des sentiments tweet')

    tweet = st.text_input('Tweet à analyser')


    predict_btn = st.button('Prédire')
    if predict_btn:
                data = tweet
                pred = request_prediction(APP_URI, data)
                st.write(pred)


if __name__ == '__main__':
    main()
