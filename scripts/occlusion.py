import maya.cmds as cmds
from maya.api import OpenMaya
from collections import defaultdict
import time
import spheral


RAY_PRESETS = {
    48: [
        OpenMaya.MVector(1.0, 0.0, 0.0),
        OpenMaya.MVector(0.707, 0.0, -0.707),
        OpenMaya.MVector(-0.0, 0.0, -1.0),
        OpenMaya.MVector(-0.707, 0.0, -0.707),
        OpenMaya.MVector(-1.0, 0.0, 0.0),
        OpenMaya.MVector(-0.707, 0.0, 0.707),
        OpenMaya.MVector(-0.0, 0.0, 1.0),
        OpenMaya.MVector(0.707, 0.0, 0.707),
        OpenMaya.MVector(0.883, 0.222, 0.414),
        OpenMaya.MVector(0.917, 0.222, -0.331),
        OpenMaya.MVector(0.414, 0.222, -0.883),
        OpenMaya.MVector(-0.331, 0.222, -0.917),
        OpenMaya.MVector(-0.883, 0.222, -0.414),
        OpenMaya.MVector(-0.917, 0.222, 0.331),
        OpenMaya.MVector(-0.414, 0.222, 0.883),
        OpenMaya.MVector(0.331, 0.222, 0.917),
        OpenMaya.MVector(0.645, 0.411, 0.645),
        OpenMaya.MVector(0.912, 0.411, 0.0),
        OpenMaya.MVector(0.645, 0.411, -0.645),
        OpenMaya.MVector(0.0, 0.411, -0.912),
        OpenMaya.MVector(-0.645, 0.411, -0.645),
        OpenMaya.MVector(-0.912, 0.411, 0.0),
        OpenMaya.MVector(-0.645, 0.411, 0.645),
        OpenMaya.MVector(0.0, 0.411, 0.912),
        OpenMaya.MVector(0.286, 0.539, 0.792),
        OpenMaya.MVector(0.762, 0.539, 0.358),
        OpenMaya.MVector(0.792, 0.539, -0.286),
        OpenMaya.MVector(0.358, 0.539, -0.762),
        OpenMaya.MVector(-0.286, 0.539, -0.792),
        OpenMaya.MVector(-0.762, 0.539, -0.358),
        OpenMaya.MVector(-0.792, 0.539, 0.286),
        OpenMaya.MVector(-0.358, 0.539, 0.762),
        OpenMaya.MVector(-0.164, 0.73, 0.663),
        OpenMaya.MVector(0.353, 0.73, 0.585),
        OpenMaya.MVector(0.663, 0.73, 0.164),
        OpenMaya.MVector(0.585, 0.73, -0.353),
        OpenMaya.MVector(0.164, 0.73, -0.663),
        OpenMaya.MVector(-0.353, 0.73, -0.585),
        OpenMaya.MVector(-0.663, 0.73, -0.164),
        OpenMaya.MVector(-0.585, 0.73, 0.353),
        OpenMaya.MVector(-0.336, 0.913, 0.233),
        OpenMaya.MVector(0.125, 0.913, 0.389),
        OpenMaya.MVector(0.409, 0.913, 0.0),
        OpenMaya.MVector(0.125, 0.913, -0.389),
        OpenMaya.MVector(-0.317, 0.913, -0.258),
        OpenMaya.MVector(0.0, 1.0, 0.0),
    ],
    24: [
        OpenMaya.MVector(0.707, 0.0, -0.707),
        OpenMaya.MVector(-0.707, 0.0, -0.707),
        OpenMaya.MVector(-0.707, 0.0, 0.707),
        OpenMaya.MVector(0.707, 0.0, 0.707),
        OpenMaya.MVector(0.917, 0.222, -0.331),
        OpenMaya.MVector(-0.331, 0.222, -0.917),
        OpenMaya.MVector(-0.917, 0.222, 0.331),
        OpenMaya.MVector(0.331, 0.222, 0.917),
        OpenMaya.MVector(0.912, 0.411, 0.0),
        OpenMaya.MVector(0.0, 0.411, -0.912),
        OpenMaya.MVector(-0.912, 0.411, 0.0),
        OpenMaya.MVector(0.0, 0.411, 0.912),
        OpenMaya.MVector(0.762, 0.539, 0.358),
        OpenMaya.MVector(0.358, 0.539, -0.762),
        OpenMaya.MVector(-0.762, 0.539, -0.358),
        OpenMaya.MVector(-0.358, 0.539, 0.762),
        OpenMaya.MVector(0.353, 0.73, 0.585),
        OpenMaya.MVector(0.585, 0.73, -0.353),
        OpenMaya.MVector(-0.353, 0.73, -0.585),
        OpenMaya.MVector(-0.585, 0.73, 0.353),
        OpenMaya.MVector(0.125, 0.913, 0.389),
        OpenMaya.MVector(0.125, 0.913, -0.389),
        OpenMaya.MVector(0.0, 1.0, 0.0),
    ],
    12: [
        OpenMaya.MVector(0.707, 0.0, -0.707),
        OpenMaya.MVector(-0.707, 0.0, 0.707),
        OpenMaya.MVector(0.917, 0.222, -0.331),
        OpenMaya.MVector(-0.917, 0.222, 0.331),
        OpenMaya.MVector(0.912, 0.411, 0.0),
        OpenMaya.MVector(-0.912, 0.411, 0.0),
        OpenMaya.MVector(0.762, 0.539, 0.358),
        OpenMaya.MVector(-0.762, 0.539, -0.358),
        OpenMaya.MVector(0.353, 0.73, 0.585),
        OpenMaya.MVector(-0.353, 0.73, -0.585),
        OpenMaya.MVector(0.125, 0.913, 0.389),
        OpenMaya.MVector(0.0, 1.0, 0.0),
    ],
    6: [
        OpenMaya.MVector(-0.707, 0.0, 0.707),
        OpenMaya.MVector(-0.917, 0.222, 0.331),
        OpenMaya.MVector(-0.912, 0.411, 0.0),
        OpenMaya.MVector(-0.762, 0.539, -0.358),
        OpenMaya.MVector(-0.353, 0.73, -0.585),
        OpenMaya.MVector(0.0, 1.0, 0.0),
    ],
    1: [
        OpenMaya.MVector(0.0, 1.0, 0.0)
    ],
}

