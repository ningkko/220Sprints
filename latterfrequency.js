// Yining Hua
// Objective: build a function that takes in a collection of strings, like

//"the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"
//an returns and object pairing each letter with its frequency of occurrence in the input strings:

//{a:1, b:1, c:1, d:2, e:4,...}

function count_letter(list){
let dict_letter = {'a':0};
	for (let i=0;i<list.length;i++){
		for (let letter of list[i]){
			for (let key in dict_letter){
				if(letter == key){
					dict_letter[key]+=1;
				}
				else{
				dict_letter[letter] = 1;
				}
			}
		}
	}
	return dict_letter;
}

list = ["a",'quick','brown','fox','jumps','over','a','lazy','dog'];
let result = count_letter(list);
console.log(result);