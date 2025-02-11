def http_status(status):
    match status:
        case 200:
            return'ok'
        case 300:
            return 'good'
        case 400:
            return 'hey buddie'
        case 500: 
            return 'get lost'
        
print (http_status(300))
        