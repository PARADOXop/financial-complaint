from flask import Flask, render_template, request, jsonify
from src.Exception import CustomException
from src.logger import logging
import os
import sys
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    try:
        logging.info("checking if flask works or not")
        print('hanji bhaiya ji')
        return 'hello xd '
    except Exception as e:
        raise CustomException(e,sys) 

if __name__ == "__main__":
    app.run()