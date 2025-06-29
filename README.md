<h3 align="center"><img src="https://github.com/user-attachments/assets/0114cde3-f7c2-4769-97d6-4cb219f8ef62" alt="welcome text" height="250px"></h3>

# forgefetch

## what is this
forgefetch - fully customizable console fetch.
you can customize it using instances and renderers. write your own or use mine https://github.com/evryoneowo/evryforgefetch

## how to use
install via `./install.sh`
run the program with `forgefetch`.

## how to install a renderer
renderer is a .py file contains render func. installation step-by-step:
1. move your renderer to the `renderers/` directory.
2. enter the name of renderer in `~/.forgefetch` (`renderer="name"`).

## how to install an instance
instance is a .py file contains fetching vars and rendering it. installation step-by-step:
1. move your instance to the `instances/` directory.
2. enter the name of instance in `~/.forgefetch` (`instance="name"`).

## how to write my own renderer
you need to write a .py file with func called the same as the file. then, you can use a richdata renderer as reference. it's easy!

## how to write my own instance
you need to write a .py file with `run()` func that prints fetch. then, you can use a standard instance as reference. it's easy!
