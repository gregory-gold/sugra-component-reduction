# SUGRA Component Reduction
A framework built on cadabra and python project superspace fields to components in Supergravity (SUGRA).

## About The Project
The modern way to construct off-shell supergravity actions is by a combination of superconformal tensor calculus and superspace approaches. 
However, projecting from superspace to components is, while often straightforward, computationally daunting. This project makes use of computer algebra via cadabra
and provides the framework to reduce fields in superspace to components in $4D, \mathcal{N}=2$ and $5D, \mathcal{N}=1$ supergravity.

## Getting Started
To start, simply install cadabra which itself has various dependencies including python. Follow the instructions on the cadabra [website](https://cadabra.science/download.html).
We can recommend building from source on Linux and macOS. brew and conda are also available as alternatives on macOS.
On Windows, install and enable Windows Subsytem for Linux (WSL) and then build from source on WSL via the Linux instructions. 
Do not build from source in Windows command prompt as it does not work as far as we know.

Once installed, run the following command in Terminal or WSL

```sh
cadabra2-gtk
```

and open or create a notebook in the desired representation. If creating a noteboook, make sure to save it at the highest level in the representation folder (i.e., 5DN1 and 4DN2) and import the appropriate modules. For example, 

```python
from sugra5DN1 import *
```
imports several useful modules (in the form of cadabra notebooks) for $5D$ component reduction: 

- `latex_macros`:  Shorthand LaTeX notations for various objects are define here. For example, `\a::LaTeXForm("\alpha")` means that `\a` will render as $\alpha$ in LaTeX. We use these shorthand notations throughout.

- `props`: Cadabra properties are assigned to indices and objects. For example, it specifies that the vector index in $5D$ should range from 0 to 4, the spinor index from 1 to 4, and the SU(2) index from 1 to 2. Additionally, fermionic nature is designated for specific objects and indices; if not specified, all are considered bosonic by default. This module also handles defining symmetry properties of objects and declaring all generators as derivatives.

- `subs`:  Defines all necessary substitutions in $5D, \mathcal{N}=1$ component reduction, including algebra, generators, covariant spinor derivatives acting on fields, contractions, gamma/sigma properties, and more.

- `methods`:  Includes all pythonic algorithms in classes and stand-alone methods used in component reduction. For example, we've implemented a `cleversimplify` class. This class determines the optimized order in which operations should act to simplify and reduce an expression to components.

- `objects`: Includes predefined objects such as fields and actions that are used in frequently in specific notebooks.

- `shared`: Includes python code that is shared between $4D$ and $5D$. For example, this notably includes a sorting algorithm that determines how to commute or anti-commute two objects to position them correctly within a term, as described by a sort order.

## Usage
WIP

Testing Images and Code+Latex Inclusion

Example 1 (image):
![Alt text](/images/exampleWeyl2.png?raw=true "Weyl2 Example")

Example 2:

```latex
expression := \alpha + \beta;
```

$\alpha + \beta$
