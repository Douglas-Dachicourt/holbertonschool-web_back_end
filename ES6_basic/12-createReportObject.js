export default function createReportObject(employeesList) {
  const employees = { ...employeesList };
  const reportObject = {
    allEmployees: employees,
    getNumberOfDepartments(...employeesList) {
      return employeesList.length + 1;
    },
  };

  return reportObject;
}
