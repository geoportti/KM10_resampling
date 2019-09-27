# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:14:22 2019

@author: Administrator

This script will go through KM10 files in the km10dir folder and resample them to 
2m resolution using rasterio bilinear resampling. Resampled files are saved to
outdir folder.
"""
import os
import rasterio
from rasterio.enums import Resampling
from rasterio.transform import from_origin


km10dir = r'directory of the km10 files'
outdir = r'directory of the resampled dem files'


# loop through the files 
for filename in os.listdir(km10dir):
    #construct the filepath
    filepath = os.path.join(km10dir,filename)
    # read the demfile and resample it to 2m resolution using rasterio
    with rasterio.open(filepath) as dataset:
        #multiply the heighy and width with 5 to get 2m pixels. In here we use bilinear sampling.
        data = dataset.read(out_shape=(dataset.count, dataset.height * 5, dataset.width * 5),resampling=Resampling.bilinear)
        #get dataset bounds for the transform
        bounds = dataset.bounds
        west = bounds[0]
        north = bounds[3]
        #transform of the new dem file
        out_transform = from_origin(west, north, 2, 2) 
        out_meta = dataset.meta.copy()
    
    #update the metafile of the output 
    out_meta.update({"driver": "GTiff",
                     "height": data.shape[1],
                     "width": data.shape[2],
                     "count": data.shape[0],
                     "crs": dataset.crs,
                     "transform": out_transform})
    
    #rename and save the resampled dem file
    outname = os.path.join(outdir,'{}_2m.tif'.format(filename[0:5]))
    with rasterio.open(outname,"w", **out_meta) as dest:
            dest.write(data)
    print('resampled',filename,'saved')