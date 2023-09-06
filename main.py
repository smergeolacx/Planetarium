#visuals
import turtle
q='''                                                Good day to you.
  this is a sql py project done by Anish Pramod solleti and Sanskar Jotwani.
This projects keeps the records related to the space and space organizations.
           we hope you like this project and understand it as much as we liked making this.
                                                   THANK YOU!!!'''
turtle.color('gray')
style = ('agency fb',24, '')

turtle.write(q, font=style, align='center')

turtle.hideturtle()

import mysql.connector as ms
print("Its important to keep track of what happens not only within our planet")
print("but also outside of it")
print("Space and Universe")
print(". . . . Storing Default Values. . . .")
#Submenu for planet table
def planet():
    while True:
        print('1. add planet')
        print('2. search planets')
        print('3. make corrections in planet')
        print('4. delete planet')
        print('5. show table planet')
        print('6. No Changes')
        try:
            a=int(input('enter your choice'))
        except:
            print('invalid')
            continue
        if a==1:
            add_p()
        if a==2:
            search_p()
        if a==3:
            update_p()
        if a==4:
            delete_p()
        if a==5:
            show_p()
        if a==6:
            break
        
#Submenu for galaxies table
def galaxies():
    while True:
        print('1. add galaxies')
        print('2. search galaxies')
        print('3. make corrections in galaxy')
        print('4. delete galaxy')
        print('5. show table galaxy')
        print('6. No Changes')
        try:
            b=int(input('enter your choice'))
        except:
            print('invalid')
            continue
        if b==1:
            add_g()
        if b==2:
            search_g()
        if b==3:
            update_g()
        if b==4:
            delete_g()
        if b==5:
            show_g()
        if b==6:
            break

#Submenu for stars table
def stars():
    while True:
        print('1. add star')
        print('2. search stars')
        print('3. make corrections in star')
        print('4. delete star')
        print('5. show table star')
        print('6. No Changes')
        try:
            c=int(input('enter your choice'))
        except:
            print('invalid')
            continue
        if c==1:
            add_s()
        if c==2:
            search_s()
        if c==3:
            update_s()
        if c==4:
            delete_s()
        if c==5:
            show_s()
        if c==6:
            break
#Submenu for moons table
def moons():
    while True:
        print('1. add moon')
        print('2. search moons')
        print('3. make corrections in moon')
        print('4. delete moon')
        print('5. show table moon')
        print('6. No Changes')
        try:
            d=int(input('enter your choice'))
        except:
            print('invalid')
            continue
        if d==1:
            add_m()
        if d==2:
            search_m()
        if d==3:
            update_m()
        if d==4:
            delete_m()
        if d==5:
            show_m()
        if d==6:
            break

#Submenu for organisation table
def org():
    while True:
        print('1. add organization')
        print('2. search satellites of organization')
        print('3. make corrections in organization')
        print('4. delete organization')
        print('5. show table organization')
        print('6. No Changes')
        try:
            e=int(input('enter your choice'))
        except:
            print('invalid')
            continue
        if e==1:
            add_o()
        if e==2:
            search_o()
        if e==3:
            update_o()
        if e==4:
            delete_o()
        if e==5:
            show_o()
        if e==6:
            break

#Establishing connection
mydb=ms.connect(host="localhost",user="root",passwd="puchi12345")
#Checking connection 
def check():            
    if mydb.is_connected():
        print('successfully connected')
    else:
        print('failed to connect')

#Creating cursor
cr=mydb.cursor()
cr.execute("create database if not exists Universe")
cr.execute("use Universe")
q1="create table if not exists planet(sno int primary key,name varchar(30),year_discovery int default 0000,surface_gravity char(30),num_moon int(80))"
cr.execute(q1)
q2="create table if not exists galaxy(sno int primary key,name varchar(30),year_discovery int,shape varchar(30),distance_lightyear int(15))"
cr.execute(q2)
q3="create table if not exists star(sno int primary key,name varchar(30),year_discovery int,solar_mass int,distance_lightyear int(15))"
cr.execute(q3)
q4="create table if not exists moon(sno int primary key,name varchar(30),parent_planet char(30),year_discovery int,time_revolution int(15))"
cr.execute(q4)
q5="create table if not exists organization1(sno int primary key, name varchar(30),year int(4),founder varchar(20),well_known_project varchar(20))"
cr.execute(q5)

#addtions functions.

