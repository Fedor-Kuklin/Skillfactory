const obj = {3: 1, minimum: 2, '': 3, abc: 4, new: 5,};
let string = 'minimum'

const string_in_object = (a, b) => {
  for (let key in a) {
    if (key == b) {
        return true;
    }
  }
  return false;
}

let result = string_in_object(obj, string);
console.log(result);
