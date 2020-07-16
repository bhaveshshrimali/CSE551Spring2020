import numpy as np
import os, math, meshio
import matplotlib.pyplot as plt
plt.rc("text", usetex=True)

meshDir = os.path.join(os.getcwd(), "meshes2D")

def read_mesh(meshPath, plot_mesh=False):
    try:
        msh = meshio.read(meshPath)
    except:
        raise ValueError("Mesh file does not exist")

    points = msh.points
    cells = msh.cells[0].data
    if plot_mesh:
        plt.figure(figsize=(8,8))
        plt.triplot(points[:, 0], points[:, 1], cells, "-o")
        plt.show()
    
    return points, cells

nodes, elems = read_mesh(os.path.join(meshDir, "trial6Mesh.msh"), plot_mesh=False)
uvals = np.linalg.norm(nodes, axis=1)
uvals = np.vstack((uvals, uvals**2)).T
print(uvals.shape)
outputMesh = meshio.Mesh(nodes, {"triangle6": elems}, point_data={"temp":uvals})
meshio.xdmf.write("outputTemp.xdmf", outputMesh)