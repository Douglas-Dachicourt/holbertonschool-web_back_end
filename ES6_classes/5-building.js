export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error('Cannot instantiate this class directly');
    }

    this._sqft = sqft;

    if (this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }

    if (typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('evacuationWarningMessage must be a function');
    }
  }

  get sqft() {
    return this._sqft;
  }
}
