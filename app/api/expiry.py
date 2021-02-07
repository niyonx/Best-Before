from google.cloud import vision
import os

# import dateparser
# from dateparser.search import search_dates

import datefinder

from PIL import Image

# set path to api key here
""" INPUT PATH TO JSON API KEY"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"

def detect_text(img):
    """Detects text in the file."""

    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    # Uncomment below if path given instead of image

    # with io.open(img, 'rb') as image_file:
    #     img = image_file.read()

    image = vision.Image(content=img)

    response = client.text_detection(image=image)
    text = response.text_annotations[0].description

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return text

def replace_MM_to_Full(text):
    months_expiry = {
      "JA" : "January",
      "FE" : "February",
      "MR": "March",
      "AL": "April",
      "MA": "May",
      "JN": "June",
      "JL": "July",
      "AU": "August",
      "SE": "September",
      "OC": "October",
      "NO": "November",
      "DE": "December"
    }

    for word, initial in months_expiry.items():
        text = text.replace(word, initial)

    return text

def find_expiry_date(img):

    text = detect_text(img)

    text = replace_MM_to_Full(text)

    try:
        expiry_date = next(datefinder.find_dates(text)).strftime("%m-%d-%Y")
    except:
        return False

    return expiry_date

# print(find_expiry_date("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225640.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225652.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225703.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225750.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225759.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225824.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225846.jpg"))
# print(detect_text("/home/niyon/Workspace/ExpireNoMore/app/images/expiry/IMG_20210205_225945.jpg"))

# REGEX = (?:\d{2}(?:\d{2})?(?: *)[\/:\-,_.]?(?: *))?\d{2}(?: *)[\/:\-,_.]?(?: *)\d{2}(?:\d{2})?

# string_with_dates = '''
#     2021 MR04
# BZ21008 Y

# 0044598AA
# B.B./M.A.2021 MA 13

# BEST BEFORE HEILLEUR AVANT
# 2021 MA 28

# 2021JL31
# K4 20:06
# BEST BEFORE/MEILLEUR AVANT

# TOSRLSA3120235
# REST BEFORE
# 2021 00 31
# NEILLEUR AVANT

# BB/MA 2021 OC 18 B

# 2021 AL14
# 16:10 M17

# 606) 05 MR
# '''

# string_with_dates = '''
#     2021 MR04
# BZ21008 Y

# 0044598AA
# B.B./M.A.2021 MA 13

# BEST BEFORE HEILLEUR AVANT
# 2021 MA 28
# '''

# string_with_dates = '''
#     2021 March04
# BZ21008 Y
# '''




# months_expiry = {
#   "JA" : "January",
#   "FE" : "February",
#   "MR": "March",
#   "AL": "April",
#   "MA": "May",
#   "JN": "June",
#   "JL": "July",
#   "AU": "August",
#   "SE": "September",
#   "OC": "October",
#   "NO": "November",
#   "DE": "December"
# }

# address = "123 north anywhere street"

# for word, initial in months_expiry.items():
#     string_with_dates = string_with_dates.replace(word, initial)

# print(string_with_dates)

# matches = datefinder.find_dates(string_with_dates)
# for match in matches:
#     print(match.strftime("%m-%d-%Y"))

# dates = search_dates(string_with_dates)
# print(dates)
