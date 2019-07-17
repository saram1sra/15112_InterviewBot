#Photographs Used : http://www.officelovin.com/wp-content/uploads/2016/01
#/ragged-edge-london-office-6.jpg
#http://wallpapercave.com/wp/YfprI0N.jpg
#http://hdwallsize.com/wp-content/uploads/2013/05/Green-Background-Abstract
#-Wallpaper-HD.jpg
#http://previews.123rf.com/images/tomwang/tomwang1111/tomwang111100023/11173418
#-Pretty-asian-business-woman-at-office-desk-with-computer-Stock-Photo.jpg

from Tkinter import *
import random
from APIPersonalityInsight import *
from speechtotextGoogle import *
from texttoSpeechGoogle import *
from getData import *
from WEBCRAWLER import *
from Comparison import *
from PIL import Image
############################
##Best Match
#############################
def randomComp(data) :
    data.z = random.choice(range(0,741))
    for i in data.titles[data.z:data.z+10]:
        txt = findJob(i)
        data.textJobnames += [txt] 
def bestMatch(data):#finds other jobs for which your personality is a match
    
    jobnames = data.titles  
    currAvg = data.avg
    totalComp = []
    betterJobs = []
    for i in range(len(data.textJobnames)):
        comparisons = 0
        jobname = jobnames[data.z+i]
       # print(jobname)
        txt = findJob(jobname) 
        callPersonalityInsights(txt, jobname)
        a,b,c = getData(jobname+".json")
        things = [a[0],a[1],b]
        for ele in range(len(things)) :
            #print(candidateData[ele])
            match,res = Comparing(data.candidatedata[ele], things[ele])
            comparisons += res
           # print(ele) 
        totalAvg = comparisons/len(things)
        totalComp += [(jobname,totalAvg)]
    for element in totalComp :
         name,avg = element       
         if currAvg < avg : 
                betterJobs += [element]
    data.bestJobs  = betterJobs
