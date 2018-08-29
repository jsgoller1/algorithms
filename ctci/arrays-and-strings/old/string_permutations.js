function test_permutation(string1, string2){
  // Assuming I asked the interviewer about what counts as a permutation,
  // and they replied that whitespaces don't count ("josh" and "jo sh" are
  // permutations), capitalization doesn't matter ("JOSH" and "josh" are
  // permutations).
  string1 = string1.replace(/ /g,"").toLowerCase();
  string2 = string2.replace(/ /g,"").toLowerCase();

  // Once the above occurs, if we sort each string, we can just compare them
  // and determine if they're permutations or not. Bear in mind that this has
  // at least O(n*log(n)) performance
  // Take each string, convert it to an array, sort, convert back to
  // a string, and compare.
  if (string1.split("").sort().join("") !== string2.split("").sort().join("")){
    return false;
  }
  return true;
}

console.log(test_permutation("foo","foo"));
console.log(test_permutation("foo","bar"));
console.log(test_permutation("Boson","Nosob"));
console.log(test_permutation("joshua samuel goller","JOSHUASAMUELGOLLER"));
console.log(test_permutation("Du hast mich gefragt", "Und ich hab nichts gesagt"));
console.log(test_permutation("banbanban","nabnabnab"));
console.log(test_permutation("",""));
