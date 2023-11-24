from flask import Flask, render_template
from app import application
# from app.static.library import predict_linreg


@application.route('/')
def index():
    hdi = 0.747  # You should replace this with actual input from user or form data
    population = 325123600  # You should replace this with actual input from user or form data
    # predicted_result = predict_linreg(hdi, population)
    # return render_template('index.html', predicted_result=predicted_result, title='Pandemic Food Security Predictor')
    return render_template('index.html', title='Pandemic Food Security Predictor')
