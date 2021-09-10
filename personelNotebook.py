##### PERSONAL NOTEBOOK GUI ####

import random
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

import os
from datetime import *


import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.haberturk.com/")

soup = BeautifulSoup(r.content,"lxml")

dolar= soup.find("a", id="dolar").text
euro = soup.find("a", id="euro").text
gramAltin = soup.find("a", id="gram-altin").text
bist100 = soup.find("a", id="bist-100").text



today = datetime.today()

dateOfNote = today.strftime("%Y-%m-%d %H:%M")



root = Tk()

root.title("Personel Notebook")

canvas = Canvas(root,height = 1100,width = 2400)
canvas.pack()


### FRAMES

notesFrame = Frame(root,bg = "#5b9aa0",bd = 8, relief=RAISED)
notesFrame.place(relx =0.03 , rely =0.03 ,relwidth = 0.46,relheight = 0.45)

calendarFrame = Frame(root,bg = "#5b9aa0",bd = 8, relief=RAISED)
calendarFrame.place(relx =0.03 , rely =0.525 ,relwidth = 0.3,relheight = 0.45)

takenNotesFrame = Frame(root,bg = "#5b9aa0",bd = 8, relief=RAISED)
takenNotesFrame.place(relx =0.52 , rely =0.03 ,relwidth = 0.46,relheight = 0.45)

currencyFrame = Frame(root,bg = "#5b9aa0",bd = 8, relief=RAISED)
currencyFrame.place(relx =0.355 ,rely =0.525,relwidth = 0.3,relheight = 0.45)

movieFrame = Frame(root,bg = "#5b9aa0",bd = 8, relief=RAISED)
movieFrame.place(relx =0.68 ,rely =0.525 ,relwidth = 0.3,relheight = 0.45)


#FUNCTIONS

def refresh():
    global noteArea
    today = datetime.today()

    dateOfNote = today.strftime("%Y-%m-%d %H:%M")
    noteArea.forget()
    
   

    noteArea = Text(notesFrame,height = 18, width = 85,font = "Times 13 bold italic",borderwidth = 5, bd = 4, relief = SUNKEN)
    
    firstNote = "{} : ".format(dateOfNote)
    
    
    
    noteArea.tag_configure('style',foreground = "black",font = ("Times",13,'bold','italic'))
    noteArea.insert(END,firstNote,'style')
    noteArea.pack(anchor = NW,padx = 15,pady = 10)
    

def saveNotes():
    notes = noteArea.get('1.0','end')
    with open("notes.txt",'a') as notesFile:
        notesFile.write(notes)
        notesFile.close()
    today = datetime.today()

    dateOfNote = today.strftime("%Y-%m-%d %H:%M")
    
    
    noteArea.delete('1.0','end')
    
    firstNote = "{} : ".format(dateOfNote)
    noteArea.tag_configure('style',foreground = "black",font = ("Times",13,'bold','italic'))
    noteArea.insert(END,firstNote,'style')
   
    
    messagebox.showinfo("TAKE NOTES","Note Saved")
    
def displayTakenNotes():
    
    with open('notes.txt', 'r') as file:
        takenNotes = file.read()
    
    takenNotesArea.tag_configure('style',foreground = "black",font = ("Times",13,'bold','italic'))
    takenNotesArea.insert(END,takenNotes,'style')
   
 
def clearTakenNotesScreen():
    takenNotesArea.delete('1.0','end')
     

def clearTakenNotes():
    resp = messagebox.askokcancel("Delete Notes Screen","Are you sure want to delete all the taken notes?")
    Label(root,text = resp).pack()
    
    if resp == 1:
        os.remove('notes.txt')
        messagebox.showinfo("Delete Notes ","You Deleted all the taken notes")
        takenNotesArea.delete('1.0','end')
    
    elif resp == 0:
        messagebox.showinfo("Delete Notes ","That was close")
        
        
def Send():
    todaysDATE = today.strftime("%Y.%m.%d")
    date = calendar.get()
    typeOfReminder= reminderTypeOption.get()
     
    with open("reminder.txt",'a') as reminderFile:
        reminderFile.write('\nOn : {}  ->  {} Event'.format(date,typeOfReminder))
        reminderFile.close()
    
    messagebox.showinfo("REMINDER","Reminder Saved")
      
