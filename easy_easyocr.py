#!/usr/bin/env python3

from easyocr import Reader
import argparse
import cv2

# for converting urls to images for opencv
import numpy as np
import urllib

def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV because opencv's putText function can't display
    # non ASCII
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def url_to_image(url):
    # download the image, convert it to a NumPy array,
    # and then read it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--is_url", type=bool, default=False
                help="if image parameter is an url or filepath")
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-l", "--langs", type=str, default="en",
                help="comma separated list of languages to OCR")
ap.add_argument("-g", "--use_gpu", type=bool, default=False,
                help="whether or not GPU should be used")
args = vars(ap.parse_args())

# break the input languages into a comma separated list
languages = args["langs"].split(",")
print("[INFO] OCR'ing with the following languages: {}".format(langs))

# convert url to image object is is_url is True
if args["is_url"]:
    image_ = url_to_image(args["image"])
else:
    image_ = args["image"]

# load the input image from disk
image = cv2.imread(image_)

# OCR the input image using EasyOCR
print("[INFO] OCR'ing input image...")
reader = Reader(languages, gpu=args["use_gpu"])

results = reader.readtext(image)

# Note: Unlike Tesseract, EasyOCR can work with
# OpenCV’s default BGR color channel ordering.
# Therefore, we do not need to swap color channels
# after loading the image.

# loop over the results
for (bbox, text, prob) in results:

    # display the OCR'd text and associated probability
    print("[INFO] {:.4f}: {}".format(prob, text))

    # unpack the bounding box
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))

    # cleanup the text and draw the box surrounding the text along
    # with the OCR'd text itself
    text = cleanup_text(text)
    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
    cv2.putText(image, text, (tl[0], tl[1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
#cv2.destroyAllWindows()
