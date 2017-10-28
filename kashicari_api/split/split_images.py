import cv2
import numpy as np
import base64

def convert_b_image(b):
    buf = base64.b64decode(b)
    with open("imageToSave.png", "wb") as fh:
        fh.write(buf)
    #img = np.frombuffer(buf, dtype=np.uint8)
    #img = cv2.imdecode(img, 1)
    img = cv2.imread('imageToSave.png')
    return img

def find_crowd_h(array, threshold, step):
    (i, j) = array.shape
    split_bool = np.zeros(j, dtype=bool)
    split_index = np.arange(j)
    for k in range(j):
        l = min(k+step, j)
        if np.sum(array[:, k:l]) < threshold:
            split_bool[k:l] = 1

    return  split_index[split_bool]

def find_crowd_v(array, threshold, step):
    (i, j) = array.shape
    split_bool = np.zeros(i, dtype=bool)
    split_index = np.arange(i)
    for k in range(i):
        l = min(k+step, i)
        if np.sum(array[k:l, :]) < threshold:
            split_bool[k:l] = 1
    return  split_index[split_bool]

def del_trash(crowd, axes):
    crowds = []
    for c in crowd:
        if c.shape[axes] > 2:
            crowds.append(c)
    return crowds

def split_object(byte):
    img = convert_b_image(byte)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (i, j) = gray_img.shape
    threshold = int(0.02 * (i + j))
    step = int(0.01 * (i + j))
    canny = cv2.Canny(gray_img, 20, 110)/255
    split_index_h = find_crowd_h(canny, threshold, step)
    crowd_h = np.hsplit(canny, split_index_h)
    crowd_h = del_trash(crowd_h, 1)
    split_index_v= []
    for crowd in crowd_h:
        split_index_v.append(find_crowd_v(crowd, threshold, step))

    object_h = np.hsplit(img, split_index_h)
    object_h = del_trash(object_h, 1)
    objects_imgs = []
    for obj, index in zip(object_h, split_index_v):
        objects = np.vsplit(obj, index)
        result_img = del_trash(objects, 0)
        objects_imgs.extend(result_img)

    return objects_imgs