#############################
##Pages
##############################
def drawIndex(canvas,data) :#INDEX PAGE
    l,b = 50,25
    margin = b +10
    cx,cy = data.width//2, data.height//2
    #background
    canvas.create_rectangle(0,0, data.width, data.height, fill ="turquoise")
    image = canvas.data["image"]
    imageSize = ( (image.width(), image.height()) )
    
    canvas.create_image(canvas.width//2, canvas.height//2, image=image)
    #title
    canvas.create_text(cx, cy - 4*margin, text = "Interview Bot",
    font = "Times 30 bold")
    #start button
    canvas.create_rectangle(cx-l,cy-b-margin,cx +l,cy+b-margin, fill ="pink",
                                                                    width = 5)
    canvas.create_text(cx,cy-margin,text = "BEGIN", font = "Times 15 bold")
    data.indexbounds = (cx-l,cy-b-margin,cx +l,cy+b-margin)
    #admin button
    canvas.create_rectangle(cx-l,cy-b +margin,cx +l,cy+b+margin, fill ="pink",
                            width = 5)
    canvas.create_text(cx,cy +margin,text = "ADMIN",font = "Times 15 bold")
    data.adminbounds = (cx-l,cy-b +margin,cx +l,cy+b+margin)
    
def drawInstruct(canvas,data) :#INSTRUCTION PAGE
    image = canvas.data["instruct"]
    imageSize = ( (image.width(), image.height()) )
    
    canvas.create_image(canvas.width//2, canvas.height//2, image=image)
    instructions ="""
        1. Please speak slowly and clearly\n\n
        2. Do not panic if the interviewer asks you to repeat your answer.\n\n
        3. Click START when you are ready and press "s"\n\n
        4. BEST OF LUCK!
                     """
    margin = 30
    border = 25
    canvas.create_text(margin, margin, text = "INSTRUCTIONS",
                            anchor = "w",font="Times 20 bold underline")
    canvas.create_line(0, 2*margin, data.width, 
                                        2*margin, fill = "black")
    canvas.create_text(margin, 9*margin,  
                        anchor = "w", text = instructions,font="Times 18 bold ")
    width = 4*margin
    #home button
    canvas.create_rectangle(data.width - width, data.height - 2*margin ,
            data.width - border, data.height - border, fill = "pink")
    centeringx1,centeringy = 1.7,1.5
    canvas.create_text(data.width - width/centeringx1, data.height
     - centeringy* margin, text = "HOME")
    #start interview button
    canvas.create_rectangle(data.width - 2*width , data.height - 2*margin ,
     data.width - width - border,data.height - border, fill = "pink")
    centeringx2 = 1.25
    canvas.create_text(data.width - 2*width/centeringx2 , data.height 
    - centeringy*margin, text = "START")
    #bounds of the button
    data.instructboundshome = (data.width - width, data.height 
    - 2*margin ,data.width - border, data.height - border)
    data.instructboundsstart = (data.width - 2*width ,
     data.height - 2*margin ,data.width - width - border,data.height - border)

def drawInterview(canvas,data) :#INTERVIEW PAGE
    margin =100
    offset = 60
    canvas.create_rectangle(0,0,data.width, data.height, fill ="black")
    image = canvas.data["interviewer"]
    imageSize = ( (image.width(), image.height()) )
    canvas.create_image(canvas.width//2, canvas.height//2 - offset, image=image) 
    #subtitles
    if data.interviewQ1 :
        canvas.create_text(data.width//2,data.height - margin, 
        text = data.question1, fill = "white", font= "Times 20")
    elif data.interviewQ2 :
        canvas.create_text(data.width//2,data.height - margin, 
        text = data.question2, fill = "white", font= "Times 20")
    elif data.interviewQ3 :
        canvas.create_text(data.width//2,data.height - margin, 
        text = data.question3, fill = "white", font= "Times 20")
    elif data.interviewQ4 :
        canvas.create_text(data.width//2,data.height - margin, 
        text = data.question4, fill = "white", font= "Times 20")
    
       
    
def drawResultButton(canvas,data) :#Result Button on Interview Page
    margin = 30
    border = 25
    width = 4*margin
    centeringx1,centeringy = 1.7,1.5
    canvas.create_rectangle(data.width - width, data.height - 2*margin ,
                             data.width - border, data.height - border, 
                             fill = "pink",outline = "white") 
    canvas.create_text(data.width - width/centeringx1, data.height - 
    centeringy* margin, text = "RESULT")
    data.resultbounds = (data.width - width, data.height - 
    2*margin ,data.width - border, data.height - border)

def drawResult(canvas,data) :#RESULT PAGE 1
    canvas.create_rectangle(0,0,data.width, data.height, fill = "slategray4")
    margin = 50
    canvas.create_text(data.width//2, margin,
                                text = "RESULTS", font = "Times 20 bold")
    personality,needs,values=getData("comparison.json")#data.candidate +".json"
    first,second = personality[0], personality[1]
    data.comparisondata = []
    comparisonData = {}
    things = [first,second,needs]
    
    for dictionary in things :
        comphell = {}
        for key in dictionary :
            comphell[key] = dictionary[key]
            comparisonData[key] = dictionary[key]
        data.comparisondata += [comphell]
    personalitycomp, needscomp,valuescomp = getData("candidate.json")
    firstcomp, secondcomp = personalitycomp[0], personalitycomp[1]
    things1 = [firstcomp, secondcomp,needscomp]
    
    data.candidatedata = []
    candidateData = {}
    for dictionary1 in things1 :
            candhell = {}
            for key1 in dictionary1 :
                candhell[key1] = dictionary1[key1]
                candidateData[key1] = dictionary1[key1]
            data.candidatedata += [candhell]
    match,data.avg = Comparing(candidateData,comparisonData)
    canvas.create_text(data.width//2, 3*margin, 
    text = "You are a %s match to the job" % data.avg,
    font = "Times 15" )
    margin = 30
    border = 25
    width = 4*margin
    centeringx1,centeringy = 1.7,1.5
    canvas.create_rectangle(data.width - width, data.height - 2*margin ,
    data.width - border, data.height - border, fill = "pink",outline = "white") 
    canvas.create_text(data.width - width/centeringx1, 
    data.height - centeringy* margin, text = "DETAILS")
    data.result1bounds = (data.width - width, data.height - 2*margin ,
    data.width - border, data.height - border)
    
    data.candidateList = []
    for dictionary1 in things1 :
            candidatedata = {}
            for key1 in dictionary1 :
                candidatedata[key1] = dictionary1[key1]
            data.candidateList+= [[candidatedata]]
    canvas.create_text(data.width//2, 4*margin, 
    text = "To conside similar and better suited jobs press 'r', your match to the job is also displayed:" )
    i=0
    if data.bestMatch:
        for ele in data.bestJobs :
            name, match = ele
            name = name[:name.index("cover")-1]
            if match >= 100 :
                canvas.create_text(data.width//2,(8+i)*margin,
                text = str(name) +" : "+ str(match),
                 fill= "red",font = "Times 15 ")
            else :    
                canvas.create_text(data.width//2,(8+i)*margin,
                text = str(name) +" : " + str(match), 
                fill= "black", font = "Times 15 ")
            i+=1
    
    #canvas.create_text(margin,margin, text = "Personality",
    #anchor = "w",font="Times 12 bold underline")
    #need to create bar chart to properly display results
    #Candidated 
    
    
def drawResult1(canvas, data) :#RESULT PAGE 2
    canvas.create_rectangle(0,0,data.width, data.height, fill = "slategray4")
    maxHeight = 150
    margin = 50
    #print(data.candidatedata, data.comparisondata)
    canvas.create_text(data.width//2, margin, 
                                text = "DETAILS", font = "Times 20 bold")
    first,second,needs =( data.comparisondata[0],data.comparisondata[1],
    data.comparisondata[2])
    i = 0
    offset = 60
    for k in first :
            #print(k,i)
            #right, left = margin +(i+1)*10 , margin +(i+2)*10 
            x1 = data.width//6 -offset
            x0 = x1 -maxHeight*first[k][0]
            i+=4
            y0,y1 = margin +(i)*10 , margin +(i+2)*10
            #top, bottom = data.height -maxHeight*d[k][0] -200,data.height- 100
            #canvas.create_rectangle( top,right,bottom,right , fill = "red")
            canvas.create_rectangle( x0,y0,x1,y1 , fill = "gold")
            canvas.create_text(x0 -offset/3,(y0+y1)//2, 
                                            text = "%.2f"%(first[k][0]*100))
            key = unicodedata.normalize('NFKD', k).encode('ascii','ignore')
            canvas.create_text(data.width//6 , (y0 +y1)//2, text = key)
    i=0
    for l in second : 
            x1 = data.width//2 - offset
            x0 = x1 -maxHeight*second[l][0]
            i+=2.2
            y0,y1 = margin +(i)*10, margin +(i+2)*10
            #top, bottom = 
            #(data.height - maxHeight*second[l][0] -200,data.height - 100)
            #right, left = margin +(i+1)*10 , margin +(i+2)*10 
            #canvas.create_rectangle( right,top,left,bottom , fill = "gold")
            canvas.create_rectangle(x0,y0,x1,y1 , fill = "gold")
            canvas.create_text(x0 -offset/2,(y0+y1)//2, 
                                    text = "%.2f"%(second[l][0]*100))
            key = unicodedata.normalize('NFKD', l).encode('ascii','ignore')
            canvas.create_text(data.width//2 , (y0 +y1)//2, text = key)
    i =0         
    for m in needs : 
            x1 = data.width//2 +data.width//2.8-offset
            x0 = x1 -maxHeight*needs[m][0]
            i+=4
            y0,y1 = margin +(i)*10 , margin +(i+2)*10 
            #top, bottom = data.height - maxHeight*d[k][0]-200,data.height- 100
            #canvas.create_rectangle( top,right,bottom,right , fill = "red")
            canvas.create_rectangle( x0,y0,x1,y1 , fill = "gold")
            canvas.create_text(x0 -offset/2,(y0+y1)//2, 
                                                text = "%.2f"%(needs[m][0]*100))
            key = unicodedata.normalize('NFKD', m).encode('ascii','ignore')
            canvas.create_text(x1 + offset//1.5 , (y0 +y1)//2, text = key)
    #person = dicttostr(first) + dicttostr(second
    #cneeds = dicttostr(needs)
    #total = person + cneeds
    #print(total)
    #canvas.create_text(margin, 6*margin,  anchor = "w", text = total)
    #personalitycomp, needscomp,valuescomp = getData("candidate.json")
    firstcomp, secondcomp,needscomp = (data.candidatedata[0], 
    data.candidatedata[1],data.candidatedata[2])
    #things1 = [firstcomp, secondcomp,needscomp]
    #candidatedata = dict()
    #candidateList = []
    #for dictionary1 in things1 :
     #       for key1 in dictionary1 :
      #          candidatedata[key1] = dictionary1[key1]
      #      candidateList += candidatedata 
    z = 0
    for k1 in firstcomp :
            #print(k1)
            #right1, left1 = margin +(z+1)*10 + 
            #offset1 , margin +(z+2)*10 +offset1
            x_0 = data.width//6 + offset
            x_1 = x_0 + maxHeight*firstcomp[k1][0]
            z+=4
            y_0,y_1 = margin +(z)*10 , margin +(z+2)*10
            #top1, bottom1 = data.height - maxHeight*d1[k1][0] -150,
            #data.height - 150
            #canvas.create_rectangle( right1 ,
            #top1, left1,bottom1 , fill = "blue")
            canvas.create_rectangle( x_0,y_0,x_1,y_1 , fill = "turquoise") 
            canvas.create_text(x_1 +
            offset//3,(y_0+y_1)//2, text = "%.2f"%(firstcomp[k1][0]*100))
    z = 0
    for l1 in secondcomp :        
            
            #print(k1)
            #right1, left1 = margin +(z+1)*10 + offset1 , 
            #margin +(z+2)*10 +offset1
            x_0 = data.width//2 + offset
            x_1 = x_0 + maxHeight*secondcomp[l1][0]
            z+=2.2
            y_0,y_1 = margin +(z)*10 , margin +(z+2)*10
            #top1, bottom1 = data.height - maxHeight*d1[k1][0] 
            #-150,data.height - 150
            #canvas.create_rectangle(right1 ,top1,left1,bottom1 , fill = "blue")
            canvas.create_rectangle( x_0,y_0,x_1,y_1 , fill = "turquoise") 
            
            canvas.create_text(x_1 +offset//3,
            (y_0+y_1)//2, text = "%.2f"%(secondcomp[l1][0]*100))
    z = 0
    for m1 in needscomp :        
            
            #print(k1)
            #right1, left1 = margin +(z+1)*10 + offset1 , margin +(z+2)*10 
            #+offset1
            x_0 = data.width//2 +data.width//2.8 + offset//3
            x_1 = x_0 + maxHeight*needscomp[m1][0]
            z+=4
            y_0,y_1 = margin +(z)*10 , margin +(z+2)*10
            #top1, bottom1 = data.height - maxHeight*d1[k1][0]-150,
            #data.height- 150
            #canvas.create_rectangle( right1 ,top1, left1,bottom1 , fill = "blue")
            canvas.create_rectangle( x_0,y_0,x_1,y_1 , fill = "turquoise") 
            
            canvas.create_text(x_1 +offset//3,
            (y_0+y_1)//2, text = "%.2f"%(needscomp[m1][0]*100))        
            
    canvas.create_text(margin,margin,anchor= "w", 
    text = "Required JOB\n Personality", font = "Times 13 bold", fill = "gold")
    canvas.create_text(data.width -margin, margin,anchor ='e',
    text = "CANDIDATE\n Personality", font = "Times 13 bold",fill = "turquoise")
    
    #totalcomp = dicttostr(firstcomp) + 
    #dicttostr(secondcomp) +dicttostr(needscomp)
    #row,col = len(data.boardResult),len(data.boardResult[0])
    #for r in range(row) :
     #       for c in range(col) :
                #print(r,c)
      #          drawCellForResult(canvas, data, r, c)
    #print(len(firstcomp) + len(secondcomp)+ len(needscomp))
    #canvas.create_text(10*margin, 6*margin,  anchor = "w", text = totalcomp)
    
def dicttostr(d,p ="") :
    for key in d :
        value = d[key]
        p += ( "%s : %s , sampling error : %s \n") % (key, value[0], value[1])
    return p
    
def formatStr(title) :#removing extra elements and formatting string
    result = []
    for s in title :
        s = s.split("-")
        res = ""
        for k in s :
           #print(k)
           temp = k[0]
           res += (str.upper(temp) + k[1:] +" ")
        #res = res[:res.index("Cover")]
        res = res[:res.find(" Cover")]
        result += [res]
    index,index2 = result.index("#wrapper"), result.index('Resources')
    result = result[index2+1:index]
    #print(result)
    return result

def AdminBounds(data) :
    parser = URLS()
    data.titles,data.urls  = parser.getURLS(
    'http://www.jobhero.com/sample-cover-letters/',"http://www.jobhero.com" ) 
    data.nameTitles = formatStr(data.titles)
    i = 0
    row,col = len(data.board),len(data.board[0])
    for r in range(row) :
            for c in range(col) :
                #print(r,c)
                
                x0 = data.boardMargin +  c * data.cellSidel
                x1 = data.boardMargin + (c+1) * data.cellSidel
                y0 = data.boardMargin +  data.startingRight + r * data.cellSideb
                y1 = data.boardMargin +data.startingRight+ (r+1) *data.cellSideb 

                data.adminBounds+= [(i,(x0,y0,x1,y1))]
                i+=1
    #print(data.adminBounds)
    
def drawAdmin(canvas, data) :
    
    margin = 50
    othermarg = 50
    canvas.create_rectangle(0,0,data.width, data.height, fill = "lightblue")
    canvas.create_rectangle(0,0, data.width, data.height, fill ="turquoise")
    image = canvas.data["adminImage"]
    imageSize = ( (image.width(), image.height()) )
    canvas.create_image(canvas.width//2, canvas.height//2, image=image)
    canvas.create_text(margin,margin//2,
        text = "Please select the job for interviewing", 
                                        anchor = "w",font = "Times 20 bold")
    
    
    #length = len(nameTitles)
   #taken from class notes
    i = 0
    row,col = len(data.board),len(data.board[0])
    for r in range(row) :
            for c in range(col) :
                #print(r,c)
                
                drawCell(canvas, data, r, c,data.nameTitles[i])
                
                i += 1
    #print(data.adminBounds) 
    canvas.create_rectangle(data.width//2, data.height - margin ,
            data.width//2 + 2*margin ,data.height - margin//4, fill = "pink")          
    canvas.create_text(data.width //2 + margin, 
                data.height - (margin +margin//3)//2, text = "HOME")
    data.adminbutton = (data.width//2, data.height - margin,
                data.width//2 + 2*margin ,data.height - margin//4)            
                

def drawCell(canvas, data,row, col,msg) :#remembered from HW6 scroller
    x0 = data.boardMargin + data.startingTop + col * data.cellSidel
    x1 = data.boardMargin + data.startingTop + (col+1) * data.cellSidel
    y0 = data.boardMargin +  row * data.cellSideb
    y1 = data.boardMargin +  (row+1) * data.cellSideb 
    #msg = "(" + str(row) +","+ str(col)+")"
    boardRowColRight = x0+data.cellSidel//2
    boardRowColTop = y0+data.cellSideb//2
    if data.click[0] :
        x_0,y_0,x_1,y_1 = data.clickbounds
        canvas.create_rectangle(x_0,y_0,x_1,y_1,fill = "cyan3")
        canvas.create_text(x_0+data.cellSidel//2,
                y_0+data.cellSideb//2,text = data.nameTitles[data.click[1]],
                fill = "white", font = "Times 15 bold")
    canvas.create_text(boardRowColRight,boardRowColTop, text = msg,
    fill = "white", font = "Times 15 bold")
    
#scroll sideways through admin page
def doMove(drow, dcol, data ) :#moving/scrolling through shifting the topmost.
    #print(1)
    #if 
    data.startingTop -= dcol #rigthmost point
    #data.startingRight -= drow  
    

#for admin page            
def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a    
        
#######################################################################################################################################
##Interview
######################################################################################################################################
def startInterview(data) :#INTERVIEW
    
    data.question1 = "Tell me about yourself, your passions, your interests; and how you came to be who you are now?"
    data.interviewQ1 = True
    #canvas.create_text(data.width//2,data.height//2, text = data.question1, 
    #fill = "white", font= "Times 20")
    texttospeech(data.question1, "question1")
    ans1 =speechtotext(time = 2*3600)
    data.interviewQ1 = False
    
    #canvas.create_rectangle(0,0,data.width, data.height, fill ="black") 
    data.question2 = "Why should we choose you for this position, instead of your peers ?"
    data.interviewQ2 = True
    #canvas.create_text(data.width//2,data.height//2, text = data.question2, 
    #fill = "white", font= "Times 20")
    texttospeech(data.question2, "question2")
    ans2 = speechtotext(time= 2*3600)
    data.interviewQ2 = False
    
    #canvas.create_rectangle(0,0,data.width, data.height, fill ="black") 
    data.question3 = "What do you consider your academic and non-academic accomplishments ?"
    data.interviewQ3 = True
    #canvas.create_text(data.width//2,data.height//2, text = data.question3, 
    #fill = "white", font= "Times 20")
    texttospeech(data.question3, "question3")
    ans3 = speechtotext(time= 2*3600)
    data.interviewQ3 = False
    
    #canvas.create_rectangle(0,0,data.width, data.height, fill ="black") 
    data.question4 = "Is there anything else you would like to add? If not and when you finish press 'r'" 
    data.interviewQ4 = True
    #canvas.create_text(data.width//2,data.height//2, text = data.question4, 
    #fill = "white", font= "Times 20")
    texttospeech(data.question4, "question4")
    ans4 = speechtotext(time= 2*3600)
    data.interviewQ3 = False
    
    totalans = ans1 +ans2 + ans3 + ans4
    #strtojson(totalans)
    #@TODO : IMPORTING API PERSONALITY INSIGHTS
    #filename = "profile1.json "
    data.candidatefile = "candidate"
    callPersonalityInsights(totalans,data.candidatefile)
    msg = open("C:/Users/saram/Dropbox/Classes/Sem1/15112/TermProject/Test code/testingFile.txt","r+")
    MyText =msg.read()
    dalpha = callPersonalityInsights(MyText, "candidate")
    

#################################################################################################################################################
def init(data):
    # load data.xyz as appropriate
    data.startspeechtext = False
    data.starttextspeech = False
    data.indexpage, data.admin, data.instruct  =True,False,False
    data.interview, data.result = False,False
    data.resultpage1 = False
    #start bounds to make sure that they are not on board before we assign it
    data.indexbounds,data.instructboundshome,data.instructboundsstart = (
                (-1,-1,-1,-1),(-1,-1,-1,-1),(-1,-1,-1,-1))
    data.getresultbutton = False
    data.boardMargin, data.startingTop, data.cellSidel, data.cellSideb = (50, 
                                                                    0, 300, 50)
    data.startingRight = 0
    data.board = make2dList( 13,int(765/13)  )
    data.boardResult = make2dList(40,13)
    data.interviewQ1,data.interviewQ2,data.interviewQ3,data.interviewQ4 = (False
    ,False,False,False)
    data.adminBounds = []
    data.click = (False,0)
    data.textJobnames = []
    data.bestMatch = False
    
def initCanvas(canvas):
    canvas.width = canvas.winfo_reqwidth()-4
    canvas.height = canvas.winfo_reqheight()-4
    image = PhotoImage(file="officespace.gif")
    image = image.subsample(2,2)
    canvas.data["image"] = image
    adminImage = PhotoImage(file="adminbackground.gif")
    canvas.data["adminImage"] = adminImage
    interviewer = PhotoImage(file="interview.gif")
    canvas.data["interviewer"] = interviewer
    instruct = PhotoImage(file="rug.gif")
    canvas.data["instruct"] = instruct
    
def inBounds(x,y,bounds) :#check if (x,y) of click is in bounds of aomething
    left,top,right,bottom = bounds
    return ( x >= left and x <=  right and y <= bottom and y >=  top )
    
def mousePressed(event, data):#Button Clicks
    # use event.x and event.y
    #instruct page
    if data.indexpage :
        if inBounds(event.x,event.y, data.indexbounds) :
             data.indexpage,data.instruct = False, True
        elif inBounds(event.x, event.y, data.adminbounds) :
            data.admin,data.indexpage = True,False  
    #interview page/ index page
    elif data.instruct :
        #back home
        if inBounds(event.x, event.y, data.instructboundshome) :
             data.indexpage,data.instruct = True, False
        #starting interview
        elif inBounds(event.x, event.y,data.instructboundsstart) :
             data.instruct, data.interview = False, True
    #result page
    elif data.interview and data.getresultbutton :
        if inBounds(event.x, event.y,data.resultbounds ) :
                 data.interview, data.result = False, True       
    elif data.admin :
        for ele in data.adminBounds :
            #print(event.x,event.y)
            i,bounds = ele
            #print(inBounds(event.x, event.y, bounds))
            if inBounds(event.x, event.y, bounds) :
                data.click, data.clickbounds = (True,i), bounds
                jobname = data.titles[i]
                #data.job = data.nameTitles[i]
                saveJob(jobname)
        if inBounds(event.x, event.y, data.adminbutton) :
            data.admin,data.indexpage = False, True
    elif data.result :
        if inBounds(event.x,event.y, data.result1bounds) :
            data.result,data.resultpage1 = False, True  
                      
def saveJob(jobname) :#save comparison data
    
    txt = findJob(jobname)
    #print(jobname,txt)
    #txt = findJob(jobname)
    if len(txt) < 600 : txt *=4
    callPersonalityInsights(txt, "comparison")
    
def keyPressed(event, data):#scrolling and calling functions 
    # use event.char and event.keysym
    if data.interview:
        if event.keysym =="r" : data.getresultbutton = True
        #elif event.keysym == "s" : data.startinter = True
    if data.admin :
        if (event.keysym == "Left"):    doMove(0,-10, data)
        elif (event.keysym == "Right"): doMove(0, +10, data)
    elif data.interview and event.keysym =="s" :
        startInterview(data)    
    elif data.result and event.keysym == "r" : 
        bestMatch(data)
        data.bestMatch = True
def timerFired(data):
    pass

def redrawAll(canvas, data):#drawing pages
    # draw in canvas
    if data.indexpage : drawIndex(canvas,data)
    elif data.admin : drawAdmin(canvas,data)
    elif data.instruct :  drawInstruct(canvas, data)
    elif data.interview : drawInterview(canvas,data)
    elif data.result : drawResult(canvas,data)
    elif data.resultpage1 : drawResult1(canvas,data)
    if data.getresultbutton : drawResultButton(canvas, data)

###############
#RunFunction
###############################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 90 # milliseconds
    init(data)
    AdminBounds(data) #initializes with init so reduces lag time of computation 
    randomComp(data)
    #of drawAdmin
    # create the root and the canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack(fill=BOTH, expand=YES)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    initCanvas(canvas)
    # set up events
    # root.bind("<Button-1>", leftMousePressed)
    # root.bind("<KeyPress>", keyPressed)
    # timerFired(canvas)
    # and launch the app
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    root.mainloop() 

run(1500,750)

#callPersonalityInsights("profile1.json")