from pyzbar import pyzbar
import cv2
import numpy as np

import requests

BARCODE_API_KEY = '5qfx4t6ihhsk9k52ohtpss2xqtcdtt'

def read_image_path_barcode(path):
  # image = cv2.imread(path)
  image = cv2.imread('/home/niyon/Desktop/PolyHx/mayo.jpg')
  barcodes = pyzbar.decode(image)
  for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    barcodeData = barcode.data.decode('utf-8')
    barcodeType = barcode.type
    text = "{} ( {} )".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

    print("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))

    return barcodeData

def read_image_barcode(img):
  img = np.array(img)
  barcodes = pyzbar.decode(img)

  for barcode in barcodes:
      (x, y, w, h) = barcode.rect
      cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

      barcodeData = barcode.data.decode('utf-8')
      barcodeType = barcode.type
      text = "{} ( {} )".format(barcodeData, barcodeType)

      print("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))

      return barcodeData

def get_product_info(barcode_id):
  search_url = 'https://api.barcodelookup.com/v2/products'

  search_params = {
      'key': BARCODE_API_KEY,
      'formatted': 'y',
      'barcode': barcode_id
  }

  request_search = requests.get(search_url, params=search_params)

  result = request_search.json()

  product_info = {
                'product_name': result['products'][0]['product_name'],
                'manufacturer': result['products'][0]['manufacturer'], 
                'brand': result['products'][0]['brand'],
                'image_url': result['products'][0]['images'][0]
            }

  return product_info

# barcode_id = read_image_path_barcode('/home/niyon/Desktop/PolyHx/mayo.jpg')
# print(get_product_info(barcode_id))