/* jshint node: true, esnext: true */

'use strict';

let compute = (firstString, secondString) => {

  if (firstString.length !== secondString.length) throw new Error("DNA strands must be of equal length.");

  return firstString.split('').filter((nucleotide, index) => { return nucleotide !== secondString[index]; }).length;

};

module.exports = compute;