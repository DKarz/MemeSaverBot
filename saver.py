import cloudinary
import os
from cloudinary import uploader
import time
import requests
import wget

cloudinary.config(
  cloud_name = 'dulaytxwk',
  api_key = '615329492513682',
  api_secret = 'BaeXljb9_mR0TmczXqlmC_v1li8',
  force_version = False
)




def upload(files, folder):
    for fi in files:
        cloudinary.uploader.upload(fi, folder = folder, resource_type="raw", public_id=fi[:len(fi) - fi[::-1].find(".") - 1], invalidate=True)
    return


def download(files):
    output = []
    for fi in files:
        link = cloudinary.utils.cloudinary_url(fi, resource_type = "raw")[0]
        output.append(link)
        continue
        try: os.unlink(fi)
        except: pass
        wget.download(link)
    return output


    
