# Y5

> ⚠️ **ALPHA - UNDER ACTIVE DEVELOPMENT**  
> **Status**: Educational & Proprietary. Not for commercial use. See LICENSE.

Y5 is the next-generation educational deep learning framework, inspired by the internal `n5` engine.  
Built with pure NumPy, Y5 aims to be the cleanest and most readable way to understand how neural networks work from scratch.

### Key Goals & Expectations for Y5

Y5 is not meant to replace PyTorch or TensorFlow. It is meant to teach.

| Feature | n5 v2024-2026 | Y5 Roadmap v1.0 |
| --- | --- | --- |
| **Target** | Private / Research | Public / Educational |
| **Code Clarity** | Functional, Dense | Modular, Heavily Commented |
| **Documentation** | Minimal | Full Docs + Examples + Tutorials |
| **Layers** | Dense, Conv2D, Pool, Dropout | All n5 layers + BatchNorm, RNN, LSTM |
| **Activations** | 9 Activations | 9 Activations + Swish, Mish |
| **Save Format** | .n5 proprietary | .y5 + Safe .npz state |
| **License** | Ironclad Proprietary | Ironclad Proprietary |
| **Focus** | Speed of prototyping | Readability & Teaching |

### What to Expect from Y5

1.  **Easier to Learn**: Every function in `f5` and `yNN` will have detailed docstrings and math explanations.
2.  **Better Examples**: We will include 10+ notebooks showing how to build MLP, CNN, and Autoencoders from zero.
3.  **GitHub Friendly**: Clean project structure, issues, and contribution guidelines for bug reports only.
4.  **Stable API**: Once we hit v1.0 the core `yNN.Sequential` API will be frozen.

### Current Status
Y5 is in `Alpha`. The API can and will change. Use only for learning.

### Installation
```bash
pip install numpy
git clone https://github.com/soufian2024/Y5
