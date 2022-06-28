# competitive-programming
My notes and solutions from [Codeforces](https://codeforces.com/profile/jsgoller1). My default template file for each problem is at `tools/template.cpp`. 

## Setup
To use the CLI, first execute the following:
```
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Running
Everything can be set up, run, and tested via `cli.py`, so do the setup and run `python3 cli.py --help`

## Structure
Every integer directory corresponds to a Codeforces problemset id, e.g. `/25` for [Codeforces Beta Round #25](https://codeforces.com/problemset/problem/25) (though contest names sometimes differ from problemset ids) and follows this structure:
- Solution files correspond to each problem, e.g. `/25/A.cpp` for problem A ([IQ Test](https://codeforces.com/contest/25/problem/A)). 
- Some problems I solved multiple ways, with each solution matching `<letter>_<solution_version_number>.cpp`, e.g. `4/A_2.cpp`. 
- Test input files match `<letter>_input<i>.txt`, e.g. `/25/A_input0.txt`.

## Credits / References / Resources
- Numerous solutions from other competitors on CodeForces
- [Competitive Programmer’s Handbook](https://cses.fi/book/book.pdf) by Antti Laaksonen
- [Elliott Jin](https://codeforces.com/profile/robot-dreams); I tend to compare my solutions to his when possible and borrowed some of his tricks for my template file. 