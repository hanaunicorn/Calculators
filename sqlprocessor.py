def dojob(sql):
    print (sql);

def main():
    # Assert the sorted list is correct
    dojob("create table a (i int);")
    dojob("insert into a values(10);") 
    dojob("insert into a values(2);")
    dojob("select i from a;"); #10,2
    dojob("insert into a values(3);")
    dojob("select i from a;"); #assert to make sure its correct

    dojob("create table b (i int);")
    dojob("insert into b values(1);")
    dojob("select i from b;"); #1
    
if __name__ == "__main__":
    main()
'''
once run this should be the result
10,2
10,2,3
1
'''