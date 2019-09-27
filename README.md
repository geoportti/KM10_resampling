# KM10_resampling

National land survey of Finland provides two kinds of digital elevation models (dem) based on the aerial laser scanning data KM10 and KM2. While KM10 dem (10m pixel size) covers the whole Finland, the KM2 (2m pixel size) covers only most of it (Image 1). When running analyses on big areas it is sometimes nessesary to resample KM10 data to 2m resolution. This way analyses for all areas can be run in same spatial resolution.
There are many ways to resample raster datasets and they all include some errors. In this example we show a efficient way to resample big areas using python module rasterio. You can read more about the rasterio resampling methods in [here][1]. 

<img src=https://github.com/geoportti/KM10_resampling/blob/master/images/dem_availability_small.png>

Image 1. KM10 and KM2 availability in Finland

##







<img src=https://github.com/geoportti/KM10_resampling/blob/master/images/comparison.png>


[1]:https://rasterio.readthedocs.io/en/stable/topics/resampling.html
