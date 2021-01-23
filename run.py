import random
import timeit

def gen_random_dict(n):
   random.seed(0)
   mydict = {}
   for i in range(n):
       nmbr = random.randrange(1, n, 1)
       mydict[nmbr] = "value "+str(nmbr)
   return mydict

# Remove a key using pop function

def remove_using_pop(dict_input):
    dict_input.pop(1)
    return None

# Remove a key using dek keyword

def remove_using_del(dict_input):
    del dict_input[1]
    return None

# Remove a key using condition

def remove_using_condition(dict_input):
    return {k: v for k, v in dict_input.items() if k != 1}

if __name__ == "__main__":
    func_to_be_tested="remove_using_pop(gen_random_dict(10000))"
    setup_stmt="from __main__ import remove_using_pop, gen_random_dict"
    runtime1 = timeit.timeit(func_to_be_tested, setup=setup_stmt,number=1)
    func_to_be_tested="remove_using_del(gen_random_dict(10000))"
    setup_stmt="from __main__ import remove_using_del, gen_random_dict"
    runtime2 = timeit.timeit(func_to_be_tested, setup=setup_stmt,number=1)
    func_to_be_tested="remove_using_condition(gen_random_dict(10000))"
    setup_stmt="from __main__ import remove_using_condition, gen_random_dict"
    runtime3 = timeit.timeit(func_to_be_tested, setup=setup_stmt,number=1)
    print("Runtime for removing key from Dict:")
    print("\t1) using Pop: {}".format(str(runtime1)))
    print("\t2) using Del: {}".format(str(runtime2)))
    print("\t3) using Condition: {}".format(str(runtime3)))
