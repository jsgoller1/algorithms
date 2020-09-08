# Makefile system

The makefiles for this repo are stored in `tools/makefiles/`. Once you have started the docker container with this repo mounted as a top-level folder,
the intended workflow is that each subdirectory contains a "thin" Makefile that just imports the Makefiles from `makefiles/` and then executes the
targets to build files in the directory (the build settings for generic C++ do not change, but anything specific to an exercise should be added in that
directory's local Makefile).

In each directory, you should be able to:

- `make solution`: makes the actual solution
- `make alternate-*`: e.g. `make alternate-4`; if there are multiple approaches to a problem, they can be stored in an `alternate-$number.cpp`
- `make python`: if I wrote a Python solution, this can be used to run it.

See `leetcode/1-two-sum/makefile` for an example.
