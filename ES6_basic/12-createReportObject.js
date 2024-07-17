export default function createReportObject(employeesList) {
  const employees = { ...employeesList };
  const reportObject = {
    allEmployees: employees,
    getNumberOfDepartments(employeesList) {
      const numberKey = Object.keys(employeesList).length;
      return numberKey;
    },
  };

  return reportObject;
}
