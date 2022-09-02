import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np 
import pandas as pd

app=flask(__name__)
model=pickle.load(open(''))


