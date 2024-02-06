# sugra-component-reduction
cadabra and python framework to project superspace fields to components in Supergravity (SUGRA).

## About The Project
The modern way to construct off-shell supergravity actions is by a combination of superconformal tensor calculus and superspace approaches. 
However, projecting from superspace to components is, while often straightforward, computationally daunting. This project makes use of computer algebra via cadabra
and provides the framework to reduce fields in superspace to components in $4D, \mathcal{N}=2$ and $5D, \mathcal{N}=1$ supergravity.

## Getting Started
To start, simply install cadabra which itself has various dependencies including python . Follow the instructions on the cadabra [website](https://cadabra.science/download.html).
We can recommend building from source on Linux and macOS. brew and conda are also available as alternatives on macOS.
On Windows, install and enable Windows Subsytem for Linux (WSL) and then build from source on WSL via the Linux instructions. Do not build from source in Windows Terminal!

Once installed, simply run 

```sh
cadabra2-gtk
```

and create or open a notebook in the desired representation.

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