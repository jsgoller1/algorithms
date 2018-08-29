// CtCI specifically says that there is "enough space at the end of the string
// for inserting new characters", but even so, this is JavaScript.

// This is how you should do it in real life; never re-invent the wheel.
function replace_simple(string){
  return string.replace(/ /g, "%20");
}

function replaceAt(string, index, newchar){
  var array = string.split("")
  array[index] = newchar;
  return array.join("");
}

// This is sort of a contrived-looking solution given that the original one was
// written in Java; the catch was that you're given a "true length" of the
// string despite the actual string being of a certain length due to added
// padding. That is, "dog   " would have length 3, despite the whitespace at
// the end. However, because JavaScript strings are mutable, we just add the
// whitespace padding to the end. This is all monstrously stupid, and you should
// just use .replace() or equivalent in real life.
function replace_interview(string){
  var space_count = 0;
  // First, figure out how many whitespaces there are in the 'true string'
  for (var i = 0; i < string.length; i++){
    if (string[i] === " "){
      space_count++;
    }
  }
  // Then, add the padding to the end
  var strlen = string.length;
  string = string + Array(space_count*2).join(" ");
  var newlen = string.length;

  // Then loop through the string and copy the characters one by one,
  // substituting "%20" for " "
  // God I fucking hate programming interviews so fucking much, I could have
  // been doing something fun right now like writing my Linux rootkit but noooo
  // some jerkoff wants to know if I know how to replace whitespace by hand (╯°□ °）╯︵ ┻━┻

  for (var i = strlen-1; i >= 0; i--){
    if (string[i] === " ") {
      string = replaceAt(string, newlen-2, "%");
      string = replaceAt(string, newlen-1, "2");
      string = replaceAt(string, newlen, "0");
      newlen -= 3;
    } else {
      string = replaceAt(string, newlen, string[i]);
      newlen--;
    }
  }
  return string;
}

console.log(replace_simple("Joshua Samuel Goller"));
console.log(replace_interview("Joshua Samuel Goller"));
