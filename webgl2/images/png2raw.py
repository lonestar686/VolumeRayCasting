""" convert a png image to a raw file """
import numpy as np
from matplotlib import pyplot as plt

volumes = [
    dict(
        img_name = 'vessels.png',
        C = 1,
        D = 160,
    ),

    dict(
        img_name = 'sagittal.png',
        C = 2,
        D = 176
    ),


    dict(
        img_name = 'handgelenk.jpg',
        C = 4,
        D = 316,
    ),

    dict(
        img_name = 'handgelenk2.jpg',
        C = 2,
        D = 160,
    ),

    dict(
        img_name = 'broccoli.png',
        C = 1,
        D = 50,
    ),

    dict(
        img_name = 'sphere_antialiased.png',
        C = 16,
        D = 256,
    ),

    dict(
        img_name = 'cuuube.png',
        C = 16,
        D = 128,
    ),

    dict(
        img_name = 'smallsphere.png',
        C = 16,
        D = 128,
    ),

]

def convert(vol: dict):
    """ convert image to raw volume """
    C = vol['C']
    D = vol['D']
    img_name = vol['img_name']

    print(f'===> Working on image: {img_name}:')

    # load image
    image = plt.imread(img_name)

    # convert it to byte
    image = (image-image.min())/(image.max()-image.min())*255
    image = image.astype(np.uint8)

    # image dimensions
    img_shapes = image.shape
    H1, W1 = img_shapes[:2]
    if len(img_shapes) == 3:
        image = image[:, :, 0]
        print(f' ###more than two dimension: {img_shapes}')

    # compute volume dimension
    print('input file: {}'.format(img_name))
    print(f'input dimension: H1={H1}, W1={W1}, C={C}, D={D}')
    W = W1//C
    DH = H1*C
    H = DH//D
    print(f'converted dimention: D={D}, H={H}, W={W}')
    print(D, H, W)

    # merge columns
    img_whole = np.empty((C, H1*W), dtype=np.uint8)
    for c in range(C):
        img_whole[c, :] = image[:, c*W:(c+1)*W].flatten()

    img_whole = img_whole.reshape((D, H, W))
    print(img_whole.shape)
    # the meta information
    str_dim = f'-'+ str(D) + 'x' + str(H) + 'x' + str(W) + '-uint8'
    # output
    root, _ = img_name.split('.')
    o_name = root + str_dim + '.raw'
    img_whole.tofile(o_name)

    print('save to {}'.format(o_name))

# convert it
if __name__ == '__main__':
    for vol in volumes:
        convert(vol)
