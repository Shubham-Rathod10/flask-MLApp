from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


class ImageDataPredictor(object):
    def __init__(self, image_path):
        self.height = self.width = 224
        self.model = ResNet50(weights='imagenet')
        self.image_path = image_path
        self._process_image()

    def _process_image(self):
        img = image.load_img(self.image_path, target_size=(self.height, self.width))
        img_array = image.img_to_array(img)
        img_res = np.expand_dims(img_array, axis=0)
        self.ready_image_input = preprocess_input(img_res)

    def predict(self, top_possibilities=1):
        predictions = self.model.predict(self.ready_image_input)
        return decode_predictions(predictions, top=top_possibilities)[0][0]

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(ImageDataPredictor('puppy.png').predict())
    t2 = time.time()-t1
    print(t2)
