# OOPS
Object Oriented Programming with C++ and Python

## Process of Completion of Exercise
1. perform ```git pull``` from the master branch. This will avoid conflicts if any
2. create a branch with the following command 
``` bash
git checkout -b <USN>-<username>-<Name>
```

3. Complete the exercise along with the output results added in the ```README.md``` of that respective Assignment folder
4. Name of the file which is the entrypoint of execution should always be ```main.cpp``` or ```main.py```
Example:
CPP
main.cpp
``` cpp
int main()
{
    // Your main goes here
    return 0;
}
```
**OR** Python
``` python
def main():
    # your code goes here
    pass

if __name__ == '__main__':
    main()
```

5. Upload the code and results of ```test.sh``` using the following command
6. Finally send me the link of your branch for the review
``` bash
git add .
git commit -m "Code updation"
git push --set-upstream origin <USN>-<username>-<NAME>
```

## How to use test.sh
```
1. Come to the root of the repository (The OOPS directory)
2. Use the following format
usage: ./test.sh <CPP/Python> <Name of the Assignment> 
Example: ./test.sh CPP Splitwise
```