def Reminder():    
       
    
    with open("reminder.txt","r") as reminderFile:
        
        content = reminderFile.read()
        reminderFile.close()
        
    reminderScreen = messagebox.showinfo("REMINDER",str(content))
    reminderScreen.pack()
    mainloop()
    
def ClearEvents():
    response = messagebox.askokcancel("Delete All Reminders","Are you sure want to delete all the reminders?")
    Label(root,text = response).pack()
    
    if response == 1:
        os.remove('reminder.txt')
        messagebox.showinfo("DELETE REMINDERS","You Deleted all the reminders")
    
    
    elif response == 0:
        messagebox.showinfo("DELETE REMINDERS","","That was close")
    


def RefreshCurrencies():
    r = requests.get("https://www.haberturk.com/")

    soup = BeautifulSoup(r.content,"lxml")
    
    dolar= soup.find("a", id="dolar").text
    euro = soup.find("a", id="euro").text
    gramAltin = soup.find("a", id="gram-altin").text
    
    dolarFrame = Label(currencyFrame,bg ="#5b9aa0",fg = "black" , text = str(dolar), font = "Times 18 bold" )
    dolarFrame.grid(row =1,column = 2,padx= 13,pady =4,ipadx= 20)
    
    altinFrame = Label(currencyFrame,bg ="#5b9aa0",fg = "black" , text = str(gramAltin), font = "Times 18 bold" )
    altinFrame.grid(row =1,column = 4,padx= 13,pady =4,ipadx= 20)
    
    euroFrame = Label(currencyFrame,bg ="#5b9aa0",fg = "black" , text = str(euro), font = "Times 18 bold" )
    euroFrame.grid(row =2,column = 2,padx= 13,pady =5,ipadx= 20)
    
    RefreshCurrenciesButton = Button(currencyFrame,bg="black",fg = "white",text = 'Refresh',font = "Times 13",borderwidth = 6, bd = 6, relief = RAISED,command = RefreshCurrencies)
    RefreshCurrenciesButton.grid(row =2,column = 4,padx= 13,pady =5,ipadx= 20)
    
    

    messagebox.showinfo("Currency Screen","Currencies Reseted")
    
    
