from django.shortcuts import render
from django.http import HttpResponse as hr
from django.contrib import messages
from django.core.mail import EmailMessage

import pyttsx3
from covaid19 import settings
from django.core.mail import send_mass_mail
# and email.find('@')!=-1 and email.find('.') and (len(query)==0 or len(query>=5)) and (len(suggest)==0 or len(suggest)>=5)
# Create your views here.


def index(request):

    return render(request, 'corona/home.html')


def home(request):
    import time

    return render(request, 'corona/index.html')


def news(request):
    def Image():
        url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=b859df0a50d84e7896e1eb01241b963f"
        import requests
        response = requests.get(url)
        news = response.json()
        img = []
        j = 0
        for item in news["articles"]:
            if j == 20:
                break
            img.append(item["urlToImage"])
            j += 1
            title = []
            j = 0
        for item in news["articles"]:
            if j == 20:
                break
            title.append(str(j+1)+". "+item["title"])
            j += 1
        Disc = []
        j = 0
        for item in news["articles"]:
            if j == 20:
                break
            Disc.append((item["description"]))
            j += 1
        link = []
        j = 0
        for item in news["articles"]:
            if j == 20:
                break
            link.append((item["url"]))
            j += 1

        return zip(title, img, Disc, link)
    img = Image()

    return render(request, 'corona/news.html', {'image': img})


def graph(request):
    # GlObal Data
    def global_data():
        import requests
        l1, l2, lst = ["cases", "todayCases", "deaths",
                       "todayDeaths", "recovered", "affectedCountries"], [], []
        url = "https://covid-19-v1.p.rapidapi.com/v1/all"

        headers = {
            'x-rapidapi-host': "covid-19-v1.p.rapidapi.com",
            'x-rapidapi-key': "5a133a9173msh0f9a6071770bbaep132ffejsn556707297e88"
        }

        response = requests.request("GET", url, headers=headers)
        data = response.json()
        data = data["data"]
        for item in l1:
            l2.append(data[item])
        lst.append(l1)
        lst.append(l2)

        return zip(l1, l2)

    # global Data ends here...
    # this code is given by Sharad pandey (future data scientist)

    labels = []
    data = []
    dic = global_data()
    for x, y in dic:
        labels.append(x.capitalize())
        data.append(y)
    labels.remove(labels[0])
    data.remove(data[0])
    print(labels, data)
    record = zip(labels, data)
    return render(request, 'corona/graph.html', {
        'labels': labels,
        'data': data,
        'record': record,
    })


def contact(request):

    name = (request.POST.get('fname', ' '))
    email = (request.POST.get('eid', ' '))
    query = (request.POST.get('query', ' '))
    suggest = (request.POST.get('suggest', ' '))
    myth = (request.POST.get('myth', ' '))

    if email == " " and name == " " and query == " " and suggest == " " and myth == " ":
        email, name, query, suggest, myth = 0, 0, 0, 0, 0
    else:
        li = 'email: '+email + "\n"+"name: "+name+"\n"+"query: " + \
            query+"\n"+'suggestion: '+suggest+"\n"+"myth: "+myth
        text = name+', thank you for showing your interest.Soon we will catch you.You can visit our instagram page fight against corona.This message is only for verification of your email id.Our team request you to stay at home and stay safe.'
        print(name, email, query, suggest, myth,)
        if len(name) >= 3 and name[0].isupper() == True and (query) == "" or len(query) >= 5 and (suggest) == "" or len(suggest) >= 5 and myth == "" or len(myth) >= 5:
            print("hello")
            message1 = ('This data is coming from user end', li, settings.EMAIL_HOST_USER, [
                        'pandeysharad52@gmail.com', 'dm.singh723dm@gmail.com', 'awnish.singh723dm@gmail.com'],)
            message2 = ('Check mail from covaidwarriors.com',
                        text, settings.EMAIL_HOST_USER, [email])

            send_mass_mail((message1, message2), fail_silently=False)

            print(message1, message2)
            messages.success(
                request, " BOOYAH! Your data has been submitted successfully.Soon we will contact you at your given email id.")
        else:
            messages.error(
                request, "Please fill the field correctly.Hover each field to see the format of a field.")

    return render(request, 'corona/contact.html')


def safety(request):

    return render(request, 'corona/safety.html')


