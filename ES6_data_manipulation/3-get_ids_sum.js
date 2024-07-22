export default function getStudentIdsSum(array) {
  const sum = array.reduce((accumulator, student) => accumulator + student.id, 0);
  return sum;
}
