export default function hasValuesFromArray(set, array) {
  const verification = array.every((elem) => set.has(elem));

  return verification;
}
