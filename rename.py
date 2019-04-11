import os

path = 'potato_healthy/'
name = 'potato_h_'
counter = 1
for f in os.listdir(path):
    suffix = f.split('.')[-1]
    #if suffix == 'jpg' or suffix == 'png' or suffix == 'JPG'or suffix == 'jpeg':
    if suffix == 'JPG':
        new = '{}.{}'.format(name+str(counter), 'jpg')
        os.rename(path + f, path + new)
        counter = int(counter) + 1
