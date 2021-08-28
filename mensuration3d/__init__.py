import math

PI = math.pi

def sphere_volume(r):
	vol = 4/3 * r ** 3	
	return vol

def sphere_sa(r):
	sa = 4 * PI * r ** 2
	return sa

def cylinder_volume(r,h):
	vol = PI * r ** 2 * h
	return vol

def cylinder_tsa(r,h):
	sa = 2 * PI * r * (r + h)
	return sa

def cylinder_csa(r,h):
	sa = 2 * PI * r * h
	return sa

def cuboid_volume(l,b,h):
	vol = l * b * h
	return vol	

def cuboid_tsa(l,b,h):
	sa = 2 * ((l * b) + (b * h) + (l * h))
	return sa

def cuboid_lsa(l,b,h):
	sa = 2 * h * (l + b)
	return sa

def cube_volume(edge):
    Vol = edge**3
    return vol

def cube_tsa(edge):
    tsa = 6 * edge * edge
    return tsa

def cube_lsa(edge):
    lsa = 4 * edge * edge
    return edge