def mythbuster(request):
    head = ['5G mobile networks DO NOT spread COVID-19', 'Exposing yourself to the sun or to temperatures higher than 25C degrees DOES NOT prevent the coronavirus disease (COVID-19)', 'You can recover from the coronavirus disease (COVID-19). Catching the new coronavirus DOES NOT mean you will have it for life.',
            'Being able to hold your breath for 10 seconds or more without coughing or feeling discomfort DOES NOT mean you are free from the coronavirus disease (COVID-19) or any other lung disease.', 'Drinking alcohol does not protect you against COVID-19 and can be dangerous', 'COVID-19 virus can betransmitted in areas with hot and humid climates']
    body = ['Viruses cannot travel on radio waves/mobile networks. COVID-19 is spreading in many countries that do not have 5G mobile networks.COVID-19 is spread through respiratory droplets when an infected person coughs, sneezes or speaks. People can also be infected by touching a contaminated surface and then their eyes, mouth or nose.', 'You can catch COVID-19, no matter how sunny or hot the weather is. Countries with hot weather have reported cases of COVID-19. To protect yourself, make sure you clean your hands frequently and thoroughly and avoid touching your eyes, mouth, and nose. ', 'Most of the people who catch COVID-19 can recover and eliminate the virus from their bodies. If you catch the disease, make sure you treat your symptoms. If you have cough, fever, and difficulty breathing, seek medical care early – but call your health facility by telephone first. Most patients recover thanks to supportive care.',
            'The most common symptoms of COVID-19 are dry cough, tiredness and fever. Some people may developmore severe forms of the disease, such as pneumonia. The best way to confirm if you have  the virus producing COVID-19 disease is with a laboratory test.  You cannot confirm it with this breathing exercise, which can even be dangerous.', 'Frequent or excessive alcohol consumption can increase your risk of health problems.', 'From the evidence so far, the COVID-19 virus can be transmitted in ALL AREAS, including areas with hot and humid weather. Regardless of climate, adopt protective measures if you livein, or travel to an area reporting COVID-19. The best way to protect yourself against COVID-19 is by frequently cleaning your hands. By doing this you eliminate viruses that may be on your hands and avoid infection that could occur by then touching your eyes, mouth, and nose.']
    image = ['src="{% static "corona/myth/src="{% static "corona/myth/1.png"%}""%}"', 'src="{% static "corona/myth/1.png"%}"', 'src="{% static "corona/myth/1.png"%}"', 'src="{% static "corona/myth/1.png"%}"',
             'src="{% static "corona/myth/1.png"%}"', 'src="{% static "corona/myth/1.png"%}"']
    d = zip(head, body, image)
    param = {'data': d}
    return render(request, 'corona/myth.html', param)


def helpline(request):

    return render(request, 'corona/helpline.html')


def precaution(request):

    return render(request, 'corona/precaution.html')


def country_graph(request):
    cnt = (request.GET.get('country', ''))
    if cnt == '':
        cnt = 'india'
        cnt = cnt.capitalize()
    print(cnt)
    inp = cnt
    inp = list(map(str, inp.split()))
    print(inp)
    st = ""
    for i in inp:
        st = st+(i.capitalize())+" "

    cnt = st.replace(" ", "")

    def country_data(cnt):
        cntry = str(cnt).lower()
        import requests
        l1 = ["cases", "todayCases", "deaths",
              "todayDeaths", "recovered", "active"]
        l2 = []
        l = 0

        url = "https://covid-19-v1.p.rapidapi.com/v1/countries"

        querystring = {"sortby": "Cases", "country": cntry}

        headers = {
            'x-rapidapi-host': "covid-19-v1.p.rapidapi.com",
            'x-rapidapi-key': "5a133a9173msh0f9a6071770bbaep132ffejsn556707297e88"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        data = response.json()

        for item in l1:
            l2.append(data["data"][item])

        if l == 0:
            print(l)
            messages.warning(
                request, "Please enter correct spelling.Given data is incorrect")

        return zip(l1, l2)
    clabel = []
    csdata = []
    cdata = (country_data(cnt))
    for x, y in cdata:
        clabel.append(x.capitalize())
        csdata.append(y)

    print(clabel, csdata)

    record = zip(clabel, csdata)
    return render(request, 'corona/countrygraph.html', {
        'clabels': clabel,
        'csdata': csdata,
        'country': cnt,
        'record': record,
    })


def state_graph(request):
    cnt = (request.GET.get('state', ''))
    print(cnt)
    if cnt == '':
        cnt = 'Haryana'
        cnt = cnt.capitalize()
    print(cnt)
    inp = cnt
    inp = list(map(str, inp.split()))
    print(inp)
    st = ""
    for i in inp:
        st = st+(i.capitalize())+" "

    cnt = st.replace(" ", " ")
    cnt = cnt[0:len(cnt)-1]
    state=cnt
    def state_data(state):
        print(state)

        state = state.lower()
        import requests
        url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewise"
        head = {
            'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com",
            'x-rapidapi-key': "5a133a9173msh0f9a6071770bbaep132ffejsn556707297e88"
        }
        response = requests.request("GET", url, headers=head)
        data = response.json()
        
        fault = 0
        for item in data:
            if state == str(item["name"].lower()):
                print("hii")
                return item
            else:
                fault = fault+1
        return fault

    data = (state_data(cnt))
    
    
    if type(data) != dict:

        messages.error(request, "Please enter correct spelling.")
        return render(request, 'corona/stategraph.html', {
            'param': "Wrong Input,please enter correct state name"


        })
    else:
        slabel = []
        sdata = []
        for key in data:
            slabel.append(key)
            sdata.append(data[key])
        slabel.remove(slabel[0])
        slabel.remove(slabel[0])
        sdata.remove(sdata[0])
        sdata.remove(sdata[0])
        print(sdata, slabel)

    record = zip(slabel, sdata)

    return render(request, 'corona/stategraph.html', {
        'labels': slabel,
        'data': sdata,
        'state': state,
        'record': record,

    })
