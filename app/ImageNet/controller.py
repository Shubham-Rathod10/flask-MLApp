from app.ImageNet.model import ImageDataPredictor
from flask import request, render_template
from PIL import Image
from random import randint
import os

class ImageNetController(object):

    def upload_image(self):
        dir_path = 'app/static/'
        for file in os.listdir(dir_path):
            if 'imgnet' in file:
                os.remove(dir_path + file)
        return render_template('imageNet.html')

    def retrieve_classification(self):
        image = request.files['image']
        ime = Image.open(image)
        ime = ime.convert('RGB')  # greyscale = 'L'
        inp_img_name = f'imgnet-{randint(1, 1000)}.png'
        ime.save('app/static/' + inp_img_name)
        output = ImageDataPredictor('app/static/' + inp_img_name).predict()
        return render_template('imageNetOutput.html', file_in=inp_img_name, img_obj=output[1].upper(), accuracy=int(output[2]*100))