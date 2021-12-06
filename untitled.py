from PIL import Image, ImageFont, ImageDraw 




def get_word_size(word,font_size):
    """get's the dimansions of any given word for any giving font size"""
    Font=ImageFont.truetype(FONT, font_size)
    return Font.getsize(word)

def font_info(words,font_size): # need to be constante across lines
    """returns all the words dimmansion in pixels plus the longest word's vertical dimansion"""
    max_=0
    word_sizes=[]
    ws_app=word_sizes.append
    for word in words:
        ws_app(get_word_size(word+' ',font_size))
        max_= word_sizes[-1][1] if word_sizes[-1][1]>max_ else max_
    
    return word_sizes,max_+5

def get_lines_len(word_sizes):
    """return the length of all the lines that are 0 weperated"""
    line_lens=[]
    current_line_len=0
    for dim in word_sizes:
        if dim==0:
            line_lens.append(current_line_len)
            current_line_len=0
        else:
            current_line_len+=dim[0]

    return line_lens
    
    
def add_line_ending(word_sizes,lines_endings):
    for line_ending in lines_endings:
        word_sizes.insert(line_ending,0)
    word_sizes.append(0)

def FontSize(text,space,multi_ligne=False):
    """find the biggest font size tha fit's in a given box using brut force"""
    
    width,height=(abs(space[0]-space[2]),abs(space[1]-space[3])) # the box dimantions 
    current_size=min(width,height)+1
    fit=False
    while(not(fit) and current_size>0):
        fit=True
        current_size-=1
        Horizontal_line,vertical_line=0,0 # where the text would be in the box had we chosen this font size
        Word_sizes,min_vertical_disstance =  font_info(text.split(' '),current_size)
        LINE_ENDING=[]
        pos_offset=0
        for pos,word_dims in enumerate(Word_sizes):
            if((Horizontal_line+word_dims[0])<width): #size * current size = letter size
                Horizontal_line+=word_dims[0]
            elif(vertical_line+min_vertical_disstance <height and multi_ligne):
                Horizontal_line=word_dims[0] #go to the start of the line and add the word and remove the space bar 
                vertical_line+=min_vertical_disstance
                LINE_ENDING.append(pos+pos_offset) # make the lines 0 seperated 
                pos_offset+=1
            else:
                fit=False
                break
           
    
    add_line_ending(Word_sizes,LINE_ENDING)
    print(Word_sizes,multi_ligne)
    if current_size==0:
        print('TEXT IS TOO LONG')

    return round(current_size),Word_sizes,(vertical_line//min_vertical_disstance)+1,min_vertical_disstance
    
                
def write_text(picture,pos,text,text_colours,allignment='L',multi_line=False):

    Font_sise,word_sizes,Ligne_nbr,ligne_heights=FontSize(text,pos,multi_line)
    Font = ImageFont.truetype(FONT, Font_sise)
    ligne_lenghts=get_lines_len(word_sizes) # needed to calculate the offset to center text
    

    text=text.split(' ')
    ligne_center_offset = (abs(pos[3]-pos[1])-ligne_heights*Ligne_nbr)//2 * (allignment=='C') # avilable space - nbr_lignes*line_ize //2 and 0 if allignment !=0
    ligne_end_index=-1
    current_word=0
    for current_line in range(Ligne_nbr):
        ligne_end_index+=1

        center_offset=(abs(pos[2]-pos[0])-ligne_lenghts[current_line])//2 * (allignment=='C')# avilabe space - needed space /2 and 0 if allignment !=c

        word_offset=pos[0]+center_offset
        ligne_offset=pos[1]+ligne_heights*current_line+ligne_center_offset
        while(ligne_end_index<len(word_sizes) and word_sizes[ligne_end_index]!=0):
            picture.text((word_offset,ligne_offset), text[current_word], text_colours[current_word], font=Font)
            word_offset+=word_sizes[ligne_end_index][0]
            ligne_end_index+=1
            current_word+=1

Data={'event':'Event is:CENTERED BOYS',
      'name1':'MOHAMED AZIZ BEN NESSIR',
      'rank1':' ML CO LEADO',
      'name2':'name2',
      'rank2':'RANK',
      'date':'32/12/2999',
      'time':'23:23',
      'location':'A207',
      'single':1}
FONT='Basic.ttf'
L_DTL_edge=2000 #make the time date and location alligne on the left
R_DTL_edge=1500 #make the time date and location alligne on the right
event_name_pos=(670,100,L_DTL_edge-150,320)
name_rank_pos=(1210,480,L_DTL_edge,750)
date_pos=(R_DTL_edge,985,L_DTL_edge,1100)
time_pose=(R_DTL_edge,1200,L_DTL_edge,1350)
location_pos=(R_DTL_edge,1430,L_DTL_edge,1570)
single_image_pos=(600,1100)


BLACK=(14,17,17)
GRAY=(173,173,173)



if Data['single']:
   # Poster = Image.open("single.png").convert('RGB')
    #Drawable_poster = ImageDraw.Draw(Poster)
    
    name_colors=[BLACK for i in Data['name1'].split(' ')]+[GRAY for i in Data['rank1'].split(' ')]
    print(name_colors)
    Event_colors=[BLACK for i in Data['event'].split(' ')]
    date_colours=[BLACK for i in Data['date'].split(' ')]
    time_colours=[BLACK for i in Data['time'].split(' ')]
    loc_colours=[BLACK for i in Data['location'].split(' ')]
    
    Poster = Image.open("single.png").convert('RGB')
    Drawable_poster = ImageDraw.Draw(Poster)
    
    
    #Font_sise,Ligne_nbr,word_sizes=FontSize(Data['event'],event_name_pos)
    #Drawable_poster.text((word_offset,ligne_offset), Data['event'], BLACK, font=Event_Font)
    write_text(Drawable_poster,event_name_pos,Data['event'],Event_colors,allignment='C')
    write_text(Drawable_poster,name_rank_pos, Data['name1']+Data['rank1'],name_colors,multi_line=True)
    write_text(Drawable_poster,date_pos, Data['date'],date_colours)
    write_text(Drawable_poster,time_pose, Data['time'],time_colours)
    write_text(Drawable_poster,location_pos, Data['location'],loc_colours)
    #nameNrank=Data['name1']+' '+Data['Rank1']
    #nameNrank_Font = ImageFont.truetype(FONT, FontSize(nameNrank,name_rank_pos))
    #Drawable_poster.text((name_rank_pos[0],name_rank_pos[1]), Data['name1'], Black, font=nameNrank_Font)
    
    #Drawable_poster.rectangle(event_name_pos,outline=BLACK,width=5)
    #Drawable_poster.rectangle(name_rank_pos,outline=BLACK,width=5)
    #Drawable_poster.rectangle(name_rank_pos,outline=BLACK,width=5)
    #Drawable_poster.rectangle(date_pos,outline=BLACK,width=5)
    #Drawable_poster.rectangle(time_pose,outline=BLACK,width=5)
    #Drawable_poster.rectangle(location_pos,outline=BLACK,width=5)
    
    Poster.save("result.PNG")
