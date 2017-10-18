sentence ="Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Wheres the peck of pickled peppers Peter Piper picked"
word_dict = {}
for word in sentence.split():
 if word not in word_dict:
 	word_dict[word] =1
 else:
 	word_dict[word]+=1
print(word_dict)
print("=========tuples==========")
print(word_dict.items())
print("=========keys==========")
print(word_dict.keys())
print("=========values==========")
print(word_dict.values())


#print("=========from collections import defaultdict==========")
from collections import defaultdict
word_dict = defaultdict(int)
for word in sentence.split():
    word_dict[word]+=1
print(word_dict)

#print("=========from collections import Counter==========")
from collections import Counter

words = sentence.split()
word_count = Counter(words)
print("the no of times peter:",  word_count['Peter'], "jhjhjhkjh")
#print word_dict



print("=========from collections import defaultdict==========")


from collections import defaultdict
user_movie_rating = defaultdict(lambda :defaultdict(int))
# Initialize ratings for Alice
user_movie_rating["Alice"]["LOR1"] =  4
user_movie_rating["Alice"]["LOR2"] =  5
user_movie_rating["Alice"]["LOR3"] =  3
user_movie_rating["Alice"]["SW1"]  =  5
user_movie_rating["Alice"]["SW2"]  =  3
print user_movie_rating


print("=========Tuples==========")

a_tuple = (1,2,'a')
b_tuple =1,2,'c'
print b_tuple[0]
print b_tuple[-1]
ASD=(a_tuple,b_tuple)
print ASD

print("=========Slicing==========")
a =(1,2,3,4,5,6,7,8,9,10)
print a[1:]
print a[1:3]
print a[1:6:2]
print a[:-1]

print min(a), max(a)

if 1 in a:
    print "Element 1 is available in tuple a"
else:
    print "Element 1 is available in tuple a"
    

if 20 in a:
    print "Element 20 is available in tuple a"
else:
    print "Element 20 is not available in tuple a"
    
print("=========from collections import namedtuple==========")   
from collections import namedtuple 
vector = namedtuple("Dimension",'x y z')
vec_1 = vector(2,2,2)
vec_2 = vector(1,0,1)
manhattan_distance = abs(vec_1.x - vec_2.x) + abs(vec_1.y - vec_2.y) \
                            + abs(vec_1.z - vec_2.z)
print "Manhattan distance between vectors = %d"%(manhattan_distance)
    
    
print("=========set creation and manipulation==========")       
    
  # 1.Initialize two sentences.
st_1 = "dogs chase cats"
st_2 = "dogs hate cats"
# 2.Create set of words from strings
st_1_wrds = set(st_1.split())
st_2_wrds = set(st_2.split())
# 3.Find out the number of unique words in each set, vocabulary size.
no_wrds_st_1 = len(st_1_wrds)
no_wrds_st_2 = len(st_2_wrds)
# 4.Find out the list of common words between the two sets.
# Also find out the count of common words.
cmn_wrds = st_1_wrds.intersection(st_2_wrds)
no_cmn_wrds = len(st_1_wrds.intersection(st_2_wrds))
# 5.Get a list of unique words between the two sets.
# Also find out the count of unique words.
unq_wrds = st_1_wrds.union(st_2_wrds)
no_unq_wrds = len(st_1_wrds.union(st_2_wrds))
# 6.Calculate Jaccard similarity
similarity = no_cmn_wrds / (1.0 * no_unq_wrds)
# 7.Let us now print to grasp our output.
print "No words in sent_1 = %d"%(no_wrds_st_1)
print "Sentence 1 words =", st_1_wrds
print "No words in sent_2 = %d"%(no_wrds_st_2)
print "Sentence 2 words =", st_2_wrds
print "No words in common = %d"%(no_cmn_wrds)
print "Common words =", cmn_wrds
print "Total unique words = %d"%(no_unq_wrds)
print "Unique words=",unq_wrds
print "Similarity = No words in common/No unique words, %d/%d = %.2f"

print("=========from sklearn.metrics import jaccard_similarity_score==========")
from sklearn.metrics import jaccard_similarity_score
# 1.Initialize two sentences.
st_1 = "dogs chase cats"
st_2 = "dogs hate cats"
# 2.Create set of words from strings
st_1_wrds = set(st_1.split())
st_2_wrds = set(st_2.split())
unq_wrds = st_1_wrds.union(st_2_wrds)
a =[1 if w in st_1_wrds else 0 for w in unq_wrds] 
b =[ 1 if w in st_2_wrds else 0 for w in unq_wrds]
print a
print b
print jaccard_similarity_score(a,b)    
    
print("====================LIST====================")
# 1.Let us look at a quick example of list creation.
a = range(1,10)
print a
b = ["a","b","c"]
print b
print a[0]
print b[1]

# 4.Slicing is accessing a subset of list by providing two indices. print a[1:3] # prints [2, 3]
print a[1:] 
print a[-1:] 
print a[:-1]  




#5.List concatenation
a = [1,2]
b = [3,4]
print a + b # prints [1, 2, 3, 4]


# 6.    List  min max
print min(a),max(a)


#7. inandnotin 

if 1 in a:
    print "Element 1 is available in list a"
else:
    print "Element 1 is available in tuple a"

# 8. Appending and extending list
a = range(1,10)
print a
a.append(10)
print a


# 9.List as a stack
a_stack = []
a_stack.append(1)
a_stack.append(2)
a_stack.append(3)
print "Add in stack", a_stack
print a_stack.pop()
print "last element deleted 3",a_stack
print a_stack.pop()
print  "second last element deleted 2",a_stack
print a_stack.pop()
print  "first element deleted 1",a_stack    


# 10.List as queue
a_queue = []
a_queue.append(1)
a_queue.append(2)
a_queue.append(3)
print a_queue.pop(0)
print a_queue.pop(0)
print a_queue.pop(0)


# 11.   List sort and reverse
from random import shuffle
a = range(1,20)
shuffle(a)
print a
a.sort()
print a
a.reverse()
print a

# 1.    Let us define a simple list with some positive and negative numbers.
a = [1,2,-1,-2,3,4,-3,-4]
# 2.    Now let us write our list comprehension.
# pow() a power function takes two input and
# its output is the first variable raised to the power of the second.
b = [pow(x,2) for x in a if x < 0]
# 3.    Finally let us see the output, i.e. the newly created list b.
print "Result ",b
    
print "==========================================="
a = {'a':1,'b':2,'c':3}
b = {
     x:pow(y,2) for x,y in a.items()
    }
print b   
print a.items()



print "==================Function===================="

def process(x):
    if isinstance(x,str):
        if(len(x)< 1):
            return x.lower()
        else:
            return x.upper()
    elif isinstance(x,int):
        return x*x
    else:
        return -9
a = (1,2,-1,-2,'D',3,4,-3,'A',1.0,'asd')
b = tuple(process(x) for x in a )
print b



    
    
    
    
    
    
    
    
    
    




