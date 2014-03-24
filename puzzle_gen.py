import sys
from optparse import OptionParser

setup = '''
Hey %s, %s, and %s.  You have numbers on your forheads.  
I promise they're positive integers.  One of them is the sum 
of the other two.  Why don't you go around in a circle and tell
us what your number is if you can infer it with your genius logic
brains.
'''

if __name__ == "__main__":
    
    parser = OptionParser()
    parser.add_option("-n","--num_answers",dest="num_answers",
                      default=4,type="int")
    parser.add_option("-m","--multiplier",dest="multiplier",default=5,
                      type="int")
    parser.add_option("-a","--answer",dest="answer",action="store_true")
    (options,args) = parser.parse_args()
    
    multiplier = options.multiplier
    num_answers = options.num_answers

    if num_answers < 2:
        raise Exception('num_answers must be 2 or greater')

    names = ['Alice','Betty','Carol']

    print setup % (names[0],names[1],names[2])

    numbers = [multiplier,multiplier,multiplier*2]

    ignorance = ": I dunno."
    print names[0] + ignorance

    for i in range(1,num_answers):
        name_index = i%len(names)
        name = names[name_index]

        if i == num_answers-1:
            print "%s: By jove, my number is %d!" % (name,numbers[2])
        else:
            print name + ignorance
            numbers = numbers[1:] + [sum(numbers[1:])]


    print "\nWhat are the other two numbers?"

    if options.answer:
        print ""
        for i in range(0,3):
            print "%s: %d" % (names[name_index-i], numbers[2-i])
        print "Obviously!"

'''
Proofish kinda thing:

Let's say we have three people:
p_0
p_1
p_2

we have three values associated with those people:

v_0
v_1
v_2

Using induction

base case - state 0
if:
   2x, x, x -> Person 0 knows right away they are 2x since 0 is 
   not a valid choice.  
else:
   p_0 passes

state n+1 given state n
What person is guessing: p_(n+1) = (n+1) mod 3
v_(n+1) is either the sum of the other two or the person before her 
(mod 3) is the sum.
If v_n is the sum
  The person before would have declared their number
Therefore, if the person before passed
  p_n+1 can declare her number as v_n + v_(n-1)

After the inductive step, we can generate puzzles of arbitrary length.

There's one additional tweak.  The original puzzle starts with state 0 being:
x, 2x, x
This is mostly the same but the first person passes once before everything 
begins.

'''
