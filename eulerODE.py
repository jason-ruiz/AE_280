# Creating a script that solves euler ordinary differential equations

# importing packages
import numpy as np
import matplotlib.pyplot as plt


# defining a function for the ODE
def odeEuler(f,y0,x):
    y = np.zeros(len(x))
    y[0] = y0
    for n in range(0,len(x)-1):
        y[n+1] = y[n] + f(y[n], x[n])*(x[n+1] - x[n])
    return y


# values of the x range
x = np.linspace(0,2,11)
y0 = 1
f = lambda y , x: -5 * (x**5) * (y**2)
y = odeEuler(f,y0,x)
k = 0.2
x_true = np.linspace(0, 2, 11)

# true solution
y_true = (1/(1 + x_true)**2)

# error solution
error = abs(y - y_true)/ (y) * .100

# print all given values
for xval in x:
    print("X value: ", xval)
print("")
for yval in y:
    print("Y value: ", yval)
print("")

for xtrue in x_true:
    print("X true value: ", xtrue)
print("")

for ytrue in y_true:
    print("Y true value: ", ytrue)

print("")
for err in error:
    print("Percent error of solution and Euler: ", err)

# plot into a figure
plt.plot(x,y,'r.-',x_true,y_true)
# creates legend
plt.legend(['Euler','True', 'Error'])
# adding grid
plt.grid(True)
# title for figure 1
plt.title("Solution of $y'=-5x^5y^2 , y(0)=1$")
# creating error plot
plot2 = plt.figure(2)
plt.plot(error)
plt.grid(True)
plt.ylabel('Y Value error')
plt.xlabel('Amount of points')
plt.title("Percent error of $y'=-5x^5y^2 , y(0)=1$")
plt.show()
