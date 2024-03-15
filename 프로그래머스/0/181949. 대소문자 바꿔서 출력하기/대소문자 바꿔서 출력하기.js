const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    // 변환할 값을 저장할 배열 준비
    let arr = [];
    
    // 입력된 문자열을 배열로 만든 뒤, 해당 문자가 대문자면 소문자, 아니라면 대문자로 변경
    str.split('').forEach((k) => {arr.push(k == k.toUpperCase() ? k.toLowerCase() : k.toUpperCase()); });
    
    // 이후 문자배열 합치기
    console.log(arr.join(''));
});