import numpy as np
import cv2


def find_crowd_h(array):
    (i, j) = array.shape
    split_bool = np.zeros(j, dtype=bool)
    split_index = np.arange(j)
    threshold = i * 0.4
    step = int(j * 0.04)
    for k in range(j):
        l = min(k+step, j)
        if np.sum(array[:, k:l]) < threshold:
            split_bool[k:l] = 1
            
    return split_index[split_bool]


def find_crowd_v(array):
    (i, j) = array.shape
    split_bool = np.zeros(i, dtype=bool)
    split_index = np.arange(i)
    threshold = j * 0.01
    step = int(i * 0.1)
    for k in range(i):
        l = min(k+step, i)
        if np.sum(array[k:l, :]) < threshold:
            split_bool[k:l] = 1
    return split_index[split_bool]


def del_trash(crowd, axes):
    crowds = []
    for c in crowd:
        if c.shape[axes] > 2:
            crowds.append(c)
    return crowds


def main():
    img = cv2.imread('img.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray_img, 20, 110)/255
    split_index_h = find_crowd_h(canny)
    crowd_h = np.hsplit(canny, split_index_h)
    crowd_h = del_trash(crowd_h, 1)        
    split_index_v = []
    for crowd in crowd_h:
        split_index_v.append(find_crowd_v(crowd))

    object_h = np.hsplit(img, split_index_h)
    object_h = del_trash(object_h, 1)
    objects_imgs = []
    for obj, index in zip(object_h, split_index_v):
        objects = np.vsplit(obj, index)
        result_img = del_trash(objects, 0)
        objects_imgs.extend(result_img)

    for image in objects_imgs:
        plt.imshow(cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB))
        plt.show()

if __name__ == '__main__':
    main()
