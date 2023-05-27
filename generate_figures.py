"""Generate PNG figures from STL 3D files."""

#from glob import glob
#from pathlib import Path

import os

import vtk

def stl_to_png(fname, fname_out):
    # Load STL file
    reader = vtk.vtkSTLReader()
    reader.SetFileName(fname)
    reader.Update()

    # Create mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(reader.GetOutput())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Set actor color to red
    actor.GetProperty().SetColor(109/255.0, 0, 15/255.0)

    # Create renderer and window
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(95/255.0, 95/255.0, 95/255.0) # set background color to white
    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)

    # Adjust camera position and focal point
    camera = renderer.GetActiveCamera()
    bounds = actor.GetBounds()
    center = [(bounds[0]+bounds[1])/2, (bounds[2]+bounds[3])/2, (bounds[4]+bounds[5])/2]
    distance = max(bounds[1]-bounds[0], bounds[3]-bounds[2], bounds[5]-bounds[4])*1.25
    camera.SetPosition(center[0], center[1], center[2]+1.5*distance)
    camera.SetFocalPoint(center[0], center[1], center[2])

    # Create window-to-image filter
    w2if = vtk.vtkWindowToImageFilter()
    w2if.SetInput(window)
    w2if.Update()

    # Create PNG writer
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(fname_out)
    writer.SetInputData(w2if.GetOutput())
    writer.Write()


def generate_figures(dir_3d="3d_files/"):
    for stl_file in os.listdir(dir_3d):
        png_file = os.path.join("figures",stl_file.replace(".STL",".png").replace(".stl",".png"))
        stl_to_png(os.path.join(dir_3d,stl_file), png_file)

if __name__ == "__main__":
    generate_figures()
