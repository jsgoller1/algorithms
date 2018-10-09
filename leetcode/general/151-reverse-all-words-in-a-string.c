/*
Statement:

Given an input string, reverse the string word by word.

Example:
Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.

Input string may contain leading or trailing spaces. However,
your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single
space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.

input: string
output: string, modified correctly so it is reversed and has no superfluous spaces


Compile with:
clang -std=c11 -Weverything -Werror 151-reverse-all-words-in-a-string.c -o ../../bin/151.bin && ../../bin/151.bin
----
Understand / Plan

We need to do three things to produce a correct answer:
- reverse the order of the words in the string
- remove unnecessary spaces between words
- remove trailing or leading spaces

We can accomplish this in these steps:
- strip leading spaces
- reverse the entire string
- re-reverse each word in the string to get correct ordering
- remove middle spaces with a constance space implementation
of memmove
- strip trailing whitespaces by moving null terminator up

Based on the problem boilerplate, we are going to assume that
the string is always null terminated.
----
Execute

See code below
----
Review:

Viewed the following discussions:
*/

#include <stdio.h>
#include <string.h>

static size_t strip_leading_spaces(char *const s, size_t len)
{
  (void)s;
  (void)len;
  return 0;
}

static void reverse(char *const s, const size_t len)
{
  (void)s;
  (void)len;
}

static void reverse_words(char *const s, const size_t len)
{
  (void)s;
  (void)len;
}

static size_t strip_middle_spaces(char *const s, size_t len)
{
  (void)s;
  (void)len;
  return 0;
}

static size_t strip_trailing_spaces(char *const s, size_t len)
{
  (void)s;
  (void)len;
  return 0;
}

static void reverseWords(char *s)
{
  size_t len = strlen(s);
  len = strip_leading_spaces(s, len);
  reverse(s, len);
  reverse_words(s, len);
  len = strip_middle_spaces(s, len);
  (void)strip_trailing_spaces(s, len);
}

int main()
{
  // basic smoke test
  char string1[] = "the sky is blue";
  char string2[] = "blue is sky the";
  reverseWords(string1);
  if (strcmp(string1, string2) != 0)
  {
    printf("Failed to first second string: %s\n", string1);
    return -1;
  }

  // Test leading and middle spaces
  char string3[] = "   the     sky  is   blue   ";
  char string4[] = "blue is sky the";
  reverseWords(string3);
  if (strcmp(string3, string4) != 0)
  {
    printf("Failed to reverse second string: %s\n", string3);
    return -1;
  }

  printf("Correctly reversed string.\n");
  return 0;
}
