def main():
    try : 
        a = int(input('Enter the number :'))
        print(a)
        return
    except Exception as e: 
        print(e)
        return
    finally: #Even if you are returning the above value the finally block will still run.
        print('hey you are finally here')
            
main()
            