def RandomRecommendation():
    
    movieRequest = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    
    movieSoup= BeautifulSoup(movieRequest.content,"lxml")
    
    
    movies = movieSoup.find_all("td",attrs = {"class":"titleColumn"})
    
    movieList = []
    movieDate = []
    
  
    for movie in movies:
        movieList.append(movie.a.text.replace("(","").replace(")",""))
        movieDates = movie.find("span",attrs ={"class":"secondaryInfo"}).text.replace("(","").replace(")","")
        movieDate.append(movieDates)
        
        
       
        newMovieList = list(zip(movieList,movieDate)) 
        
        
        
    RecommendedMovie = random.choice(newMovieList)
    
    

    
    #NEW WINDOWS
    
    newWindows = Toplevel()
    newWindows.title("Movie Recommendation")

    movie_canvas = Canvas(newWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    movie_canvas.pack()

    
    movieArea = Text(newWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
 
    theMovie= " {} ".format(RecommendedMovie)
    
    
    
    movieArea.tag_configure('style',font=('Verdana', 14))
    
    movieArea.insert(END,theMovie,'style')
    movieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)
    
    

def Action():
    
    actionRequestList  =[
        "https://www.imdb.com/search/title/?genres=action&explore=title_type,genres&view=simple",
        "https://www.imdb.com/search/title/?genres=action&view=simple&start=51&explore=title_type,genres&ref_=adv_nxt",
        "https://www.imdb.com/search/title/?genres=action&view=simple&start=101&explore=title_type,genres&ref_=adv_nxt"
        ]
    
    randomRequest = random.choice(actionRequestList)
    
    
    actionRequest = requests.get(randomRequest)
    
    actionRequest= BeautifulSoup(actionRequest.content,"lxml")
    
    actionMovies = actionRequest.find_all("div",attrs = {"class":"col-title"})
    
    actionMoviesList = []
    actionMoviesDateList = []
    newActionMovieList = []
    
  
    for actionMovie in actionMovies:
        actionMoviesList.append(actionMovie.a.text.replace("(","").replace(")",""))
        actionMovieDates = actionMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        actionMoviesDateList.append(actionMovieDates)
        
        
       
        newActionMovieList = list(zip(actionMoviesList,actionMoviesDateList)) 
      
        
        

    RecommendedActionMovie = random.choice(newActionMovieList)
    newWindows = Toplevel()
    newWindows.title("Action Movie Recommendation")

    movie_canvas = Canvas(newWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    movie_canvas.pack()

    
    actionMovieArea = Text(newWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
 
    theMovie= " {} ".format(RecommendedActionMovie)
    
    
    
    actionMovieArea.tag_configure('style',font=('Verdana', 14))
    
    actionMovieArea.insert(END,theMovie,'style')
    actionMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)
    
def Comedy():
    comedyRequestList  = ["https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=5B3JB4MV8VTHS9YTPHEZ&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1",
                          "https://www.imdb.com/search/title/?genres=comedy&start=51&explore=title_type,genres&ref_=adv_nxt",
                          "https://www.imdb.com/search/title/?genres=comedy&start=101&explore=title_type,genres&ref_=adv_nxt"
                          ]
        
 
    
    randomComedyRequest = random.choice(comedyRequestList)
    comedyRequest = requests.get(randomComedyRequest)
    
    comedyRequest= BeautifulSoup(comedyRequest.content,"lxml")
    
    comedyMovies = comedyRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    comedyMoviesList = []
    comedyMoviesDateList = []
    newComedyMovieList = []
    
  
    for comedyMovie in comedyMovies:
        comedyMoviesList.append(comedyMovie.a.text.replace("(","").replace(")",""))
        comedyMovieDates = comedyMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        comedyMoviesDateList.append(comedyMovieDates)
        
        
       
        newComedyMovieList = list(zip(comedyMoviesList ,comedyMoviesDateList)) 
      
        
        

    RecommendedComedyMovie = random.choice(newComedyMovieList)
    
    newComedyWindows = Toplevel()
    newComedyWindows.title("Comedy Movie Recommendation")

    comedy_movie_canvas = Canvas(newComedyWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    comedy_movie_canvas.pack()

    
    comedyMovieArea = Text(newComedyWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
   
    theComedyMovie= " {} ".format(RecommendedComedyMovie)
    
    
    
    comedyMovieArea.tag_configure('style',font=('Verdana', 14))
    
    comedyMovieArea.insert(END,theComedyMovie,'style')
    comedyMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)
    

def Drama():
    dramaRequestList  = ["https://www.imdb.com/search/title/?genres=drama&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f1cf7b98-03fb-4a83-95f3-d833fdba0471&pf_rd_r=8Y0B04C92T8TS98ABFFF&pf_rd_s=center-3&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr3_i_1",
                         "https://www.imdb.com/search/title/?genres=drama&start=51&explore=title_type,genres&ref_=adv_nxt",
                         "https://www.imdb.com/search/title/?genres=drama&start=101&explore=title_type,genres&ref_=adv_nxt"
                        ]
        
 
    
    randomDramaRequest = random.choice(dramaRequestList)
    dramaRequest = requests.get(randomDramaRequest)
    
    dramaRequest= BeautifulSoup(dramaRequest.content,"lxml")
    
    dramaMovies = dramaRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    dramaMoviesList = []
    dramaMoviesDateList = []
    newDramaMovieList = []
    
  
    for dramaMovie in dramaMovies:
        dramaMoviesList.append(dramaMovie.a.text.replace("(","").replace(")",""))
        dramaMovieDates = dramaMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        dramaMoviesDateList.append(dramaMovieDates)
        
        
       
        newDramaMovieList = list(zip(dramaMoviesList ,dramaMoviesDateList)) 
      
        
        

    RecommendedDramaMovie = random.choice(newDramaMovieList)
    
    newDramaWindows = Toplevel()
    newDramaWindows.title("Drama Movie Recommendation")

    drama_movie_canvas = Canvas(newDramaWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    drama_movie_canvas.pack()

    
    dramaMovieArea = Text(newDramaWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
 
    theDramaMovie= " {} ".format(RecommendedDramaMovie)
    
    
    
    dramaMovieArea.tag_configure('style',font=('Verdana', 14))
    
    dramaMovieArea.insert(END,theDramaMovie,'style')
    dramaMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)


def Fantasy():
    fantasyRequestList  = ["https://www.imdb.com/search/title/?genres=fantasy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=fd0c0dd4-de47-4168-baa8-239e02fd9ee7&pf_rd_r=FPK1PV31N2YQPKB0ZC62&pf_rd_s=center-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr4_i_3",
                          "https://www.imdb.com/search/title/?genres=fantasy&start=51&explore=title_type,genres&ref_=adv_nxt",
                          "https://www.imdb.com/search/title/?genres=fantasy&start=101&explore=title_type,genres&ref_=adv_nxt"
                         ]
        
 
    
    randomFantasyRequest = random.choice(fantasyRequestList)
    fantasyRequest = requests.get(randomFantasyRequest)
    
    fantasyRequest= BeautifulSoup(fantasyRequest.content,"lxml")
    
    fantasyMovies = fantasyRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    fantasyMoviesList = []
    fantasyMoviesDateList = []
    newFantasyMovieList = []
    
  
    for fantasyMovie in fantasyMovies:
        fantasyMoviesList.append(fantasyMovie.a.text.replace("(","").replace(")",""))
        fantasyMovieDates = fantasyMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        fantasyMoviesDateList.append(fantasyMovieDates)
        
        
       
        newFantasyMovieList = list(zip(fantasyMoviesList ,fantasyMoviesDateList)) 
      
        
        

    RecommendedFantasyMovie = random.choice(newFantasyMovieList)
    
    newFantasyWindows = Toplevel()
    newFantasyWindows.title("Fantasy Movie Recommendation")
   

    fantasy_movie_canvas = Canvas(newFantasyWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    fantasy_movie_canvas.pack()

    
    fantasyMovieArea = Text(newFantasyWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
  
 
    theFantasyMovie= " {} ".format(RecommendedFantasyMovie)
    
    
    
    fantasyMovieArea.tag_configure('style',font=('Verdana', 14))
    
    fantasyMovieArea.insert(END,theFantasyMovie,'style')
    fantasyMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)



def Horror():
    horrorRequestList  = ["https://www.imdb.com/search/title/?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=FPK1PV31N2YQPKB0ZC62&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3",
                          "https://www.imdb.com/search/title/?genres=horror&start=51&explore=title_type,genres&ref_=adv_nxt",
                          "https://www.imdb.com/search/title/?genres=horror&start=101&explore=title_type,genres&ref_=adv_nxt"
                         ]
        
 
    
    randomHorrorRequest = random.choice(horrorRequestList)
    horrorRequest = requests.get(randomHorrorRequest)
    
    horrorRequest= BeautifulSoup(horrorRequest.content,"lxml")
    
    horrorMovies = horrorRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    horrorMoviesList = []
    horrorMoviesDateList = []
    newHorrorMovieList = []
    
  
    for horrorMovie in horrorMovies:
        horrorMoviesList.append(horrorMovie.a.text.replace("(","").replace(")",""))
        horrorMovieDates = horrorMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        horrorMoviesDateList.append(horrorMovieDates)
        
        
       
        newHorrorMovieList = list(zip(horrorMoviesList ,horrorMoviesDateList)) 
      
        
        

    RecommendedHorrorMovie = random.choice(newHorrorMovieList)
    
    newHorrorWindows = Toplevel()
    newHorrorWindows.title("Horror Movie Recommendation")
   

    horror_movie_canvas = Canvas(newHorrorWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    horror_movie_canvas.pack()

    
    horrorMovieArea = Text(newHorrorWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
  
 
    theHorrorMovie= " {} ".format(RecommendedHorrorMovie)
    
    
    
    horrorMovieArea.tag_configure('style',font=('Verdana', 14))
    
    horrorMovieArea.insert(END,theHorrorMovie,'style')
    horrorMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)



def Mystery():
    mysteryRequestList  = ["https://www.imdb.com/search/title/?genres=mystery&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f1cf7b98-03fb-4a83-95f3-d833fdba0471&pf_rd_r=FPK1PV31N2YQPKB0ZC62&pf_rd_s=center-3&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr3_i_2",
                           "https://www.imdb.com/search/title/?genres=mystery&start=51&explore=title_type,genres&ref_=adv_nxt",
                           "https://www.imdb.com/search/title/?genres=mystery&start=101&explore=title_type,genres&ref_=adv_nxt"
                         ]
        
 
    
    randomMysteryRequest = random.choice(mysteryRequestList)
    mysteryRequest = requests.get(randomMysteryRequest)
    
    mysteryRequest = BeautifulSoup(mysteryRequest.content,"lxml")
    
    mysteryMovies = mysteryRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    mysteryMoviesList = []
    mysteryMoviesDateList = []
    newHorrorMovieList = []
    
  
    for mysteryMovie in mysteryMovies:
        mysteryMoviesList.append(mysteryMovie.a.text.replace("(","").replace(")",""))
        mysteryMovieDates = mysteryMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        mysteryMoviesDateList.append(mysteryMovieDates)
        
        
       
        newMysteryMovieList = list(zip(mysteryMoviesList ,mysteryMoviesDateList)) 
      
        
        

    RecommendedMysteryMovie = random.choice(newMysteryMovieList)
    
    newMysteryWindows = Toplevel()
    newMysteryWindows.title("Mystery Movie Recommendation")
   

    mystery_movie_canvas = Canvas(newMysteryWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    mystery_movie_canvas.pack()

    
    mysteryMovieArea = Text(newMysteryWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
  
 
    theMysteryMovie= " {} ".format(RecommendedMysteryMovie)
    
    
    
    mysteryMovieArea.tag_configure('style',font=('Verdana', 14))
    
    mysteryMovieArea.insert(END,theMysteryMovie,'style')
    mysteryMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)





def Romance():
    romanceRequestList  = ["https://www.imdb.com/search/title/?genres=romance&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e0da8c98-35e8-4ebd-8e86-e7d39c92730c&pf_rd_r=FPK1PV31N2YQPKB0ZC62&pf_rd_s=center-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr2_i_1",
                           "https://www.imdb.com/search/title/?genres=romance&start=51&explore=title_type,genres&ref_=adv_nxt",
                           "https://www.imdb.com/search/title/?genres=romance&start=101&explore=title_type,genres&ref_=adv_nxt"
                         ]
        
 
    
    randomRomanceRequest = random.choice(romanceRequestList)
    romanceRequest = requests.get(randomRomanceRequest)
    
    romanceRequest = BeautifulSoup(romanceRequest.content,"lxml")
    
    romanceMovies = romanceRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    romanceMoviesList = []
    romanceMoviesDateList = []
    newRomanceMovieList = []
    
  
    for romanceMovie in romanceMovies:
        romanceMoviesList.append(romanceMovie.a.text.replace("(","").replace(")",""))
        romanceMovieDates = romanceMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        romanceMoviesDateList.append(romanceMovieDates)
        
        
       
        newRomanceMovieList = list(zip(romanceMoviesList ,romanceMoviesDateList)) 
      
        
        

    RecommendedRomanceMovie = random.choice(newRomanceMovieList)
    
    newRomanceWindows = Toplevel()
    newRomanceWindows.title("Romance Movie Recommendation")
   

    romance_movie_canvas = Canvas(newRomanceWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    romance_movie_canvas.pack()

    
    romanceMovieArea = Text(newRomanceWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
  
 
    theRomanceMovie= " {} ".format(RecommendedRomanceMovie)
    
    
    
    romanceMovieArea.tag_configure('style',font=('Verdana', 14))
    
    romanceMovieArea.insert(END,theRomanceMovie,'style')
    romanceMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)
    
    
    


def Thriller():
    thrillerRequestList  = ["https://www.imdb.com/search/title/?genres=thriller&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e0da8c98-35e8-4ebd-8e86-e7d39c92730c&pf_rd_r=7GG7JWS4X15AA7Z8V21J&pf_rd_s=center-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr2_i_3",
                            "https://www.imdb.com/search/title/?genres=thriller&start=51&explore=title_type,genres&ref_=adv_nxt",
                            "https://www.imdb.com/search/title/?genres=thriller&start=101&explore=title_type,genres&ref_=adv_nxt"
                            ]
        
 
    
    randomThrillerRequest = random.choice(thrillerRequestList)
    thrillerRequest = requests.get(randomThrillerRequest)
    
    thrillerRequest = BeautifulSoup(thrillerRequest.content,"lxml")
    
    thrillerMovies = thrillerRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    thrillerMoviesList = []
    thrillerMoviesDateList = []
    newThrillerMovieList = []
    
  
    for thrillerMovie in thrillerMovies:
        thrillerMoviesList.append(thrillerMovie.a.text.replace("(","").replace(")",""))
        thrillerMovieDates = thrillerMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        thrillerMoviesDateList.append(thrillerMovieDates)
        
        
       
        newThrillerMovieList = list(zip(thrillerMoviesList ,thrillerMoviesDateList)) 
      
        
        

    RecommendedThrillerMovie = random.choice(newThrillerMovieList)
    
    newThrillerWindows = Toplevel()
    newThrillerWindows.title("Thriller Movie Recommendation")
   

    thriller_movie_canvas = Canvas(newThrillerWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    thriller_movie_canvas.pack()

    
    thrillerMovieArea = Text(newThrillerWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
  
 
    theThrillerMovie= " {} ".format(RecommendedThrillerMovie)
    
    
    
    thrillerMovieArea.tag_configure('style',font=('Verdana', 14))
    
    thrillerMovieArea.insert(END,theThrillerMovie,'style')
    thrillerMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)




def SciFi():
    scifiRequestList  = ["https://www.imdb.com/search/title/?genres=sci-fi&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=RPZBXG5XWCAZPEDTK5ZG&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_2",
                            "https://www.imdb.com/search/title/?genres=sci-fi&start=51&explore=title_type,genres&ref_=adv_nxt",
                            "https://www.imdb.com/search/title/?genres=sci-fi&start=101&explore=title_type,genres&ref_=adv_nxt"
                            ]
        
 
    
    randomScifiRequest = random.choice(scifiRequestList)
    scifiRequest = requests.get(randomScifiRequest)
    
    scifiRequest = BeautifulSoup(scifiRequest.content,"lxml")
    
    scifiMovies = scifiRequest.find_all("h3",attrs = {"class":"lister-item-header"})
    
    scifiMoviesList = []
    scifiMoviesDateList = []
    newScifiMovieList = []
    
  
    for scifiMovie in scifiMovies:
        scifiMoviesList.append(scifiMovie.a.text.replace("(","").replace(")",""))
        scifiMovieDates = scifiMovie.find("span",attrs ={"class":"lister-item-year text-muted unbold"}).text.replace("(","").replace(")","")
        scifiMoviesDateList.append(scifiMovieDates)
        
        
       
        newScifiMovieList = list(zip(scifiMoviesList ,scifiMoviesDateList)) 
      
        
        

    RecommendedScifiMovie = random.choice(newScifiMovieList)
    
    newScifiWindows = Toplevel()
    newScifiWindows.title("Science Fiction Movie Recommendation")
   

    scifi_movie_canvas = Canvas(newScifiWindows,bg ="#528AAE",height = 1100,width = 2400,bd= 5,relief = RAISED)
    scifi_movie_canvas.pack()

    
    scifiMovieArea = Text(newScifiWindows,height = 10, width = 50,borderwidth = 5, bd = 8, relief = RAISED)
    
  
 
    theScifiMovie= " {} ".format(RecommendedScifiMovie)
    
    
    
    scifiMovieArea.tag_configure('style',font=('Verdana', 14))
    
    scifiMovieArea.insert(END,theScifiMovie,'style')
    scifiMovieArea.place(relx =0.3 , rely =0.4 ,relwidth = 0.42,relheight = 0.15)







    
#LABELS

notesLabel = Label(notesFrame,bg = "#5b9aa0", fg = "black", text = "TAKE NOTES", font = "Times 21 bold italic underline")
notesLabel.pack(anchor = NW,padx = 5,pady = 5)

saveButton = Button(notesFrame,font = "Times 12",bg="black",fg = "white",text = 'Save',borderwidth = 2, bd = 5, relief = RAISED,command = saveNotes)
saveButton.pack(anchor = NE,padx = 15,pady = 5,ipadx = 15)

refreshButton = Button(notesFrame,font = "Times 12",bg="black",fg = "white",text = 'Refresh',borderwidth = 2, bd = 5, relief = RAISED,command = refresh)
refreshButton.pack(anchor = NE,padx = 15,pady = 5,ipadx = 15)


noteArea = Text(notesFrame,height = 18, width = 85,font = "Times 13 bold italic",borderwidth = 5, bd = 4, relief = SUNKEN)

firstNote = "{} : ".format(dateOfNote)



noteArea.tag_configure('style',foreground = "black",font = ("Times",13,'bold','italic'))
noteArea.insert(END,firstNote,'style')
noteArea.pack(anchor = NW,padx = 15,pady = 10)


### TAKEN NOTES AREA


takenNotesLabel = Label(takenNotesFrame,bg = "#5b9aa0", fg = "black", text = "TAKEN NOTES", font = "Times 21 bold italic underline")
takenNotesLabel.pack(anchor = NW,padx = 5,pady = 0)

displayButton = Button(takenNotesFrame,font = "Times 12",bg="black",fg = "white",text = 'Display Taken Notes',borderwidth = 2, bd = 5, relief = RAISED,command = displayTakenNotes)
displayButton.pack(anchor = NE,padx = 25,pady = 4,ipadx = 13)

clearTakenNotesButton = Button(takenNotesFrame,font = "Times 12",bg="black",fg = "white",text = 'Clear the Screen',borderwidth = 2, bd = 5, relief = RAISED,command =clearTakenNotesScreen)
clearTakenNotesButton.pack(anchor = NE,padx = 25,pady = 4,ipadx = 13)

clearAllTakenNotesButton = Button(takenNotesFrame,font = "Times 12",bg="black",fg = "white",text = 'Clear Taken Notes',borderwidth = 2, bd = 5, relief = RAISED,command =clearTakenNotes)
clearAllTakenNotesButton.pack(anchor = NE,padx = 25,pady = 4,ipadx = 13)


takenNotesArea = Text(takenNotesFrame,height = 250, width = 85,borderwidth = 5, bd = 4, relief = SUNKEN)

takenNotesArea.tag_configure('style',foreground = "#bfbfbf",font = ("Verdana",10,'bold'))
takenNotesArea.pack(anchor = S,padx = 15,pady = 5)




#CALENDAR AREA


    
calendarLabel = Label(calendarFrame,bg = "#5b9aa0",fg = "black",text = "REMINDER",font = "Times 22 bold italic underline")
calendarLabel.pack(anchor = N, padx = 5, pady = 5)

reminderType = Label(calendarFrame,bg ="#5b9aa0",fg = "black",text = "REMINDER TYPE",font = "Times 15 bold italic ")
reminderType.pack(anchor = N, padx = 5,pady = 9)

reminderTypeOption = StringVar(calendarFrame)
reminderTypeOption.set("\t")

reminderTypeMenu = OptionMenu(calendarFrame,reminderTypeOption,"Work","Birthday","Meeting","Deadline","Private")

reminderTypeMenu.pack(anchor = N,padx = 5, pady = 0,ipadx = 25,ipady = 1)

calendar = DateEntry(calendarFrame,width = 12,bg = 'orange',foreground = 'black',borderwidth = 1, locale = 'de_DE')


calendar.pack(anchor = N,padx = 5,pady = 9,ipadx = 11,ipady=1)

calendar._top_cal.overrideredirect(False)



day_var = IntVar()


DeliverButton = Button(calendarFrame,font = "Times 12",bg="black",fg = "white",text = 'Send',borderwidth = 2, bd = 5, relief = RAISED,command = Send)
DeliverButton.pack(anchor = N,padx = 5, pady = 11,ipadx = 31,ipady = 1)

RemindMeButton = Button(calendarFrame,font = "Times 12",bg="black",fg = "white",text = 'Remind Me',borderwidth = 2, bd = 5, relief = RAISED,command = Reminder)
RemindMeButton.pack(anchor = S,padx = 5, pady = 11,ipadx = 10,ipady = 1)

ClearEventsButton =Button(calendarFrame,font = "Times 12",bg="black",fg = "white",text = 'Clear Reminders',borderwidth = 2, bd = 5, relief = RAISED,command = ClearEvents)
ClearEventsButton.pack(anchor = S,padx = 5, pady = 11,ipadx = 10,ipady = 1)


#CURRENCIES AREA

currencyFrameLabel = Label(currencyFrame,bg ="#5b9aa0",fg = "black", text = "CURRENCIES",font = "Times 22 bold italic underline")
currencyFrameLabel.grid(row =0,column = 2,padx= 16,pady =5,ipadx= 20)

dolarFrame = Label(currencyFrame,bg ="#5b9aa0",fg = "black" , text = str(dolar), font = "Times 18 bold" )
dolarFrame.grid(row =1,column = 2,padx= 13,pady =4,ipadx= 20)

altinFrame = Label(currencyFrame,bg ="#5b9aa0",fg = "black" , text = str(gramAltin), font = "Times 18 bold" )
altinFrame.grid(row =1,column = 4,padx= 13,pady =4,ipadx= 20)

euroFrame = Label(currencyFrame,bg ="#5b9aa0",fg = "black" , text = str(euro), font = "Times 18 bold" )
euroFrame.grid(row =2,column = 2,padx= 13,pady =5,ipadx= 20)

RefreshCurrenciesButton = Button(currencyFrame,bg="black",fg = "white",text = 'Refresh',font = "Times 12",borderwidth = 6, bd = 6, relief = RAISED,command = RefreshCurrencies)
RefreshCurrenciesButton.grid(row =2,column = 4,padx= 13,pady =5,ipadx= 20)








#MOVIE RECOMMENDATION AREA


movieVariable = IntVar()

movieLabel = Label(movieFrame,bg ="#5b9aa0",fg = "black",text = "MOVIE",font = "Times 22 bold italic underline" )
movieLabel.grid(row = 0,column = 2,padx= 9,pady =5)


actionButton = Button(movieFrame,text = "Action",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Action)
actionButton.grid(row =1,column = 2,padx= 15,pady =15,ipadx= 23)

comedyButton = Button(movieFrame,text = "Comedy",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Comedy)
comedyButton.grid(row =1,column = 4,padx= 15,pady =15,ipadx= 16)


dramaButton = Button(movieFrame,text = "Drama",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Drama)
dramaButton.grid(row =1,column = 6,padx= 15,pady =15,ipadx= 18)


fantasyButton = Button(movieFrame,text = "Fantasy",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Fantasy)
fantasyButton.grid(row =2,column = 2,padx= 15,pady =15,ipadx= 14)


horrorButton = Button(movieFrame,text = "Horror",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Horror)
horrorButton.grid(row =2,column = 4,padx= 15,pady =15,ipadx= 20)


mysteryButton = Button(movieFrame,text = "Mystery",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Mystery)
mysteryButton.grid(row =2,column = 6,padx= 15,pady =15,ipadx= 13)


romanceButton = Button(movieFrame,text = "Romance",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Romance)
romanceButton.grid(row =3,column = 2,padx= 15,pady =15,ipadx= 11)


thrillerButton = Button(movieFrame,text = "Thriller",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = Thriller)
thrillerButton.grid(row =3,column = 4,padx= 15,pady =15,ipadx= 19)


scienceFictionButton = Button(movieFrame,text = "Sci-Fi",font = "Times 16 italic bold",borderwidth = 1, bd = 4, relief = RAISED,command = SciFi)
scienceFictionButton.grid(row =3,column = 6,padx= 15,pady =15,ipadx= 22)



randomButton = Button(movieFrame,bg="black",fg = "white",text = 'Random',font = "Times 12",borderwidth = 2, bd = 5, relief = RAISED,command = RandomRecommendation)
randomButton.grid(row = 5,column = 4,padx= 18,pady = 15,ipadx= 20)


root.mainloop()
    

