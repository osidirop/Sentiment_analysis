punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())            
            
            
def strip_punctuation(word):
    
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")

    return word

def get_pos(string):
    
    cnt_count_pos = 0
    
    lst_words = string.split(" ")
    
    for word in lst_words:
        word = strip_punctuation(word).lower()
        
        if word in positive_words:
            cnt_count_pos += 1
     
    return cnt_count_pos 
    
def get_neg(string):
    
    cnt_count_neg = 0
    
    lst_words = string.split(" ")
    
    for word in lst_words:
        word = strip_punctuation(word).lower()
        
        if word in negative_words:
            cnt_count_neg += 1
     
    return cnt_count_neg     
    
###### Read twitters file    


retweet_count = []
reply_count = []
pos_score = []
neg_score = []
net_score = []


fname = "project_twitter_data.csv"
with open(fname,'r') as file_ref:
    lines = file_ref.readlines()
     
    for line in lines[1:]:
        lst = line.strip().split(",")
        
        text = lst[0]
        pos_score.append(get_pos(text))
        neg_score.append(get_neg(text))
        net_score.append(get_pos(text) - get_neg(text))
        
        retweet_count.append(lst[1])
        reply_count.append(lst[2])

fresults = "resulting_data.csv"        
with open(fresults,'w') as file_ref:   
    file_ref.write("Number of Retweets" + ", " +
                   "Number of Replies" + ", " +
                   "Positive Score" + ", " +
                   "Negative Score" + ", " +
                   "Net Score\n")
    
    for i in range(0, len(retweet_count)):   
        file_ref.write(str(retweet_count[i]) + ", " + 
                       str(reply_count[i]) + ", " +
                       str(pos_score[i]) + ", " +
                       str(neg_score[i]) + ", " +
                       str(net_score[i]) + "\n")
     
  
