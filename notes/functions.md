## Functions

Defining a function is as simple as this:
```
def print_the_thing():
    print("I am printing the thing.)
    print("watch me print.")
    
def print_the_thing_twice():
    print_the_thing()
    print_the_thing()
    
print_the_thing_twice()
```
This first function definition creates a function that prints a couple of lines. The second function definition just calls the first function twice, so it will print the 2 lines of text twice. Lastly, we call the 2nd function so that when we run the program it executes the code from print_the_thing() twice.

**Flow of execution** Even though we have code that precedes the call of print_the_thing_twice(), the only code that will be exeucted or "output" will be that specific line where the function call is. This is known as the flow of execution. Function definitions do not change the flow of execution of a program so here the "def" portions although required for logic (ie you can't call a function that hasn't been defined), do not matter when it comes to executing statements.

### Parameters and arguments

There may be functions that require arguments. Some functions require passing multiple values as arguments. These arguments are assigned to variables inside the function called parameters.

```
def print_this(x):
    print(x + 1)
```
This function definition will take x as an argument. Inside the function the value of x is assigned to a mathematical operation which takes "x" and adds it to 1.
```
def print_this(x):
    print(x + 1)

print_this(12)
>> 12
```
This shows what would be output if the print_this() function is called with an argument value of 12.
