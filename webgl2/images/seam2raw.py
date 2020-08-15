
import numpy as np

def normalize(c):
    cmin, cmax = np.amin(c), np.amax(c)
    return (c-cmin)/(cmax-cmin)*255

# original dimension
ny, nx, nz = 1001, 876, 751

# output dimension
o_ny, o_nx, o_nz  = ny, nx, nz

# # a small cube
o_ny, o_nx, o_nz = 256, 256, 256

imgfile="../../../../DeepLearning/DataSet/seam/img_zxy.H@"
# in yxz order
a = np.fromfile(imgfile, dtype=np.float32)
a = normalize(a).astype(np.uint8).reshape(ny, nx, nz)
print(np.amin(a), np.amax(a))
# a.tofile('seam_img_1001x876x751_uint8.raw')
a1 = a[o_ny:o_ny+256, o_nx:o_nx+256, o_nz:o_nz+256]
a1.tofile('seam_img-{}x{}x{}-uint8.raw'.format(o_ny, o_nx, o_nz))

# # salt density
# SALT_DEN = 2.165

# maskfile = "../../../DeepLearning/DataSet/seam/mask_zxy.H@"
# b = np.fromfile(maskfile, dtype=np.float32)
# b[b == SALT_DEN] = 128
# b[b != 128] = 0
# b=b.astype(np.uint8).reshape(ny, nx, nz)
# print(np.amin(b), np.amax(b))
# # b.tofile('seam_mask_1001x876x751_uint8.raw')
# b1 = b[:o_ny, :o_nx, :o_nz]
# b1.tofile('seam_mask-{}x{}x{}-uint8.raw'.format(o_ny, o_nx, o_nz))

