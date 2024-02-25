print ("Hello there")
a=10
b=0
try: #method for evaluating scenarios#
    print("This is outer try block")
    try:
        print(a/b)
    except ZeroDivisionError:
        print ("Division by 0")
    finally:
        print ("inside inner finally block")

except Exception:
    print ("General Exception")
finally:
    print ("inside outer finally block")        