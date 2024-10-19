function solution(arr)
{
    var answer = [arr[0]];
    let index = 0;
    for (let i=1; i<arr.length; i++){
        if (answer[index] != arr[i]) {
            answer.push(arr[i])
            index += 1
        }
    }
    return answer
}