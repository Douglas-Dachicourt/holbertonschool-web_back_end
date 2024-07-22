export default function getStudentsByLocation(array, city) {
  const newArray = array.filter((student) => student.location === city);
  return newArray;
}
