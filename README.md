# Basic Arithmetic Operator

Basic arithmetic operator is a simple python application that allows user to add,subtract, multiply and divide two numbers.

## Usage

Unzip and Untar the package `ArithmeticOperator.tar.gz`

Make sure that python 2.7 is installed in your system

_Method 1_:
Launch cmd prompt from the directory where `Arithmetic_Operations.py` is available


```python
python Arithmetic_Operations.py
```

_Method 2_: Launch `Arithmetic_Operations.pyc` from the extracted path

## Build & Validation

As this is developed in Python building the code is not required. The build script `Build.sh` is bash and runs linter analysis, checks for code integrity.

`pylint`is used for code analysis, hence please install `pylint` in the system before running the build script.

```python
pip install pylint
```

 GitBash can be used to run the build script.

## Running Tests

`TestArithmetic_Operations.py` is the test script to validate `Arithmetic_Operations.py`. It has four tests with two combinations for each test.

```python
python TestArithmetic_Operations.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```
## Packaging

Packaging is done by the bash script `PackageScript.sh`
. The script should be executed by passing two arguments, one is the source directory where the artifacts to be packaged is present and two is a BOM file (`BOM.txt` is a text file which has the list of artifacts to be packaged).

The script compares the list of artifacts from `BOM.txt` with artifacts present in the directory and exits if any artifact is missing from source directory. It also throws a warning but continues packaging if any extra artifact is present in the source directory.

```
./PackageScript.sh <source directory> <path/BOM.txt>
```

## Housekeeping

`Cleanup.sh` removes `.gz` artifacts older than three days from source directory.

## Containerization

`Dockerfile` is to install and run the app locally.

`Dockerfile` invokes `Dockerscript.sh`. Amend the `Dockerscript.sh` accordingly with the necessary arguments.
