// Installed npm packages: jquery underscore request express
// jade shelljs passport http sys lodash async mocha chai sinon
// sinon-chai moment connect validator restify ejs ws co when
// helmet wrench brain mustache should backbone forever debug jsdom

var _ = require('underscore');

var evens = _.reject([1, 2, 3, 4, 5, 6], (num) => num % 2 != 0);

console.log("Evens");
console.log(evens);

const abc = (name) => {
  console.log(`hello ${name}`)
}

const sample = (argument1, callback1) => {
  if(argument1 === true) {
    callback1("pete")
  } else {
    console.log("argument1 was false")
  }
  callback1("aki")
}

sample(false, abc)

// example of using callbacks in different scenarios to reduce repetitive code
const good_function = async (arg1, errorCallback, successCallback) => {
  result = await axios.get(arg1)
  .then(response => successCallback())
  .catch(error => errorCallback())
  return result
}

// examples of same result using async/await vs not.
const withoutAsync = () => {
  // our goal is to console.log("akimi") when the response is done
  axios.get(url)
  .then(url2 => {
    axios.get(url2)
    .then(url3 => {
      axios.get(url3)
      .then(url4 => {
        console.log(url4)
      })
    })
    .catch(error2)
  })
  .catch(error => .. )
}

const withAsync = async () => {
  // our goal is to console.log("akimi") when the response is done
  const result = await axios.get(url) // ->5 seconds
  .then(response => ..)
  .catch(error => .. )
  const url2 = await axios.get(result) // -> 10 seconds
  const url3 = await axios.get(url2) // -> 10 seconds
  // total time is now 25 seconds to get here
  console.log("akimi")
}
// Promise.all(promise1, promise2, promise3...) - > concurrency

// nesting -> dependency -> does it depend on the result before? yes/no
// speed bottleneck -> if !dependent then longest duration = total time

closures -> function in a function -> the real question is scope // .bind() es5

react / other FE frameworks -> 
  async await (es5 codebases) -> hooks, setState changes that are depended on 
  functional component
    useEffect()
      useContext()
      




