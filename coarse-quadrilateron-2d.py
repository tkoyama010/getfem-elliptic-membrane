import pyvista as pv

pv.set_plot_theme("document")

mesh = pv.read("coarse-quadrilateron-2d.vtk")

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

plotter.show(cpos="xy", screenshot="coarse-quadrilateron-2d.png")

import pyvista as pv

pv.set_plot_theme("document")

mesh = pv.read("coarse-quadrilateron-2d.vtk")

plotter = pv.Plotter(border=True)

plotter.add_mesh(mesh)
plotter.add_mesh(
    mesh.separate_cells().extract_feature_edges(),
    show_edges=True,
    line_width=5,
    color="black",
)
plotter.add_point_labels(
    mesh.points,
    [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "P5",
        "",
        "P6",
        "P7",
        "",
        "P3",
        "",
        "P4",
        "",
        "P2",
        "",
        "P1",
        "",
    ],
    italic=True,
    font_size=40,
    shape_color="white",
    point_color="red",
    point_size=30,
    render_points_as_spheres=True,
    always_visible=True,
    shadow=False,
)

plotter.show(cpos="xy", screenshot="coarse-quadrilateron-2d-02.png")
