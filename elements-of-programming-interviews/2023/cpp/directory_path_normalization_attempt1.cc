#include <deque>
#include <stack>
#include <string>

#include "test_framework/generic_test.h"
using std::deque;
using std::stack;
using std::string;

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

#define PARENT_DIR ".."
#define CURR_DIR "."
#define CONTINUE_PARSING 1
#define HALT_PARSING 0

string assemblePath(stack<string, deque<string>>& s, bool isAbsolute) {
  if (s.empty()) {
    return "";
  }
  string path = "";
  while (!s.empty()) {
    path = s.top() + "/" + path;
    s.pop();
  }
  path.erase(path.end() - 1);
  path = ((isAbsolute) ? "/" : "") + path;
  printf("Final path: %s\n", path.c_str());

  return path;
}

void handleDirRelative(stack<string>& s, const string& dir) {
  if (dir == "..") {
    if (s.empty() || s.top() == "..") {
      s.push(dir);
    } else {
      s.pop();
    }
  } else if (!(dir == ".") && !(dir == "")) {
    s.push(dir);
  }
}

void handleDirAbsolute(stack<string>& s, const string& dir) {
  if (dir == ".." && !s.empty()) {
    s.pop();
  } else if (!(dir == ".") && !(dir == "")) {
    s.push(dir);
  }
}

string ShortestEquivalentPath(const string& path) {
  if (path.empty()) {
    return "";
  }
  printf("\nInitial path: %s\n", path.c_str());
  stack<string> s;
  bool isAbsolute = (path[0] == '/');
  string currPath = path;

  auto begin_it = path.begin(), end_it = path.begin();
  for (int i = 0; i < path.size(); i++) {
    // printf("i: %d\n", i);
    if (path[i] == '/' || i == path.size() - 1) {
      end_it = path.begin() + i;
      string dir(begin_it, end_it);
      // printf("dir: %s\n", dir.c_str());
      isAbsolute ? handleDirAbsolute(s, dir) : handleDirRelative(s, dir);
      begin_it = end_it + 1;
    }
  }

  return assemblePath(s, isAbsolute);
}

int main(int argc, char* argv[]) {
  /*
  ShortestEquivalentPath("");
  ShortestEquivalentPath("home");
  ShortestEquivalentPath("home/foobar");
  ShortestEquivalentPath("../home/foobar");
  ShortestEquivalentPath("../../home/foobar");
  ShortestEquivalentPath("../../home/../foobar");
  */
  ShortestEquivalentPath("/");
  ShortestEquivalentPath("/../../");
  ShortestEquivalentPath("/home");
  ShortestEquivalentPath("/home/foobar/");
  ShortestEquivalentPath("/../home/foobar/");
  ShortestEquivalentPath("/../../home/foobar");
  ShortestEquivalentPath("/../../home/../foobar");
  /*
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"path"};
  return GenericTestMain(args, "directory_path_normalization.cc",
                         "directory_path_normalization.tsv",
                         &ShortestEquivalentPath, DefaultComparator{},
                         param_names);
  */
}
