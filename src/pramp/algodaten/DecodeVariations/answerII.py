import unittest

def decodeVariations(S):
  """
  @param S: str
  @return: int

  Approach 1: Decode Variations -> DP


  1262

  12 6 2 LFB

  1 2 6 2 ABFB

  1 26 2 AZB

  3 options

  DP 

  input: i is the index of the current letter in word

  output: total combinations or options

  Base Case: DP[len(word)] = 1

  Start Case: DP(0)

  Recursion:

  firstDigit = int(DP[i])

  twoDigit = int(DP[i:i+2])

  if 1 <= firstLetter <= 9:
    total += dp(i+1)

  if 10 <= twoDigit <= 26:

    total += dp(i+2)

  return total


  DP linear or memo DP


  R- O(N ) with memo (2^N) without memo

  S-O(N)

  """
  return VariationsDecoder().decode_variations(S)

class VariationsDecoder:
  
    
  def decode_variations(self,S):
    
    '''
    
    '''
    #hashmap memo cache
    self.dp_memo_cache = {}
    self.dp_memo_cache[len(S)] = 1

    #store S
    self.S = S
    
    #start case with 0
    return self._dp(0)
    
  def _dp(self, letter_index):
    # letter_index is the index of the letter in the word S
    
    #memo
    if letter_index in self.dp_memo_cache:
      return self.dp_memo_cache[letter_index]
    
    #base case
    if letter_index == len(self.S):
      # if we reached the end, we found 1 way to decode
      return 1
    
    #recursion
    total = 0
    
    firstDigit = int(self.S[letter_index])
  
    if 1 <= firstDigit <= 9:
      total += self._dp(letter_index+1)

    if letter_index +1 < len(self.S):
      twoDigit = int(self.S[letter_index:letter_index+2])
      
      if 10 <= twoDigit <= 26:
        total += self._dp(letter_index+2)

    self.dp_memo_cache[letter_index] = total
    return total
  
  
class TestVariationsDecoder(unittest.TestCase):
  
  def test_1(self):
    
    #Arrange
    S = '1'
    
    #Act
    ans=  VariationsDecoder().decode_variations(S)
    
    #Assert
    print(ans)
    self.assertEqual(ans,1)

  def test_1262(self):
    
    #Arrange
    S = '1262'
    
    #Act
    ans=  VariationsDecoder().decode_variations(S)
    
    #Assert
    print(ans)
    self.assertEqual(ans,3)
    
  
#unittest.main(verbosity=2)
  


	

