"""

https://leetcode.com/problems/uncommon-words-from-two-sentences/


    Understand:
    
    Input:
    A = "This apple is sweet"
    B = " This apple is sour"

    Output = ["sweet", "sour"]

    A ="apple apple" B =" bannana"
    Output:["banana"]

    A="Apple Orange" b="Rambutan Mango"
    Output:["Apple, Orange, Rambutan, Mango"]


    A="Apple Apple" B="Mango Mango"
    Output = []
    
    Plan:(Mine)
    
    A = "This apple is sweet"
    B = " This apple is sour"
    
    A={this, apple, is, sweet}
    B={this, apple , is , sour}
    
    1-Make a set out out input A
    2-Make a set out of input B
    3-Create an empty list to save uncommond words
    4-loop though A, check if A not in B and not repeated in  A
        if true save to empty list
    5-loop trough B , check if B not in A and not repeated in B
        if true save in empty list
    6-return uncommond words list
    
    
    Plan:(instructor)
    Create two dictionaries that contain the word count of both sentences
    Go though each word in both sentences
        check if word has count of 1 and doesn't occur in other sentence
        if it is, then append that word to the result
    return result
    
    

"""


class Solution:#brute force, not optimal does not covert all cases and very bad time complexity
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        listA = A.split()
        listB = B.split()
        
        a_set = set(listA)
        b_set = set(listB)
        
        uncommon_words = []
        for x in listA:
            count = 0
            if x not in b_set:
                uncommon_words.append(x)
            else:
                count += 1
                if count == 2:
                    uncommon_words.append(x)
                    count = 0
                    
                
        for x in listB:
            if x not in a_set:
                uncommon_words.append(x)
            else:
                count += 1
                if count == 2:
                    uncommon_words.append(x)
                    count = 0
        return uncommon_words
        
        
###SOLUTION OPTIMAL      
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        wordCount = defaultdict(int)
        C = A + " "+  B
        listC = C.split(" ")
        
        for word in listC:
            wordCount[word] += 1
        
        res =[]
        
        for word in listC:
            if wordCount[word] == 1:
                res.append(word)
        return res
("""
 I had a general idea of how to tackle the problem. But because Dictionaries were the optimal data structure,
 I guess i am not very familiar with back to back. So I recommend myselt to more basic practices with Dictionaries, sets and tuples
 SO THAT i better know their differences strenghs and weakneses.
 
 The main point i misssed in this exercise. Was not understanding how dictionaries behave when you add a value with on a key
 thats already existing.
 
 
 """)
                