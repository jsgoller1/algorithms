#!/bin/bash
case_counter= 1
for case in open('A-large.in','r').read().split('\n')[1:-1]:
#for case in open('data.txt','r').read().split('\n')[1:-1]:
    max_shyness, how_many = case.split(" ")
    friends_required = 0
    standing = int(how_many[0])
    shyness = 1
    #print "case: " + how_many
    for num_of in how_many[1:]:
        #print "num_of: "+num_of
        if num_of != '0':
            #print "standing: " + str(standing)
            #print "shyness: " + str(shyness)
            if standing < shyness:
                #print "added friends: " + str(shyness-standing)
                friends_required += shyness - standing
                standing += shyness - standing
            standing += int(num_of)
        shyness += 1

    print 'Case #'+str(case_counter)+":", friends_required
    case_counter+=1
