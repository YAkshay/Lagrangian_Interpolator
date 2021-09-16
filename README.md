# Lagrangian Interpolator GUI
== Description ==

The following GUI lets you plot an approximate curve with the points
you give as input using lagrangian interpolation between those points.
The code takes input points from the user, then takes 50(by default)
points between the minimum and maximum x-coordinate and finds the
value of y using a linear combination of Lagrange basis polynomials.

== How to use ==
1) Select the number of points with which you want to interpolate.
2) Type in the x and y coordinates of the points in their respective
columns.
3) Click the 'Plot' push-button. A curve will be plotted in the right portion
of the GUI, which represents the polynomial made up by the input points.
4) you change the number of samples in the curve plotted by
sliding the bar from the sliding widget.
5) Type in the value of x where you want to find the value of the
polynomial.
6) On clicking the 'Find' push-button, you can see the value being printed
below on the GUI.