#function to callback for the addition of planet details in the table
def add_p():
    sno=int(input('serial number: '))
    name=input('enter planet name: ')
    year=int(input('enter the year discovered neglecting "B.C","A.D": '))
    surface_gravity=int(input('enter surface_gravity of the planet: '))
    moons=float(input('enter the number of moons: '))
    i1="insert into planet(sno,name,year_discovery ,surface_gravity,num_moon)values({},'{}',{},{},{})".format(sno,name,year,surface_gravity,moons)
    print('... added...')
    cr.execute(i1)
    mydb.commit()

#function to callback for the addition of galaxy details in the table
def add_g():
    sno=int(input('serial number: '))
    name=input('enter galaxy name: ')
    year=int(input('enter the year discovered neglecting "B.C","A.D": '))
    shape=input('enter shape of the galaxy: ')
    distance_lightyear=float(input('enter the distance of the galaxy W.R.T the milkyway: '))
    i2="insert into galaxy(sno,name,year_discovery,shape,distance_lightyear)values({},'{}',{},'{}',{})".format(sno,name,year,shape,distance_lightyear)
    print('... added...')
    cr.execute(i2)
    mydb.commit()
    
#function to callback for the addition of star details in the table
def add_s():
    sno=int(input('serial number: '))
    name=input('enter star name: ')
    year=int(input('enter the year discovered neglecting "B.C","A.D": '))
    solar_mass=input('enter the solar mass of the star: ')
    distance_lightyear=float(input('enter the distance of the star W.R.T the sun: '))
    i3="insert into star(sno,name,year_discovery,solar_mass,distance_lightyear)values({},'{}',{},'{}',{})".format(sno,name,year,solar_mass,distance_lightyear)
    print('... added...')
    cr.execute(i3)
    mydb.commit()
    
#function to callback for the addition of moon details in the table
def add_m():
    sno=int(input('serial number: '))
    name=input('enter moon name: ')
    year=int(input('enter the year discovered neglecting "B.C","A.D": '))
    parent_planet=input('enter the name of the parent planet of the moon: ')
    time_revolution=int(input('enter the time period of the moon in days(round to the closest integer): '))
    i4="insert into moon(sno,name,parent_planet,year,time_revolution)values({},'{}',{},'{}',{})".format(sno,name,parent_planet,year,time_revolution)
    print('... added...')
    cr.execute(i4)
    mydb.commit()
    
#function to callback for the addition of organization details in the table
def add_o():
    sno=int(input('serial number: '))
    name=input('enter organization name: ')
    year=int(input('enter the year the organization was established: '))
    founder=input('enter the name of the founder of the organization: ')
    well_known_project=input('the most recognisible project by the organization: ')
    i5="insert into organization1(sno,name,year,founder,well_known_project)values({},'{}',{},'{}','{}')".format(sno,name,year,founder,well_known_project)
    print('... added...')
    cr.execute(i5)
    mydb.commit()
    
#function to callback for searching record of given planet
def search_p():
    while True:
        try:
            name=input('enter planet name')
        except:
            print('invalid')
            continue
        cr.execute("select * from planet where name='{}'".format(name))
        row=cr.fetchall()    
        for i in row:
            print(i)
        break

#function to callback for searching record of given galaxy
def search_g():
    while True:
        try:
            name=input('enter galaxy name')
        except:
            print('invalid')
            continue
        cr.execute("select * from galaxy where name='{}'".format(name))
        row=cr.fetchall()    
        for i in row:
            print(i)
        break

#function to callback for searching record of given star
def search_s():
    while True:
        try:
            name=input('enter star name')
        except:
            print('invalid')
            continue
        cr.execute("select * from star where name='{}'".format(name))
        row=cr.fetchall()    
        for i in row:
            print(i)
        break

#function to callback for searching record of given moon/natural satellite
def search_m():
    while True:
        try:
            name=input('enter satellite name')
        except:
            print('invalid')
            continue
        cr.execute("select * from moon where name='{}'".format(name))
        row=cr.fetchall()    
        for i in row:
            print(i)
        break

#function to callback for searching record of given organisation
def search_o():
   while True:
        try:
            name=input('enter organization name')
        except:
            print('invalid')
            continue
        cr.execute("select * from organization1 where name='{}'".format(name))
        row=cr.fetchall()    
        for i in row:
            print(i)
        break
        
############################################################################
#delete function.
#function to callback for deleting record of given planet
def delete_p():
    while True:
        try:
            name=input('enter planet name')
        except:
            print('invalid')
            continue
        cr.execute("delete from planet where name='{}'".format(name))
        print('...deleted...')
        mydb.commit()
        break

