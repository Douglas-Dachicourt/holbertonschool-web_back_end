export default function cleanSet(set, startString) {
  const str = '';
  const array = Array.from(set);

  if (!startString) {
    return '';
  }

  const filteredArray = array.filter((elem) => elem.startsWith(startString));
  const mappedArray = filteredArray.map((elem) => elem.replace(startString, ''));
  const finalString = str + mappedArray.join('-');

  return finalString;
}
