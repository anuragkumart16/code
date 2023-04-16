/*
// javascript variables
// containers to store data values is called variable
// var number1 = 23 ;
// let number2 = 43 
console.log("here comes the output")
console.log(number1 + number2)

// datatypes in javascript
let string1="this is string"
let string2="this is another string"
console.log(string1,string2)

// objects (key value pairs) of javascript
var marks={
    ravi: 34,
    anurag :64,
    lucky: 92

} 
console.log(marks)

// booleans
let a= true;
let b= false;

console.log(a,b)

// undefined
var c;
console.log(c)
// above statement will return "undefined" as the vlue of the var is not given

var d=undefined;
console.log(d)
// the above statement will also give undefined

// null datatype
var e=null
console.log(e)


// there are two types of datatypes in javascript
// 1. Primitive Datatype : integer,symbol,string,undefined,null,boolean
// 2. Reference datatype: arrays, objects 

// array
var arr=[1,2,3,4,5]
console.log(arr)
// when an array is printed first the length of the array is printed then the array is printed
console.log(arr[0])
console.log(arr[1])
console.log(arr[2])
console.log(arr[3])
console.log(arr[4])
// when negative index is passed into the array it returns undefined
console.log(arr[-1])
// strings can also be passed
let sh=["anurag","bablu"]
console.log(sh)



// operators in javascript
console.log(number1)
console.log(number2)
// + - * / are few operators
console.log(number1+number2)
console.log(number1-number2)
console.log(number1*number2)
console.log(number1/number2)
console.log(number1%number2)


// assingment operator
number1 = number2
console.log(number2)
// this will assign value of number2 to number1
// yahan var ya let use nhi krte hain

// comparison operators
a = 12;
b = 13;
console.log(a>b)
// it will return true or false
*/


/*
// logical and ( ha yeh logic gate wala and hai)
// represented by &&
console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);

// logical or (ha yeh logic gate wala or hai)
// represented by ||
console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);


// logical not
// represented by !
console.log(!true);
console.log(!false);


// comparison operator
// == for equals
// >= for greater than equals to
// <= for smaller than equals to
// > greater than
// < smaller than
*/

// function example
function avg(a,b){
    return (a+b)/2;
}
c = avg(4,6);
console.log(c)

// line 120 me function keyword hai , avg function ka naam hai, bracket me variable define hua hai
// return output c var me daal dega 
// console.log se phir print ho jaaega


// agar output ek integer hai to voh blue se aaega console me
// agar output ek string hai toh voh black se aaega


// if statement
var age=4;
if(age>18){
    console.log("you are not a kid");
}
else if (age==0){
    console.log("you are not born")
}
else{
    console.log("you are a kid");
}




//  for loop
var anu=[1,2,3,4,5,6,7,8,9];
console.log(anu);

for (var i=0 ; i<anu.length;i++){
    console.log(anu[i]);
}
// another way to print elements of an array
// for each
anu.forEach(function(element){
    console.log(element);
})



let j=0;
while (j<anu.length){
    console.log("jai hind");
    j++ ;
}