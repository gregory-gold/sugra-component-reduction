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

and open or create a notebook in the desired representation. If creating a noteboook, make sure to save it at the highest level in the representation folder (i.e., 5DN1 and 4DN2) and import the appropriate modules.

```python
from sugra5DN1 import *
```
This command imports several useful modules for 5D component reduction: `shared`, `latex_macros`, `props`, `subs`, `methods`, and `objects`.

In the `latex_macros` module, we define shorthand notations for various objects. For example, "\a::LaTeXForm("\alpha")" means that "\a" will render as "\alpha" in LaTeX. We use these shorthand notations throughout our modules.

The `shared` module is shared between both 4D and 5D component reduction notebooks. Within it, we've implemented general classes, notably including a sorting algorithm. This algorithm determines how to commute or anti-commute two objects to position them correctly within a term, as described by a sort order.

Within the `Props` module, properties are assigned to indices and objects. For example, it specifies that the vector index in 5D should range from 0 to 4, the spinor index from 1 to 4, and the SU(2) index from 1 to 2. Additionally, fermionic nature is designated for specific objects and indices; if not specified, all are considered bosonic by default. This module also handles defining symmetry properties of objects and declaring all generators as derivatives.

The `subs` module defines all necessary substitutions in 5D N=1 component reduction, including algebra, generators, covariant spinor derivatives acting on fields, contractions, gamma/sigma properties, and more.

In the `methods` module, we've implemented a `cleversimplify` class. This class determines the order in which operations should act to simplify and reduce an expression to components.

See the example notebooks for more detail.


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
