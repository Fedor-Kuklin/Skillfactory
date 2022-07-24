class Appliance {
    constructor(name) {
        this.name = name;
        this.voltage = 220;
        this.deviceTurned = false;
  }
  deviceSwitch(deviceSwitch) {
    if (deviceSwitch === 'on') {
      this.deviceTurned = true;
    } else {
      this.deviceTurned = false;
    }
  }
  energyConsumption(time) {
    if (this.deviceTurned) {
    this.power = this.devicePower;
  } else {
    this.power = 1;
  }
    
  let сonsumption = this.power * time * 0.01;
  console.log(`Устройство ${this.name} за время работы ${time}ч потратил ${сonsumption} кВт*ч `);
  }
}
  class Monitor extends Appliance{
    constructor(name, amperage, size, voltage, deviceTurned)  {
        super(voltage, deviceTurned);
        this.name = name;
        this.size = size + " дюймов";
        this.amperage = amperage;
        this.devicePower = Math.round(this.voltage * amperage)
  }
  getInfo() {
    console.log(`Параметры монитора ${this.name}`);
    for (const key in this) {
      if (typeof this[key] !== "function") {
        console.log(`${key}: ${this[key]}`);
      }
    }
    console.log('\n');
  }
  }

  class Computer extends Appliance{
    constructor(name, amperage, numberCores, voltage, deviceTurned)  {
        super(voltage, deviceTurned);
        this.name = name;
        this.numberCores = numberCores + " ядер центрального процессора";
        this.amperage = amperage;
        this.devicePower = Math.round(this.voltage * amperage)
    }
    getInfo() {
    console.log(`Параметры компьютера ${this.name}`);
    for (const key in this) {
      if (typeof this[key] !== "function") {
        console.log(`${key}: ${this[key]}`);
      }
    }
    console.log('\n');
  }
  }
  const mac = new Computer('Mac Mini', 0.7, 6); // name, amperage, number of CPU cores
  const monitor = new Monitor('Samsung', 0.1, 27); // name, amperage, size (inch)
  
  mac.getInfo();
  monitor.getInfo();
  
  mac.deviceSwitch('off');
  monitor.deviceSwitch('on');
  monitor.getInfo();
  
  mac.energyConsumption(5);
  monitor.energyConsumption(6);