export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const clone = {
      brand: this._brand,
      motor: this._motor,
      color: this._color,
    };

    const cloneObj = Object.getOwnPropertySymbols(this);
    for (const symbol of cloneObj) {
      clone[symbol] = this[symbol];
    }

    return cloneObj;
  }
}
