# Y5

> **Y5 v0.1 Alpha**  
> The upgraded successor to `n5`. Built for learning Deep Learning with NumPy + SciPy.  
> **Status**: Educational & Proprietary. Not for commercial use.

`Y5` was released on Aug 7, 2026. One day after `n5`.  
Why? Because we learned. `n5` was solid. `Y5` is faster, easier, and better.

---

### ⚡ Quick View / نظرة سريعة / Aperçu Rapide

**[AR] العربية**  
`Y5` هي النسخة المطورة من مكتبة `n5`.  
الهدف: تعليم الشبكات العصبية من الصفر.  
الجديد: أسرع 10 مرات في `Conv2D` بفضل `SciPy` + تجربة مستخدم أسهل + دعم لموديلات `n5` القديمة.  
الترخيص: استخدام شخصي وتعليمي فقط. ممنوع التجارة.

**[FR] Français**  
`Y5` est la version améliorée de la librairie `n5`.  
Objectif: Apprendre le Deep Learning from scratch.  
Nouveauté: 10x plus rapide sur `Conv2D` grâce à `SciPy` + Meilleure UX + Support des anciens modèles `n5`.  
Licence: Usage personnel et éducatif uniquement. Usage commercial interdit.

**[EN] English**  
`Y5` is the improved version of `n5`.  
Goal: Learn Deep Learning from scratch.  
What's new: 10x faster `Conv2D` with `SciPy` + Better DX + Backward support for `n5` models.  
License: Personal and educational use only. No commercial use.

---

### What is Y5?

Y5 is an object-oriented deep learning framework written in pure Python.  
Same philosophy as `n5`: understand every line of code.  
New goal: make it faster with SciPy and make the developer experience smooth.

### n5 vs Y5

`n5` was public and worked great for MLPs. `Y5` fixes the bottlenecks.

| Feature | **n5** | **Y5** |
| --- | --- | --- |
| **Core `class f5`** | 9 Activations, 5 Losses | **Improved**: More funcs, better numerics, cleaner API |
| **CNN Speed** | `O(n²)` Python loops | **`O(n log n)` with SciPy** - 5x to 10x faster |
| **Dense/MLP Speed** | Fast with NumPy | **Same speed** |
| **User Experience** | Functional | **Better**: Clear errors, type hints, docs, examples |
| **Model Support** | `.n5` format only | **Dual Support**: Load `.n5` and new `.y5` format |
| **New Layers** | Dense, Conv2D, Pool, Dropout | **+ BatchNorm, Residual, LR Schedulers** |
| **Optimizers** | SGD only | **+ Adam, RMSprop** |

### Key Improvements in Y5

1.  **Improved `class f5`**  
    The math core is rewritten for stability and clarity.  
    Same `f5.activation()` and `f5.compute_loss()` style so n5 users feel at home.
    
2.  **SciPy Acceleration**  
    `Conv2D` and `Pooling` now use `scipy.signal` and `scipy.ndimage` internally.  
    This is where Y5 wins big vs n5.
    
3.  **Better User Experience**  
    Better error messages. Full docstrings. 5+ example notebooks. Easier debugging.

4.  **Dual Model Compatibility**  
    You can load your old `n5` models directly: `Sequential.load_n5("model.n5")`  
    And save new models in the improved `.y5` format.

### Installation
```bash
pip install numpy scipy
git clone https://github.com/soufian2024/Y5| **New Features** | Limited | BatchNorm, Adam, LR Schedulers, More Activations |
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
