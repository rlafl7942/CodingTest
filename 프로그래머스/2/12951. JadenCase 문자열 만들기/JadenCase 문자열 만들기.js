function solution(s) {
    var answer = '';
    var tmp = s.split(" ")
    for (let i=0; i<tmp.length;i++) {
        for (let j=0; j<tmp[i].length; j++) {
            if (j==0) {
                if (tmp[i][j] === tmp[i][j].toLowerCase()) {
                    answer = answer + tmp[i][j].toUpperCase()
                }
                else {
                    answer = answer + tmp[i][j]
                }
            }
            else {
                if (tmp[i][j] === tmp[i][j].toUpperCase()) {
                    answer = answer + tmp[i][j].toLowerCase()
                }
                else {
                    answer = answer + tmp[i][j]
                }
            }
        }
        answer = answer + " "
    }
    answer = answer.slice(0, answer.length - 1)
    return answer;
}