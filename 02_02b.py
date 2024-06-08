from collections import deque
# from pprint import pprint

def check_palindrome(word):
    word = deque(word)
    while len(word) > 1:
        if word.pop() != word.popleft():
            return False
    return True

def main():
    #add code here
    return

if __name__ == "__main__":
    # main()
    print(check_palindrome("tacocat"))