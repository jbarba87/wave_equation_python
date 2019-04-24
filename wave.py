import numpy as np
import matplotlib.pyplot as plt
# import time

# Class that contains all the data refered to a wave
class Wave:

  dt = 0
  dx = 0
  t_end = 0
  x_end = 0
  coef = 0
  b = 0
  U = []
  t0 = []

  # Constructor
  def __init__ (self, dt, dx, t_end, x_end, coef, b, function_t0):
    self.dt = dt
    self.dx = dx
    self.t_end = t_end
    self.x_end = x_end
    self.coef = coef
    self.b = b
    self.t0 = function_t0 # initial condition function

    # creating time and space vectors
    self.t = np.arange(0., t_end, dt)
    self.x = np.arange(0., x_end, dx)

  # Solve function
  def wave_solve(self):

    c = self.coef*(self.dt/self.dx)
    c = c*c

    U = self.U

    # Creating the vector with the initial condition (use numpy)
    U.append(np.array(self.t0(self.x))) 

    t_future = np.array([0.]*len(self.x))

    U.append(t_future)

    # For i = 0    
    U[1][0] = self.b[0]
    for j in range(1, len(self.x) - 1):
      U[1][j] = c*( U[0][j+1] - 2*U[0][j] + U[0][j-1] ) + 2*U[0][j] - U[0][j] 
    U[1][-1] = self.b[1]

    # For i > 0
    for i in range(1, len(self.t) - 1):
      U.append(np.array(t_future))
      U[i+1][0] = self.b[0]
      for j in range(1, len(self.x) - 1):
        print(j)
        U[i+1][j] = c*( U[i][j+1] - 2*U[i][j] + U[i][j-1] ) + 2*U[i][j] - U[i-1][j]
      U[i+1][-1] = self.b[1]

    return 0


  # Showing function

  def show(self):

    plt.ion()

    for i in range(1, len(self.t) - 1,10):
      plt.clf() # Reseting the plot
      plt.plot(self.x, self.U[i]);
      plt.xlim(0, self.x_end)
      plt.ylim(-1.5, 1.5);
      plt.title('Time: {:02.3f}'.format(i*self.dt))

      plt.pause(0.001)
    plt.close()
    return 0

