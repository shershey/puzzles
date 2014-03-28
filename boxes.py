import random

N = 4
K = N/2
S = 100

#Generate all possible combos
def gen_c_recursive(combos,combo,bits,first_loc):
    bits = bits-1
    for loc in range(first_loc,len(combo)-bits):
        new_combo = list(combo)
        new_combo[loc] = 1
        if bits == 0:
            combos.append(new_combo)
        else:
            gen_c_recursive(combos,new_combo,bits,loc+1)

def gen_combos(N,K,fewer_than=True):
    combos = []
    if fewer_than == False:
        min_k = K
    else:
        min_k = 1
    for k in range(min_k,K+1):
        gen_c_recursive(combos,[0]*N,k,0)
    return combos
combos = gen_combos(N,K)

print "Num Combos: %s" % (len(combos))

#Generate all possible strategies
def gen_s_recursive(strats,strat,combos,n):
    for i in range(len(combos)):
        combo = combos[i]
        new_strat = list(strat)
        new_strat.append(combo)
        if n == 1:
            strats.append(new_strat)
            if len(strats) % 100000 == 0:
                print len(strats)
        else:
            gen_s_recursive(strats,new_strat,combos,n-1)
    

def gen_recursive(N,combos):
    strats = []
    gen_s_recursive(strats,[],combos,N)
    return strats

strats = gen_recursive(N,combos)

print "Num Strats: %s" % (len(strats))

#Do Monte Carlo Simulation

probs = []

def calculate_prob(strat,S,N):
    num_dead = 0
    num_alive = 0

    for s in range(S):
        x = range(N)
        random.shuffle(x)
        
        live = True

        for i in range(len(strat)):
            step = strat[i]
            found = step[x[i]] == 1
            if not found:
                num_dead = num_dead+1
                live = False
                break
        if live:
            num_alive = num_alive+1

    return float(num_alive) / (num_alive+num_dead)

for strat in strats:
    prob = calculate_prob(strat,S,N)
    probs.append(prob)



results = zip(probs,strats)
results.sort()
results.reverse()

print results[0:5]
print "refining prob..."
print "refined prob: %f" % (calculate_prob(results[0][1],1000000,N))


    
#Sort
#Print the best few
