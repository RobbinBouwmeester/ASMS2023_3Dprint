# Static website for the 2023 ASMS 3D-printing exhibit

This repo contains the code to convert 3D STL files to PNG images and render a static website with Quarto.


## Local setup

1. Install Quarto (tested with 1.3.353)
2. Install Python (tested with 3.10)
3. Install Python dependencies: `pip install -r requirements.txt`


## Generate PNG figures from STL files

Run `generate_figures.py` on a machine with an X server available (cannot be run in a headless environment).


## Preview website

Run `quarto preview` to build the website and run a preview webserver.

