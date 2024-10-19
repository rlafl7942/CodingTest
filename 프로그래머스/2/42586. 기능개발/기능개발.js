function solution(progresses, speeds) {
    var answer = [];
    var days = [];
    for (let i=0; i<progresses.length; i++) {
        tmp = (100-progresses[i])
        if (tmp%speeds[i] !== 0)
            days.push(Math.floor(tmp/speeds[i])+1)
        else
            days.push(tmp/speeds[i])
    }
    let max_tmp = days[0]
    let cnt = 1
    for (let i=1; i<days.length; i++) {
        if (max_tmp < days[i]) {
            max_tmp = days[i]
            answer.push(cnt)
            cnt = 1
        }
        else 
            cnt = cnt+1
    }
    answer.push(cnt)
    return answer;
}