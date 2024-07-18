export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    if (TypeError) {
      throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
    return this._sqft;
  }
}
