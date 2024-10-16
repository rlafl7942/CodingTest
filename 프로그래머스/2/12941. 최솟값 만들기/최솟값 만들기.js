function solution(A,B){
    var answer = 0;

    A = A.sort((a, b)=> a-b)
    B = B.sort((a, b) => b-a)
    
    while (A.length !=0 && B.length !=0 ){
        answer = answer + A.pop() * B.pop()
    }

    return answer;
}