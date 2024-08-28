# Serp++
## About this project
Serp++, or just "Serp", is a hobby programming language that aims to combine the easy-to-use syntax of python and the power of c++.
The big goal of this programming language is to compile already existing python code and its dependencies, even if they are written in c++ or similiar languages that use bind libaries like [pybind11](https://github.com/pybind/pybind11).

This language isn't supposed to be used in production or big projects and should be considered as a hobby project.
## How will it work?
Being still a young student, who has already written assamblers for custom processor architectures and instructions set, this project is still going to be a big and difficult task and will take some time to be complete and ready to use.
Personally, I have gathered some good experiences on how compilers work and how computers execute code. But having never actually worked with a compiler or any compiled programming language, it is obvious that I won't have a clear idea on how it will work nor on how I will implement some things.

As soon I get an idea on how I want to structure everything, I will update this specific section.

# Syntax and execution
## Basic python syntax
For the most of Serp++ I want to feature the already existing python syntax with only slight variations and tweaks.
The goal here is, that every developer, who has already worked with python before, should be able to adapt immediately and write good and performant Serp++ code without any references or documentation.

## The c++ part...
Never having worked with actually c++ (except a few times), I will focus on making c++ functions from libaries or headers avaiable in python programms and not compiling them externally.
This will work by compiling the c++ to its ["object code"](https://en.wikipedia.org/wiki/Object_code) with an already existing compiler like [clang](https://en.wikipedia.org/wiki/Object_code) or [gcc](https://github.com/gcc-mirror/gcc) and then being linked by a the Serp++ linker with the dedicated python executor code.
