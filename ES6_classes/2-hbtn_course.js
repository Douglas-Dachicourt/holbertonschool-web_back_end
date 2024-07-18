export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName === "string") {
        this._name = newName;
    }
  }

  set length(newLength) {
    if (typeof newLength === "number") {
        this._length = newLength;
    }
  }

  set students(newStudents) {
    if (typeof newStudents === "string") {
        this._studens = newStudents;
    }
  }
}
