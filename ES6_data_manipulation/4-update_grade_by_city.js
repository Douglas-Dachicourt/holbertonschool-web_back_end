export default function updateStudentGradeByCity(array, city, grades) {
  const filterArray = array.filter((student) => student.location === city);

  const result = filterArray.map((student) => {
    const grade = grades.find((grade) => grade.studentId === student.id);
    return {
      ...student,
      grade: grade ? grade.grade : 'N/A',
    };
  });
  return result;
}
