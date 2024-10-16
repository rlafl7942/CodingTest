function solution(s) {
    var answer = [];
    var cnt_result = 0;
    var cnt = 0
    while (s !== "1"){
        var cnt_zero = 0;
        for (let j=0; j<s.length; j++) {
            if (s[j] === "0") {
                cnt_zero = cnt_zero + 1
            }
        }
        tmp = (s.length - cnt_zero).toString(2)
        cnt_result = cnt_result + 1
        cnt = cnt + cnt_zero
        s = tmp
    }
    answer.push(cnt_result);
    answer.push(cnt);
    return answer;
}