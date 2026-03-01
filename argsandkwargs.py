def sumof(*args,**kwargs):
    total=sum(args)
    count=len(args)
    avg=total/count

    cr_point=kwargs.get("cr_point",0)

    final=avg+cr_point
    print("Average Score",avg)
    print("Extra Credit",cr_point)
    print("Final Point",final)

sumof(79,78,67,56,cr_point=5)
