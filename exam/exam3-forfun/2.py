def product0(num_list):
    product2=0
    x2,y2,z2=0,0,0
    for i in range (0,len(num_list)-2):
        for o in range (i+1,len(num_list)-1):
            for p in range (o+1,len(num_list)):
                x,y,z=num_list[i],num_list[o],num_list[p]
                product1=x*y*z
                if product2==0:
                    product2=product1
                    x2,y2,x2=x,y,z
                if product2<product1:
                    product2=product1
                    x2,y2,z2=x,y,z
    print(product2,x2,y2,z2)
product0([1,2,3,-3,-2,-19,2,3,4,4,33])