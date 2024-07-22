export default function hasValuesFromArray(set, array) {
  const newSet = set;

  const verification = array.every((elem) => newSet.has(elem));

  return verification;
}
