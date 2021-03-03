"""

https://leetcode.com/problems/jewels-and-stones/

Problem:

You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".



Understand:
    Whatever characters in Jewels Found in Stones  , return Quantity
    
    Input:
       Jewels =  "aA",  stones = "aAAbcd"
    Output: 3
    
    Input:
        Jewels = "AA" stones = "bbb"
    Output: 0
    
    Input:
        Jewels = "" Stones = "cc"
    Output : 0


Plan:(Mine)
    Loop though characters in Jewels
        Check if X is found in Stones
            if it is found add to return value + 1
    After looping just return the value of count 
       
Plan:(Instructor)

    Input:
       Jewels =  "aA",  stones = "aAAbcd"
       J = {a,A}
       
    1- Make a set of Jewels
    2- Go through  stones and count how many stones are Jewels
    
    
(My plan works. It would do the Job. But compared to the instructors 
solution is not very optimal. WHY? Because search on a string is WORST case O(n),
whereash searching on a set is contant time 0(1). Yeah we would need to create a set
out of the string given in Jewels , so we trading space for better Time Complexity)


"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for x in stones:
            if x in jewels:
                count += 1
        return count
    
class Solution:#PERFORMANT
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(list(jewels))
        count = 0
        for x in stones:
            if x in j:
                count += 1
        return count