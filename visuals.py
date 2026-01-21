import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

values = np.array([[0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 3, 0],
                [0, 0, 0, 3, 3, 3]])

a, b, c, d, e, f = zip(*values)

figure1 = plt.figure()
subplot1 = figure1.add_subplot(111, projection="3d")
subplot1.quiver(a, b, c, d, e, f)

subplot1.set_xlim([0, 5])
subplot1.set_ylim([0, 5])
subplot1.set_zlim([0, 5])

plt.xlabel("x")
plt.ylabel("y")
# plt.zlabel("z")
plt.title("Vector Output")
plt.show()