import getfem as gf
import numpy as np

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_QK(2,1)")
x = [
    2.12968779,
    1.78302097,
    2.0,
    2.41700006,
    1.16499996,
    1.36939037,
    0.0,
    0.0,
    2.83276558,
    3.25,
    1.78299999,
    0.0,
]
y = [
    0.748563945,
    0.453000009,
    0.0,
    0.0,
    0.812830687,
    1.30441773,
    1.58299994,
    1.0,
    1.34800005,
    0.0,
    2.29920578,
    2.75,
]
mesh.add_convex(gt, [[x[0], x[1], x[3], x[2]], [y[0], y[1], y[3], y[2]]])
mesh.add_convex(gt, [[x[4], x[5], x[7], x[6]], [y[4], y[5], y[7], y[6]]])
mesh.add_convex(gt, [[x[8], x[0], x[9], x[3]], [y[8], y[0], y[9], y[3]]])
mesh.add_convex(gt, [[x[10], x[5], x[8], x[0]], [y[10], y[5], y[8], y[0]]])
mesh.add_convex(gt, [[x[5], x[10], x[6], x[11]], [y[5], y[10], y[6], y[11]]])
mesh.add_convex(gt, [[x[5], x[4], x[0], x[1]], [y[5], y[4], y[0], y[1]]])
mesh.save("coarse-quadrilateron-1d.msh")
mesh.export_to_vtk("coarse-quadrilateron-1d.vtk", "ascii")

import pyvista as pv

pv.set_plot_theme("document")

mesh = pv.read("coarse-quadrilateron-1d.vtk")

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

plotter.show(cpos="xy", screenshot="coarse-quadrilateron-1d.png")

import pyvista as pv

pv.set_plot_theme("document")

mesh = pv.read("coarse-quadrilateron-1d.vtk")

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
    ["", "", "", "", "", "", "", "", "P3", "P4", "P2", "P1"],
    italic=True,
    font_size=40,
    shape_color="white",
    point_color="red",
    point_size=30,
    render_points_as_spheres=True,
    always_visible=True,
    shadow=False,
)

plotter.show(cpos="xy", screenshot="coarse-quadrilateron-1d-02.png")

import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

# Parameters
epsilon = 0.1  # depth(mm)
Emodulus = 210000.0 * epsilon  # Young Modulus (N/mm2) * depth(mm)
nu = 0.3  # Poisson Coefficient
clambda = Emodulus * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))
mu = Emodulus / (2.0 * (1 + nu))

mesh = gf.Mesh("load", "coarse-quadrilateron-1d.msh")

fb1 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)
fb2 = mesh.outer_faces_with_direction([0.0, -1.0], 0.01)
fb3 = mesh.outer_faces_with_direction([1.0, 1.0], np.pi / 4.0 - 0.01)

LEFT_BOUND = 1
BOTTOM_BOUND = 2
OUTER_BOUND = 3

mesh.set_region(LEFT_BOUND, fb1)
mesh.set_region(BOTTOM_BOUND, fb2)
mesh.set_region(OUTER_BOUND, fb3)

elements_degree = 1

mfu = gf.MeshFem(mesh, 2)
mfd = gf.MeshFem(mesh, 1)
mfrhs = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)
mfd.set_classical_fem(elements_degree)
mfrhs.set_classical_fem(elements_degree)
mfu.save("coarse-quadrilateron-1d.mfu")

mim = gf.MeshIm(mesh, elements_degree * 2)
mim.save("coarse-quadrilateron-1d.mim")

F = mfrhs.eval(
    "[10.0 * " + str(epsilon) + ", 0.0, 0.0, 10.0 * " + str(epsilon) + "]"
)  # F (N/mm2) * depth (mm)

md = gf.Model("real")
md.add_fem_variable("u", mfu)
md.add_initialized_fem_data("NeumannData", mfrhs, F)
md.add_initialized_data("E", Emodulus)
md.add_initialized_data("nu", nu)
md.add_isotropic_linearized_elasticity_pstress_brick(mim, "u", "E", "nu")
md.add_normal_source_term_brick(mim, "u", "NeumannData", OUTER_BOUND)
# md.add_source_term(mim, "(Reshape(NeumannData,qdim(u),meshdim)*Normal).Test_u", OUTER_BOUND)
md.assembly()
RHS = md.rhs()
print("RHS", RHS)
