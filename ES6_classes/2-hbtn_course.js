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
    throw new TypeError("Name must be a string");
  }

  set length(newLength) {
    if (typeof newLength === "number") {
        this._length = newLength;
    }
    throw new TypeError("Length must be a number");
  }

  set students(newStudents) {
    if (typeof newStudents === "string") {
        this._studens = newStudents;
    }
  }
}
