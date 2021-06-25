import numpy as np

def calculate(lst):
  if len(lst) == 9:
    lstArray = np.array(lst).reshape([3,3])
    outDict = {
        'mean': [lstArray.mean(axis=0).tolist(),lstArray.mean(axis=1).tolist(),lstArray.mean()],
        'variance': [lstArray.var(axis=0).tolist(),lstArray.var(axis=1).tolist(),lstArray.var()],
        'standard deviation': [lstArray.std(axis=0).tolist(),lstArray.std(axis=1).tolist(),lstArray.std()],
        'max': [lstArray.max(axis=0).tolist(),lstArray.max(axis=1).tolist(),lstArray.max()],
        'min': [lstArray.min(axis=0).tolist(),lstArray.min(axis=1).tolist(),lstArray.min()],
        'sum': [lstArray.sum(axis=0).tolist(),lstArray.sum(axis=1).tolist(),lstArray.sum()]
    }
    return outDict
  else:
    raise ValueError('List must contain nine numbers.')