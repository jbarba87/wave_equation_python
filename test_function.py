import numpy as np

def cos_t0(data):

  # Return the cos of the function
  t = .5 - .5*np.cos(2*np.pi*data/(data[-1]))
  return t


def sin_t0(data):
  return np.sin(data)
