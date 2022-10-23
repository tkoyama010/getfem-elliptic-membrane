import pyvista as pv

pv.set_plot_theme("document")

mesh = pv.read("fine-quadrilateron-1d.vtk")

plotter = pv.Plotter(border=True)

plotter.add_mesh(mesh)
plotter.add_mesh(
    mesh.separate_cells().extract_feature_edges(),
    show_edges=True,
    line_width=5,
    color="black",
)
plotter.add_points(
    mesh.points, render_points_as_spheres=True, point_size=30.0, color="red"
)

plotter.show(cpos="xy", screenshot="fine-quadrilateron-1d.png")
