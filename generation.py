import json
import numpy as np

n = 100
p = dict()
p['capacity'] = np.random.rand(n).tolist()
p['free'] = np.random.rand(n).tolist()
p['demand'] = n
p['number'] = n

with open('parameter.json', 'w') as f:
    json.dump(p, f)
