#!/opt/python-2.6-64/bin/python
#import datetime
def generator(row):
    row_list=row.split(',') #converts string of words into a list of words
    output = []
    #pat_file=open('log_pat.txt','w')
    
    for item in row_list[8:]:
        item.rstrip('\r')
#time=datetime.datetime(int(row_list[8][0:4]),int(row_list[8][5:7]),int(row_list[8][8:10]),int(row_list[8][11:13]),int(row_list[8][14:16]),int(row_list[8][17:19]))
        #time_new=time+timedelta(minutes=2)
        #pat_file.write('-s '+time[0:10]+'T'+time[11:19]+'+00.00 -e '+time_new[0:10]+'T'+time_new[11:19]+'+00.00' + ' -g '.join(row_list[9:11])+'\n')
        items = item.split(',') #puts a word in a list into a list
        if len(items[0]) != 0:
            output.append([items[0]]) #converts the list of words to list of list of words

    return output