#function to callback for deleting record of given galaxy
def delete_g():
    while True:
        try:
            name=input('enter galaxy name')
        except:
            print('invalid')
            continue
        cr.execute("delete from galaxy where name='{}'".format(name))
        print('...deleted...')
        mydb.commit()
        break
    
#function to callback for deleting record of given star
def delete_s():
    while True:
        try:
            name=input('enter star name')
        except:
            print('invalid')
            continue
        cr.execute("delete from star where name='{}'".format(name))
        print('...deleted...')
        mydb.commit()
        break

#function to callback for deleting record of given moon
def delete_m():
    while True:
        try:
            name=input('enter moon name')
        except:
            print('invalid')
            continue
        cr.execute("delete from moon where name='{}'".format(name))
        print('...deleted...')
        mydb.commit()
        break

#function to callback for deleting record of given organisation
def delete_o():
    while True:
        try:
            name=input('enter organization name')
        except:
            print('invalid')
            continue
        cr.execute("delete from organization1 where name='{}'".format(name))
        print('...deleted...')
        mydb.commit()
        break
    
#show tables function.
#function to display all the records of table planets
def show_p():
    s1="select * from planet"
    cr.execute(s1)
    row=cr.fetchall()    
    for i in row:
        print(i)

#function to display all the records of table galaxies
def show_g():
    s2="select * from galaxy"
    cr.execute(s2)
    row=cr.fetchall()    
    for i in row:
        print(i)

#function to display all the records of table stars
def show_s():
    s3="select * from star"
    cr.execute(s3)
    row=cr.fetchall()    
    for i in row:
        print(i)

#function to display all the records of table moons
def show_m():
    s4="select * from moon"
    cr.execute(s4)
    row=cr.fetchall()    
    for i in row:
        print(i)

#function to display all the records of table organisation
def show_o():
    s5="select * from organization1"
    cr.execute(s5)
    row=cr.fetchall()    
    for i in row:
        print(i)
        
def update_p():
    a=input('enter name of planet')
    #sno int primary key,name varchar(30),year_discovery int default 0000,surface_gravity char(30),num_moon int(80)
    print('1. year of discovery')
    print('2. surface gravity')
    print('3. number of moons')
    print('4. none')
    up=int(input('what would you like to update?'))
    if up==1:
        up1=int(input('enter new year of discovery'))
        u1="update planet set year_discovery={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==2:
        up1=input('enter new value of surface gravity')
        u1="update planet set surface_gravity='{}' where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==3:
        up1=int(input('enter new number of moons'))
        u1="update planet set num_moon={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==4:
        print('exiting')

def update_g():
    a=input('enter name of galaxy')
    #sno int primary key,name varchar(30),year_discovery int,shape varchar(30),distance_lightyear int(15)
    print('1. year of discovery')
    print('2. shape')
    print('3. distance in lightyears')
    print('4. none')
    up=int(input('what would you like to update?'))
    if up==1:
        up1=int(input('enter new year of discovery'))
        u1="update galaxy set year_discovery={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==2:
        up1=input('enter new shape of galaxy')
        u1="update galaxy set shape='{}' where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==3:
        up1=int(input('enter new distance (in lightyears)'))
        u1="update galaxy set distance_lightyear={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==4:
        print('exiting')

def update_s():
    a=input('enter name of star')
    #sno int primary key,name varchar(30),year_discovery int,solar_mass int,distance_lightyear int(15)
    print('1. year of discovery')
    print('2. solar mass')
    print('3. distance in lightyears')
    print('4. none')
    up=int(input('what would you like to update?'))
    if up==1:
        up1=int(input('enter new year of discovery'))
        u1="update star set year_discovery={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==2:
        up1=int(input('enter new solar mass'))
        u1="update star set solar_mass={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==3:
        up1=int(input('enter new distance (in lightyears)'))
        u1="update star set distance_lightyear={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==4:
        print('exiting')

def update_m():
    a=input('enter name of moon')
    #sno int primary key,name varchar(30),parent_planet char(30),year_discovery int,time_revolution int(15)
    print('1. parent planet')
    print('2. year of discovery')
    print('3. revolution time')
    print('4. none')
    up=int(input('what would you like to update?'))
    if up==1:
        up1=input('enter new parent planet')
        u1="update moon set parent_planet='{}' where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==2:
        up1=int(input('enter new year of discovery'))
        u1="update moon set year_discovery={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==3:
        up1=int(input('enter new time period'))
        u1="update moon set time_revolution={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==4:
        print('exiting')

