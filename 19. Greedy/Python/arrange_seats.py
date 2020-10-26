'''
https://www.interviewbit.com/problems/seats/
There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.
An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.
Return minimum value % MOD where MOD = 10000003

Example
Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -
              . . . . x . . x x . . . x . .
Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .
Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -  
    Number of jumps by him =   (6 - 4) = 2

2 - Bring the person sitting at 12th index to 9th index - 
    Number of jumps by him = (12 - 9) = 3

So now the total number of jumps made = 
    ( 2 + 3 ) % MOD = 
    5 which is the minimum possible jumps to make them seat together.
There are also other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.
'''

# move all x almost towards center
class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        
        n = len(A)
        
        M = 10000003
        s = 0
        e = n-1
        
        # find leftmost x
        while s < n and A[s] != 'x':
            s += 1
        
        # find rightmost x
        while e >= 0 and A[e] != 'x':
            e -= 1
            
        moves = 0
        jump = 1                                            # keep track of how many are there before current x
        
        while s < e:
            
            # find or move place of current x towards right till we find next x 
            count = 0
            s += 1
            while s < e and s < n and A[s] != 'x':
                count += 1
                s += 1
            moves += (jump*count)
            
            # find or move place of current x towards left till we find next x 
            count = 0
            e -= 1
            while e > s and A[e] != 'x':
                count += 1
                e -= 1
            moves += (jump*count)
            
            # one x is finished from both sides
            jump += 1
        
        return moves%M
            
        
        
        
        
        
        
        
                    