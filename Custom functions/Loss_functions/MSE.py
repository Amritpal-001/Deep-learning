import numpy as np


## Implementation 1
def mean_square_error(x , y ):
  '''
  inputs:
  x = actual  ( 1*n shape)
  y = prediction( 1*n shape)
  
  returns:
  MSE loss: Float 
  
  '''
  diff = y - x
  diff_squared = diff ** 2
  mean_diff = diff_squared.mean()
  return(mean_diff)
  
