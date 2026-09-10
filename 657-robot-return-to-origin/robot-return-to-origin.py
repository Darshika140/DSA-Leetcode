class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count_L, count_R, count_U, count_D=0,0,0,0
        for i in moves:
            if i=='U':
                count_U+=1
            elif i=='D':
                count_D+=1
            elif i=='L':
                count_L+=1
            else:
               
                count_R+=1
        if (count_L==count_R) and (count_D==count_U):
            return True
        else:
            return False
            

        