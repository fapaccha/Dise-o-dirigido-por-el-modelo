var Vehicle = require('./Vehicle.js');

class CarType1 extends Vehicle {
  constructor() {
    super("car", "super");
  }
}

class CarType2 extends Vehicle {
  constructor() {
    super("car", "deportivo");
  }
}

class CarType3 extends Vehicle {
  constructor() {
    super("car", "combi");
  }
}

class CarType4 extends Vehicle {
  constructor() {
    super("car", "clasico");
  }
}

export{CarType1,CarType2,CarType3,CarType4};

