var last = 0;
var first = 1;
while (first < 4e6){
	var aux = first;
    first  = first+last;
    last = aux;
}
console.log(last);
