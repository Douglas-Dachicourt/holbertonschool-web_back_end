export default function getListStudentIds(array) {
  if (Array.isArray(array) === false) {
    return [];
  }

  const newArray = array.map((person) => person.id);
  return newArray;
}
