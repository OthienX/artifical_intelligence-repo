import random
first_name = ["john", "mercy","tendo","herbert", "grace","ben", "mishell", "jonita","alberto", "bruno","vena","gabriel", "jackson", "richard", "davis", "joseph", "ryan", "benjamin", "simon","charles","lucky","ameila","timo","annet","mwejuma","maggie","shibert","hajati"]
second_name =["kyakuwaire","mutonyi","kisakye","omondi","apondi", "neto","magret","neto","augustine", "othieno", "kakoza","kalembe","biyizika","waiswa","kalembe"," mpiiya","okorach ","kagoya","akinyi","kabakuma","nuur","nangobi","namugaya","nasanga","nabirye","abel","ashuti","nagawa","mwoyo","babirye ","nambozo","kusasira"]
street_name =["main", "high","maple","park","oak","pine","cedar","elm","washington","preal"]
cities =["kampala","jinja","iganga","bugweri","bukweki","kanyuga","mukono","iiira","aura","gulu"]
states =['bugembe','kainogoga','buwekura','ruhuro','wanyange','katende','budubumli']
for num in range(100):
    first =random.choice(first_name)
    last =random.choice(second_name)
    phone = f'+256-555-{random.randint(1000,99999)}'
    street_num =random.randint(100,999)
    street =random.choice(street_name)
    city = random.choice(cities)
    state =random.choice(states)
    zip_code = random.randint(1000, 66666)
    address = f'{street_num}-{street} st.{city}-{state}-{zip_code}'
    email = first.lower() + last.lower() +"@yahoo.com"
    print(f'{first} {last}\n{phone} \n{address}\n{email}\n')
