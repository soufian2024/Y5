# Y5

> ⚠️ **ALPHA - UNDER ACTIVE DEVELOPMENT**  
> **Status**: Educational & Proprietary. Not for commercial use. See LICENSE.

**Y5** is the improved version of `n5`.  
Same philosophy, better experience. Built for learning deep learning with NumPy + SciPy.

### Why Y5 and not n5?

`n5` was public and smooth. `Y5` takes that base and makes it better.

|  | **n5** | **Y5** |
| --- | --- | --- |
| **Core Class `f5`** | Basic activations & losses | **Improved `f5`**: More functions, better numerics, cleaner API |
| **Speed** | Pure NumPy | **NumPy + SciPy** for Conv2D and Pooling |
| **User Experience** | Functional | **Better DX**: Clear errors, type hints, docs, examples |
| **Model Support** | `n5` models only | **Dual Support**: Load `.n5` + New `.y5` format |
| **New Features** | Limited | BatchNorm, Adam, LR Schedulers, More Activations |
| **Goal** | Prototype | **Teach + Research + Benchmark** |

### Key Improvements

1.  **Improved `class f5`**  
    The math core is rewritten. More activation functions, more loss functions, better stability.  
    Same `f5.activation()` and `f5.compute_loss()` style so it's familiar.

2.  **Better User Experience**  
    Cleaner error messages. Full docstrings. Example notebooks. Easier to debug than `n5`.

3.  **Dual Model Support**  
    You can load your old `n5` models directly in Y5.  
    And you can also use the new `Y5` model format with more features.

4.  **SciPy Acceleration**  
    `Conv2D` and `Pooling` layers now use `scipy` internally for a major speed boost.

### Status
`Y5 v0.1 Alpha`. API is stable but may receive improvements. 

### Quick Example
```python
from y5 import yNN, f5
import numpy as np

# Works with new Y5 models
model = yNN.Sequential()
model.add(yNN.Dense(784, 128, activation='relu'))
model.add(yNN.Dense(128, 10, activation='softmax'))

# You can also load old n5 models
# model = yNN.Sequential.load_n5("old_model.n5")
