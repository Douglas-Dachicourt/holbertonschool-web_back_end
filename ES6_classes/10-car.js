export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const clone = new this.constructor(this._brand, this._motor, this._color);

    const cloneObj = Object.getOwnPropertySymbols(this);
    for (const symbol of cloneObj) {
      clone[symbol] = this[symbol];
    }

    return cloneObj;
  }
}
