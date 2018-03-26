#!/opt/python-2.6-64/bin/python

config_f=open('config.cfg','r') 
evr_columns=[]
for line in config_f:  #Reading the config file
    row=line.rstrip('\r\n')
    evr_columns.append('evr_evoucherimage.'+row) #Building the query
    
SQL_search_strg=', '.join(evr_columns) #Converts the list to a string of words delimited by commas
print SQL_search_strg
config_f.close()