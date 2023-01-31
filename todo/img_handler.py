#!/usr/bin/env python3
from PIL import Image
import os
from random import choice
from djsite.settings import BASE_DIR, MEDIA_ROOT

PHOTO_PATH = os.path.join(MEDIA_ROOT, 'photos/')

def img_handler(instance, prj_id, s):
    prj_id = str(prj_id)
    album_path = os.path.join(PHOTO_PATH, prj_id)    
    img_path = os.path.join(album_path, f'{prj_id}_{str(s)}')    

    with open(rf'{img_path}.jpg', 'wb+') as destination:
        for chunk in instance.chunks():
            destination.write(chunk)

    outfile = img_path + ".thumbnail"
    with Image.open(rf'{img_path}.jpg') as im:
        im = crop_center(im)
        im = im.resize((256,256))
        im.save(outfile, "JPEG", optimize=True, quality=80)


def collect_album(prj_id):
    prj_id = str(prj_id)
    album_lst = os.listdir(os.path.join(PHOTO_PATH, prj_id))
    album_lst = set(map(lambda x: os.path.splitext(x)[0], album_lst))
    return album_lst


def insert_thumbnail(db_Obj):
    for i in db_Obj:
        album = list(collect_album(i.id))
        i.thumbnail = f'/media/photos/{i.id}/' + choice(album) + '.thumbnail'
    return db_Obj


def crop_center(pil_img):
    img_width, img_height = pil_img.size
    if img_width > img_height:
        crop_factor = img_height
    else:
        crop_factor = img_width

    return pil_img.crop(((img_width - crop_factor) // 2,
                         (img_height - crop_factor) // 2,
                         (img_width + crop_factor) // 2,
                         (img_height + crop_factor) // 2)).resize((256, 256))