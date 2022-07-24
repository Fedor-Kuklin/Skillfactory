const obj = {3: 1, minimum: 2, '': 3, abc: 4, new: 5,};

const key_object = (a) => {
  for (let key in a) {
    if (a.hasOwnProperty(key)) {
        console.log(key);
    }
  }
}

key_object(obj);
