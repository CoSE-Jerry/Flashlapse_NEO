#FlashLapse_NEO IR Branch

##Overview
This is a Flashlapse-derived user interface for imaging plant health under heat stress
conditions using a trifecta of infrared cameras: SeekThermal long wavelength IR, an short range IR i
raspberry pi camera (NDVI), and a NoIR camera (rasperry pi camera with no IR filter).

The goal is to use the three camera's information to create a high-resolution image of plants
under heat stress while integrating a more rich sensor dataset from a long wavelength IR camera (low
resolution).

##Setup and Dependencies
This system has been tested on a Raspberry Pi with the Raspian Stretch OS (TODO: Get version information)

###Dependencies
#(TODO: Copy and paste dependencies from other document)
#PyQT5: python-qtpy (apt-get)
#Python Open Computer Vision Library: python-opencv (apt-get)
#libseekthermal (github) - Make sure to do `make install`
#pbcvt (github) - pyboostcvt - Make sure to do `make install`
#py-libseekthermal (github)

###Setup
#Build libseekthermal
#Build py-libseekthermal (grab from github)
#cp pylibseek_ext.so ~/ThermalPlantHeater/Flashlapse_NEO/_python/



