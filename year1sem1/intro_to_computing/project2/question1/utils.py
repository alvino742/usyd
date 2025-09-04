import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from poliastro_atmosphere import COESA76
from astropy import units as u

model = COESA76()

def density(altitude):
    """Compute atmospheric density given altitude in m"""
    rho = model.density(altitude * u.m)
    return rho.value

def plot_earth(ax, earth_radius=6378e3):

    # Store xlims
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()

    # Load the circular PNG image of the Earth
    earth_img = mpimg.imread('circular_earth.png')
    
    # Get the dimensions of the image
    img_height, img_width = earth_img.shape[:2]
    
    # Scale the image to match the Earth radius
    scale_factor = earth_radius / img_width
    new_width = img_width * scale_factor
    new_height = img_height * scale_factor
    
    # Display the image centered at the origin (Earth's position)
    ax.imshow(earth_img, extent=[-new_width, new_width, -new_height, new_height], aspect='auto')

    # Reset axes limits
    xlims = [np.min([-1.2*earth_radius, xlims[0]]), np.max([1.2*earth_radius, xlims[1]])]
    ylims = [np.min([-1.2*earth_radius, ylims[0]]), np.max([1.2*earth_radius, ylims[1]])]
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
