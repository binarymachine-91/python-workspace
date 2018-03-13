def even_integers_function(n):
    even_no = []
    for i in range(n):
        if i%2 == 0:
            #even_no.append(i)
            yield i
    #return even_no
print(list(even_integers_function(100)))