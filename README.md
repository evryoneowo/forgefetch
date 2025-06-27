![richdata renderer](https://github.com/user-attachments/assets/7c90cccc-c667-44fb-a768-275029e3fb14)

# forgefetch

## what is this
forgefetch - customizable console fetch. the main feature is renderers.

## how to use
just run `instance.py`.

## how to install renderer
renderer is a .py file contains render func. installation step-by-step:
1. move your renderer to the forgefetch directory.
2. enter the name of renderer in `config.json` (`renderer="name"`).
3. now you can just run `instance.py`!

## how to write my own renderer
you need to write a .py file with func called the same as the file. then, you can use a richdata renderer as reference. it's easy!

## how to customize fetch
you can import `instance.py` and use already created `Fetch` object `fetchmain` or import `fetch.py` for using it manually.
