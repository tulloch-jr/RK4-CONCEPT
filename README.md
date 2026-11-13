# RK4-CONCEPT

This project demonstrates how to use the fourth-order Runge-Kutta method
(usually called **RK4**) to estimate the solution to a differential equation.

## The idea

A differential equation describes how a value changes. This example uses
`dy/dt = y`: the rate of change of `y` is equal to its current value. Starting
from `y = 1` at `t = 0`, the exact solution is `y = e^t`.

Computers usually solve this kind of problem by taking small steps. In each
step, RK4 checks the slope four times: at the beginning, at two estimates of
the midpoint, and at the end. It combines those slopes using a weighted
average to estimate the next value. Using several slopes makes RK4 generally
more accurate than using only the slope at the beginning of each step.

In this script, each step has size `0.1`, and the method takes 30 steps from
`t = 0` to `t = 3`. The plot compares the RK4 estimates with the exact curve
`e^t`. The closer the two curves are, the better the numerical estimates.

## Run the program

You need Python and the `numpy` and `matplotlib` packages. Install the
packages with:

```powershell
python -m pip install numpy matplotlib
```

Run the script from this folder:

```powershell
python RK41.PY
```

The program displays no interactive window; it saves the comparison plot as
`RK41_result.png` in the current directory.
