function Appliance(name) {
    this.voltage = 220;
    this.deviceTurned = false
  }
  Appliance.prototype.deviceSwitch = function(deviceSwitch) {
    if (deviceSwitch === 'on') {
      this.deviceTurned = true;
    } else {
      this.deviceTurned = false;
    }
  }
  Appliance.prototype.energyConsumption = function(time) {
  if (this.deviceTurned) {
    this.power = this.devicePower;
  } else {
    this.power = 1;
  }
    
  let сonsumption = this.power * time * 0.01;
  console.log(`Устройство ${this.name} за время работы ${time}ч потратил ${сonsumption} кВт*ч `);
  }

  function Monitor(name, amperage, size) {
    this.name = name;
    this.size = size + " дюймов";
    this.amperage = amperage;
    this.devicePower = Math.round(this.voltage * amperage)
  }

  Monitor.prototype = new Appliance();
  Monitor.prototype.getInfo = function() {
    console.log(`Параметры монитора ${this.name}`);
    for (const key in this) {
      if (typeof this[key] !== "function") {
        console.log(`${key}: ${this[key]}`);
      }
    }
    console.log('\n');
  }

  function Computer(name, amperage, numberCores) {
    this.name = name;
    this.numberCores = numberCores + " ядер центрального процессора";
    this.amperage = amperage;
    this.devicePower = Math.round(this.voltage * amperage)
  }
  Computer.prototype = new Appliance();
  Computer.prototype.getInfo = function() {
    console.log(`Параметры компьютера ${this.name}`);
    for (const key in this) {
      if (typeof this[key] !== "function") {
        console.log(`${key}: ${this[key]}`);
      }
    }
    console.log('\n');
  }

  const mac = new Computer('Mac Mini', 0.7, 6);
  const monitor = new Monitor('Samsung', 0.1, 27);
  
  mac.getInfo();
  monitor.getInfo();
  
  mac.deviceSwitch('off');
  monitor.deviceSwitch('off');
  monitor.getInfo();
  
  mac.energyConsumption(5);
  monitor.energyConsumption(6);