def update_o():
    a=input('enter name of organization')
    #sno int primary key, name varchar(30),year int(4),founder varchar(20),well_known_project varchar(20)
    print('1. year of foundation')
    print('2. well known/successful project')
    print('3. none')
    up=int(input('what would you like to update?'))
    if up==1:
        up1=input('enter new new/updated year of foundation')
        u1="update organization1 set year={} where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==2:
        up1=int(input('enter new/updated project'))
        u1="update organization1 set well_known_project varchar='{}' where name='{}'".format(up1,a)
        cr.execute(u1)
        print('...updated...')
        mydb.commit()
    elif up==3:
        print('exiting')
############################################################################
#predetermined values.

d="delete from planet where name='earth'"
d1="delete from planet where name='mercury'"
d2="delete from planet where name='venus'"
d3="delete from galaxy where name='milkyway'"
d4="delete from galaxy where name='galaxy2'"
d5="delete from galaxy where name='galaxy3'"
d6="delete from star where name='star1'"
d7="delete from star where name='star2'"
d8="delete from star where name='star3'"
d9="delete from moon where name='moon1'"
d10="delete from moon where name='moon2'"
d11="delete from moon where name='moon3'"
d12="delete from organization where name='org1'"
d13="delete from organization where name='org2'"
d14="delete from organization where name='org3'"
cr.execute(d)
cr.execute(d1)
cr.execute(d2)
cr.execute(d3)
cr.execute(d4)
cr.execute(d5)
cr.execute(d6)
cr.execute(d7)
cr.execute(d8)
cr.execute(d9)
cr.execute(d10)
cr.execute(d11)
cr.execute(d12)
cr.execute(d13)
t1="insert into planet values(01,'mercury',265,3.7,0)"
t2="insert into planet values(02,'venus',1610,8.87,1)"
t3="insert into planet values(03,'earth',0000,9.8,1)"
t4="insert into galaxy values(01,'milkyway', 0000,'spiral disk',0000)"
t5="insert into galaxy values(02,'galaxy2', 0000,'shape2',0000)"
t6="insert into galaxy values(03,'galaxy3', 0000,'shape3',0000)"
t7="insert into star values(01,'star1', 0000,'0000',0000)"
t8="insert into star values(02,'star2', 0000,0000,0000)"
t9="insert into star values(03,'star3', 0000,0000,0000)"
t10="insert into moon values(01,'moon1','parent1',0000,0000)"
t11="insert into moon values(02,'moon1','parent2',0000,0000)"
t12="insert into moon values(03,'moon1','parent3',0000,0000)"
cr.execute(t1)
cr.execute(t2)
cr.execute(t3)
cr.execute(t4)
cr.execute(t5)
cr.execute(t6)
cr.execute(t7)
cr.execute(t8)
cr.execute(t9)
cr.execute(t10)
cr.execute(t11)
cr.execute(t12)
mydb.commit()

print('|','-'*12,'planets','-'*12,'|')

cr.execute('select * from planet')
row=cr.fetchall()
for i in row:
    print(i)
print('|--------------------------------------|')
print('')
print('|','-'*16,'galaxies','-'*16,'|')

cr.execute('select * from galaxy')
row=cr.fetchall()
for i in row:
    print(i)
print('|','-'*46,'|')
print('')
print('|','-'*7,'stars','-'*7,'|')

cr.execute('select * from star')
r2=cr.fetchall()
for k in r2:
    print(k)
print('|','-'*22,'|')
print('')
print('|','-'*13,'moons','-'*13,'|')

cr.execute('select * from moon')
r3=cr.fetchall()
for l in r3:
    print(l)
print('|','-'*38,'|')
print()
print()
print(". . . Default Values Stored . . .")
print()
print(". . . Opening Menu . . .")
print()
print(". . . Welcome to the International Space Research Organisation Access Terminal . . .")
print(". . . Pre-determined values of already acquired data has been stored. You may access them from the tables below . . .")
print()
print(". . . MENU . . .")
print()

