function solution(s) {
    var answer = '';
    var tmp = s.split(" ").map(x => +x);
    let max = tmp[0]
    let min = tmp[0]
    for (let i=0; i<tmp.length; i++){
        if (tmp[i] > max) {
            max = tmp[i]
        }
        if (tmp[i] < min) {
            min = tmp[i]
        }
    }
    answer = `${min} ${max}`
    return answer;
}