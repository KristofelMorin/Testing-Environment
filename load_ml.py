import pandas as pd
from flask import Response
from flask_restful import Resource
from flask import request, make_response
from users.service import create_user, reset_password_email_send, login_user, reset_password
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

class CreateDairyApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for login user.

        :return: JSON object
        """
        max_words = 10000
        max_len = 100
        input_data = request.get_json()       
        tokenizer = Tokenizer(num_words=max_words)
        X_train = pd.read_csv(r'D:\Testing-Environment\X_train.csv', encoding='latin-1')
        #tokenizer.fit_on_texts(X_train)
        tokenizer.fit_on_texts(X_train)
        texts = [input_data.get('text')]

        # Pra-pemrosesan teks
        processed_texts = tokenizer.texts_to_sequences(texts)
        processed_texts = pad_sequences(processed_texts, maxlen=max_len)

        # Membuat prediksi
        global loaded_model
        predictions = loaded_model.predict(processed_texts)

        # Mengonversi nilai prediksi menjadi label
        labels = ['Non-Depresi' if pred < 0.5 else 'Depresi' for pred in predictions]

        result = {texts:"", predictions: ""}
        # Menampilkan hasil prediksi
        for i, text in enumerate(texts):
            result.text= texts
            result.prediksi= labels[i]
            print(f"Teks: {text}")
            print(f"Prediksi: {labels[i]}")

        response, status = login_user(request, input_data) 
        return make_response(response, status, result)
    