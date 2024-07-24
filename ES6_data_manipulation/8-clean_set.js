export default function cleanSet(set, startString) {
  const str = '';
  const array = Array.from(set);

  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const filteredArray = array.filter((elem) => elem.startsWith(startString));
  const mappedArray = filteredArray.map((elem) => elem.replace(startString, ''));
  const finalString = str + mappedArray.join('-');

  return finalString;
}