def calculate(dagpath, max_dist=1, falloff=1, num_rays=1, random=False,
                      smooth_iterations=0):
    '''Calculate ambient occlusion for the provided MFnMesh'''

    mesh_fn = OpenMaya.MFnMesh(dagpath)
    mesh_iter = OpenMaya.MItMeshPolygon(dagpath)
    num_verts = mesh_fn.numVertices
    falloff = 1.0 / falloff

    weights_dict = dict((i, [0.0, False]) for i in xrange(num_verts))

    while not mesh_iter.isDone():
        n = OpenMaya.MFloatVector(mesh_iter.getNormal())
        p = mesh_iter.center()
        if random:
            rays = (spheral.hemispheral_vector(n) for i in xrange(num_rays))
        else:
            rays = spheral.rotate_vectors(
                RAY_PRESETS[num_rays],
                OpenMaya.MVector(n),
                OpenMaya.MFloatVector)
        hits = []
        for r in rays:
            hit = mesh_fn.anyIntersection(
                OpenMaya.MFloatPoint(p) + n * 0.005,
                r,
                OpenMaya.MSpace.kWorld,
                max_dist,
                False,
                accelParams=mesh_fn.autoUniformGridParams(),
                )
            if hit:
                hits.append(hit[1])

        if hits:
            s = 1.0 / len(hits)
            w = sum(hits) * s * falloff

        for v in mesh_iter.getVertices():
            weights_dict[v][0] += w
            if weights_dict[v][1]:
                weights_dict[v][0] *= 0.5
            else:
                weights_dict[v][1] = True

        mesh_iter.next(1)

    vert_weights = [weights_dict[i][0] for i in xrange(num_verts)]

    if smooth_iterations:
        neighbors = defaultdict(list)
        for e in xrange(mesh_fn.numEdges):
            v1, v2 = mesh_fn.getEdgeVertices(e)
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        for si in xrange(smooth_iterations):
            post_smooth = []
            for i in xrange(num_verts):
                w = vert_weights[i]
                nw = [vert_weights[neighbor] for neighbor in neighbors[i]]
                post_smooth.append((w + sum(nw)) / (len(nw) + 1))
            vert_weights = post_smooth

    return vert_weights
