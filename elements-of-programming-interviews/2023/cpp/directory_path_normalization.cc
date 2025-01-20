#include <string>
#include <vector>

#include "test_framework/generic_test.h"
using std::string;
using std::vector;

/*
- Cases:
  - absolute path (begins with /)
  - relative path (no prefix /)

- Tokens:
  - ".."
    - relative: if the top of the (nonempty) stack is not "..", should pop.
Otherwise, push it.
    - nonrelative: always pop the top of the (nonempty) stack
  - "."
    - represents current dir; can be ignored
  - ""
    - represents "//"; can be ignored (or treated as ".")
  - (any chars)
    - represents a directory name. Has to be pushed, may be removed.
*/

string assembleFinalPath(const vector<string>& dirs, bool isAbsolute) {
  string path = isAbsolute ? "/" : "";
  for (string dir : dirs) {
    path += dir + "/";
  }
  if (path.size() > 1) {
    path.erase(path.end() - 1);
  }
  return path;
}

void processAbsolute(vector<string>& dirs, vector<string>& processedDirs) {
  for (string dir : dirs) {
    if (dir == "..") {
      if (!processedDirs.empty()) {
        processedDirs.pop_back();
      }
    } else {
      processedDirs.push_back(dir);
    }
  }
}

void processRelative(vector<string>& dirs, vector<string>& processedDirs) {
  for (string dir : dirs) {
    if (dir == ".." && !processedDirs.empty() && processedDirs.back() != "..") {
      processedDirs.pop_back();
    } else {
      processedDirs.push_back(dir);
    }
  }
}

void stripPath(const string& path, vector<string>& dirs) {
  string curr = "";
  for (int i = 0; i <= path.size(); i++) {
    if ((i == path.size() || path[i] == '/')) {
      if (!curr.empty() && curr != ".") {
        dirs.push_back(curr);
      }
      curr.clear();
    } else {
      curr += path[i];
    }
  }
}

string ShortestEquivalentPath(const string& path) {
  if (path.empty()) {
    return path;
  }
  bool isAbsolute = (path[0] == '/');
  vector<string> dirs, processedDirs;
  stripPath(path, dirs);
  isAbsolute ? processAbsolute(dirs, processedDirs)
             : processRelative(dirs, processedDirs);
  return assembleFinalPath(processedDirs, isAbsolute);
}

int main(int argc, char* argv[]) {
  /*
  ShortestEquivalentPath("");
  ShortestEquivalentPath("home");
  ShortestEquivalentPath("home/foobar");
  ShortestEquivalentPath("../home/foobar");
  ShortestEquivalentPath("../../home/foobar");
  ShortestEquivalentPath("../../home/../foobar");
  ShortestEquivalentPath("/");
  ShortestEquivalentPath("/../../");
  ShortestEquivalentPath("/home");
  ShortestEquivalentPath("/home/foobar/");
  ShortestEquivalentPath("/../home/foobar/");
  ShortestEquivalentPath("/../../home/foobar");
  ShortestEquivalentPath("/../../home/../foobar");
  ShortestEquivalentPath("/.");
  */

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"path"};
  return GenericTestMain(args, "directory_path_normalization.cc",
                         "directory_path_normalization.tsv",
                         &ShortestEquivalentPath, DefaultComparator{},
                         param_names);
}
