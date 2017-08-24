def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
        
    if (end_quote == -1):
    	return 'Nenhum', 0
    return url, end_quote
                 

url, end_quote = get_next_target('<a href')

print url
print end_quote


