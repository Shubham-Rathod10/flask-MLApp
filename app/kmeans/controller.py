from random import randint

from flask import render_template, request
from PIL import Image
from app.kmeans.models import KMeansAlgo
import os


#@app.route('/kmeans/output', methods=['GET', 'POST'])
def _algo():
    # req_image = request.form
    # message = 'Please find your uploaded file here :'
    image = request.files['image']
    ime = Image.open(image)
    ime = ime.convert('RGB').resize((500, 500))  # greyscale = 'L'
    inp_img_name = f'input-{randint(1, 1000)}.png'
    ime.save('app/static/'+inp_img_name)
    file_out = KMeansAlgo().kmeansalgo(ime)
    return render_template('output.html', file_in = inp_img_name, file_out = file_out)

#@app.route('/')
def home():
    return render_template('home1.html')

#@app.route('/kmeans')
def kmeans():
    """ This function is used to take the input image. """
    dir_path = 'app/static/'
    for file in os.listdir(dir_path):
        if 'input' or 'output' in file:
            os.remove(dir_path+file)
    return render_template('kmeans.html', message=None)

#@app.route('/kmeans/file', methods=['GET', 'POST'])
# def kmeansfile():
#     message = 'Please find your uploaded file here :'
#     image = request.files['image']
#     ime = Image.open(image)
#     ime = ime.convert('RGB').resize((500, 500))  # greyscale = 'L'
#     inp_img_name = f'input-{randint(1, 1000)}.png'
#     ime.save('app/static/'+inp_img_name)
#     return render_template('kmeans.html', message=message, img=inp_img_name)