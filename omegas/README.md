The Gammas
==========

About this Directory
--------------------

1.  This folder will have two gamma files.  gamma1.py will be a situation where
    the Sun is assumed to be made up of all hydrogen.  I will be using pressure
    and density that I looked up for the Sun.  Let's assume the Sun is made up
    of a monatomic ideal gas, therefore gamma = 5/3.  THIS IS NOT REALISTIC
    SITUATIONS.

    (P*V)^gamma = constant, P is pressure, V is volume.

    gamma = ( C_sub(p) / C_sub(v) ) = ( f +2 / f ),

    where f is the number of degrees of freedom of the gas. For monoatomic case,
    the number of degrees of freedom are 3. so (2+3)/3 = 5/3

2.  gamma2.py will be more realistic conditions of the Sun as close as I can
    achieve.

3.  The program will allow you to input any "n" energy mode, and will return the angular modes "l", rotating splitting modes "m", and respective     omegas "w" for the pressure modes "p" and gravitational modes "g".

4.  Picture links below.


![Inputting and Outputting info](https://raw.githubusercontent.com/jaylenw/helioseismology/master/omegas/Screenshot1.png "Inputting and Outputting info")

![Plotting P Modes](https://raw.githubusercontent.com/jaylenw/helioseismology/master/omegas/Screenshot2.png "Plotting P Modes")

![Plotting G Modes Squared](https://raw.githubusercontent.com/jaylenw/helioseismology/master/omegas/Screenshot3.png "Plotting G Modes Squared")

![Plotting G Modes imaginary Components](https://raw.githubusercontent.com/jaylenw/helioseismology/master/omegas/Screenshot4.png "Plotting G Modes imaginary Components")