def earth():
    q='''Earth, our home, is the third planet from the sun.
It's the only planet known to have an atmosphere containing free oxygen,
oceans of water on its surface and, of course, life.
Earth is the fifth largest of the planets in the solar system. ...
About a fifth of Earth's atmosphere consists of oxygen, produced by plants.'''
    turtle.color('light blue')
    style = ('agency fb',24, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def venus():
    q='''Similar in size and structure to Earth, Venus has been called Earth's
twin. These are not identical twins, however – there are radical
differences between the two worlds.
Venus has a thick, toxic atmosphere filled with carbon dioxide and it’s
perpetually shrouded in thick, yellowish clouds of mostly sulfuric acid
that trap heat, causing a runaway greenhouse effect. It’s the hottest
planet in our solar system, even though Mercury is closer to the Sun.
Venus has crushing air pressure at its surface – more than 90 times that
of Earth – similar to the pressure you'd encounter a mile below the
ocean on Earth.
'''
    turtle.color('brown')
    style = ('agency fb',20, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def mars():
    q='''The fourth planet from the Sun, Mars is a dusty, cold, desert world with a very thin atmosphere.
This dynamic planet has seasons, polar ice caps and weather and canyons and extinct volcanoes,
evidence it was once an even more active past.
Mars is one of the most explored bodies in our solar system.'''
    turtle.color('maroon')
    style = ('agency fb',19, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def mercury():
    q='''The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon.
From the surface of Mercury, the Sun would appear more than three times as large as it does when viewed from Earth,
and the sunlight would be as much as seven times brighter.
Despite its proximity to the Sun, Mercury is not the hottest planet in our solar system –
that title belongs to nearby Venus, thanks to its dense atmosphere.
 '''
    turtle.color('gray')
    style = ('agency fb',16, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def jupiter():
    q='''jupiter has a long history surprising scientists—all the way back to 1610
when Galileo Galilei found the first moons beyond Earth. That discovery
changed the way we see the universe.
Fifth in line from the Sun, Jupiter is, by far, the largest planet in the solar
system – more than twice as massive as all the other planets combined.
Jupiter's familiar stripes and swirls are actually cold, windy clouds of
ammonia and water, floating in an atmosphere of hydrogen and helium.
Jupiter’s iconic Great Red Spot is a giant storm bigger than Earth that
has raged for hundreds of years.
'''
    turtle.color('gray')
    style = ('agency fb',18, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def saturn():
    q='''Saturn is the sixth planet from the Sun and the second largest planet in our solar system.
Adorned with thousands of beautiful ringlets, Saturn is unique among the
planets. It is not the only planet to have rings—made of chunks of ice
and rock—but none are as spectacular or as complicated as Saturn's.
'''
    turtle.color('brown')
    style = ('agency fb',18, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def uranus():
    q='''The first planet found with the aid of a telescope, Uranus was discovered
in 1781 by astronomer William Herschel, although he originally thought it
was either a comet or a star.
It was two years later that the object was universally accepted as a new
planet, in part because of observations by astronomer Johann Elert
Bode. Herschel tried unsuccessfully to name his discovery Georgium
Sidus after King George III. Instead the scientific community accepted
Bode's suggestion to name it Uranus, the Greek god of the sky, as
suggested by Bode.
'''
    turtle.color('blue')
    style = ('agency fb',19, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()

def neptune():
    q='''Dark, cold and whipped by supersonic winds, ice giant Neptune is the
eighth and most distant planet in our solar system.
More than 30 times as far from the Sun as Earth, Neptune is the only
planet in our solar system not visible to the naked eye and the first
predicted by mathematics before its discovery. In 2011 Neptune
completed its first 165-year orbit since its discovery in 1846.
'''
    turtle.color('blue')
    style = ('agency fb',18, '')

    turtle.write(q, font=style, align='center')

    turtle.hideturtle()
def learn():
    while True:
        print('1. Mercury')
        print('2. Venus')
        print('3. Earth')
        print('4. Mars')
        print('5. Jupiter')
        print('6. Saturn')
        print('7. Uranus')
        print('8. Neptune')
        print('9. No Access')
        try:
            learn=int(input('enter planet you would like to learn more about'))
        except:
            print('invalid')
        if learn==1:
            mercury()
        elif learn==2:
            venus()
        elif learn==3:
            earth()
        elif learn==4:
            mars()
        elif learn==5:
            jupiter()
        elif learn==6:
            saturn()
        elif learn==7:
            uranus()
        elif learn==8:
            neptune()
        elif learn==9:
            print()
            print('. . . Exiting . . .')
            print()
            break
        
while True:
    print('1. Planet')
    print('2. Galaxy')
    print('3. Stars')
    print('4. Moons')
    print('5. Organization')
    print('6 Learn More About Planets')
    print('7. No Access')
    try:
        abc=int(input('Which table would you like to access? (Enter option number)'))
    except:
        print('invalid')
        continue
    if abc==1:
        planet()
    elif abc==2:
        galaxies()
    elif abc==3:
        stars()
    elif abc==4:
        moons()
    elif abc==5:
        org()
    elif abc==6:
        learn()
    elif abc==7:
        print()
        print('. . . We hope you have found what you needed . . .')
        print('. . . Exiting database . . .')
        print('. . . Logging out . . .')
        break
