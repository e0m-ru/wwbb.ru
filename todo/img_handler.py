#!/usr/bin/env python3
from PIL import Image
import os
from .models import Project
from random import choice
from djsite.settings import BASE_DIR, MEDIA_ROOT
PHOTO_PATH = f"{os.path.join(MEDIA_ROOT,'photos')}"


def collect_album(id):
    album_lst = os.listdir(os.path.join(PHOTO_PATH,str(id)))
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


def img_handler(instance, id, s):
    db_Obj = Project.objects.get(id=id)
    img_name = f'{s}_{id}'
    album_dir = os.path.join(PHOTO_PATH, str(id))
    img_path = f'{album_dir}/{img_name}'

    with open(img_path+'.jpg', 'wb+') as destination:
        for chunk in instance.chunks():
            destination.write(chunk)

    outfile = img_path + ".thumbnail"
    with Image.open(img_path+'.jpg') as im:
        im = crop_center(im)
        im = im.resize((256,256))
        im.save(outfile, "JPEG", optimize=True, quality=80)
    db_Obj.album = db_Obj.album + '\n' + f'/media/photo/{id}' + img_name