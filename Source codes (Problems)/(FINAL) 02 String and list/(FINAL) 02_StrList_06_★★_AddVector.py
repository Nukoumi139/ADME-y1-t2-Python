u = input()
v = input()

u_num = u[1:-1]
v_num = v[1:-1]

vec_u = u_num.split(", ")
vec_v = v_num.split(", ")

ui = float(vec_u[0])
uj = float(vec_u[1])
uk = float(vec_u[2])
vi = float(vec_v[0])
vj = float(vec_v[1])
vk = float(vec_v[2])

si = ui + vi
sj = uj + vj
sk = uk + vk

ou = "[" + str(ui) + ", " + str(uj) + ", " + str(uk) + "]"
ov = "[" + str(vi) + ", " + str(vj) + ", " + str(vk) + "]"
os = "[" + str(si) + ", " + str(sj) + ", " + str(sk) + "]"

print(ou + " + " + ov + " = " + os)