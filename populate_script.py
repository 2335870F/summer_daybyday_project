import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'summer_daybyday_project.settings')
import django
django.setup()
from entries.models import *
from django.contrib.auth.models import User

cat_objects = {}
admin_objects = {}
bio = "Hello! I enjoy making food the opportunity to upload entries, create reminders, and explore my entries on this website!"
def populate():
    reviews = {"Did well" : {"author" : "lynda_faller", "entry" : "Web App Development Course", "chef" : "lynda_faller", "rating" : 4.25, "comment":"Finished almost all of this week's homework!"},
    "Partied too much" : {"author" : "lynda_faller", "entry" : "Web App Development Course", "chef" : "lynda_faller", "rating" : 2 , "comment":" Best night but didn't work on this course at all!"},
    "Not done yet": {"author" : "lynda_faller", "entry" : "4th of July weekend plans", "chef" : "lynda_faller", "rating" : 3, "comment":"Getting there but still need to buy ingredients!",},
    }
    admins = {
    "lynda_faller" : {"email":"lynda@gmail.com", "password":"lyndafaller", "fname":"Lynda", "lname":"Faller", "chef":True, "photo":"profile_pics/lynda.png",},
    "amy_hynes" : {"email":"amy@gmail.com", "password":"amyhynes", "fname":"Amy", "lname":"Hynes", "chef":True, "photo":"profile_pics/amy.png",},
    "eve_ohagan" : {"email":"eve@gmail.com", "password":"eveohagan", "fname":"Eve", "lname":"O'Hagan", "chef":True, "photo":"profile_pics/eve.png",},
    "q_smart" : {"email":"q@gmail.com", "password":"qiufeismart", "fname":"Q", "lname":"Smart", "chef":True, "photo":"profile_pics/q.png",},}
    #EVERY TIME THERE IS A RETURN STATEMENT IN ABOUT/INGREDIENTS/STEPS USE \r\n
    entries = [
    {"name": "Web App Development Course",
    "importance" : 5,
    "cats" : "My Courses",
    "chef" : "lynda_faller",
    "photo" : "pancakes.jpeg",
    "key_info":"Professor Email: \r\nLecture Times: \r\nLecture Location: \r\nExam Date: TBA",
    "content": "Important assignments due this week: \r\n Important assignments due this month: ",
     "to_do":"Message Kait about 2nd Assessed Exercise",
    },
    {"name": "Object Oriented Software Engineering Course",
    "importance" : 5,
    "cats" : "My Courses, Degree Courses",
    "chef" : "lynda_faller",
    "photo" : "panini.jpeg",
    "key_info":"Professor Email: \r\nLecture Times: \r\nLecture Location: \r\nExam Date: TBA",
    "content": "Important assignments due this week: \r\n Important assignments due this month: ",
     "to_do":"Email professor",
    },
    {"name": "4th of July weekend plans",
    "importance" : 3,
    "cats" : "My Weekends, My Holidays",
    "chef" : "lynda_faller",
    "photo" : "burger.png",
    "key_info":"Date: \r\nTime: \r\nPeople involved: \r\nLocation:",
    "content": "Plans: \r\n Estimated Cost: ",
    "to_do": "Find paper straws",
    },
    {"name": "Online Account Information",
    "importance" : 1,
    "cats" : "My Home, Personal, My Work",
    "chef" : "lynda_faller",
    "photo" : "tirimisu.jpeg",
    "key_info":" ",
    "content": "MyGlasgow Login info: Username: Password: \r\n Deliveroo Login info: Username: Password: ",
    "to_do":"Find out password for Hollister",
    },
    {"name": "Extra Code for Project",
    "importance" : 2,
    "cats" : "My Work, Other, Degree Courses",
    "chef" : "lynda_faller",
    "photo" : "shake.jpeg",
    "key_info":"Code for the new web application I'm working on",
    "content": "For switching into the right project, use: cd /Users/lyndafaller/workspace/summer_daybyday_project\r\n Other info: when you want to add something like category, a MODEL: you need to change rango/admin.py and rango/models.py. first, create your new models in your django app's (rango's) models.py file. This means create class PageAdmin which inherits from admin.ModelAdmin so: class PageAdmin(admin.ModelAdmin). import anything up top you may need to import. Next, update admin.py to include and register your new models. so, class PageAdmin(admin.ModelAdmin), and then do admin.site.register(Page, PageAdmin). you may need to add imports up top. Perform the migration python manage.py makemigrations rango. Apply the changes python manage.py migrate. This will create the necessary infratructure within the database for your new models. If you're running your development server, stop. delete the db.sqlite3 file, delete trash. If you have changed your app's models, run the python manage.py makemigrations rango command. Run python manage.py migrate to create a new database file to migrate database tables to the database. Create a new admin account with python manage.py createsuperuser command. Then, create/edit your population script for your new models. Use the command python populate_rango.py TO RUN IT and to insert credible test data into your new database!!!",
    "to_do":"resolve issue about django",
    },]
    #	cuisines = {"Italian": {"likes": 64, "photo":"italian.jpeg"},
    #		"American": {"likes": 32, "photo":"american.jpeg"},
    #		"Mexican": {"likes": 16, "photo":"mexican.jpeg"},
    #		"Chinese": {"likes": 16, "photo":"chinese.jpeg"},
    #		"Indian": {"likes": 16, "photo":"indian.jpeg"},
    #		"Japanese": {"likes": 16, "photo":"japanese.png"},}
    
    #these are subcategories in the category of My Courses
    My_Courses = {"Degree Courses": {"likes": 32, "photo":"american.jpeg"}, "Electives": {"likes":30, "photo":"american.jpeg"},}

    #	specials = {"St Patrick's Day": {"likes": 64, "photo":"stpaddys.jpeg"},
    #		"Easter": {"likes": 32, "photo":"easter.jpeg"},
    #		"Christmas": {"likes": 16, "photo":"christmas.jpeg"},
    #		"Halloween": {"likes": 16, "photo":"halloween.jpeg"},
    #		"4th of July": {"likes": 16, "photo":"4july.jpeg"},
    #		"Valentine's Day": {"likes": 16, "photo":"valentines.jpeg"},}
    #these are subcategories in the category of My Home
    My_Home = {"Grocery Lists": {"likes": 64, "photo":"stpaddys.jpeg"},
    "Personal": {"likes": 32, "photo":"easter.jpeg"},
    "Family": {"likes": 16, "photo":"christmas.jpeg"},}

    cats = {"My Courses": {"likes": 64, "photo":"breakfast.jpeg"},
    "My Work": {"likes": 32, "photo":"lunch.jpeg"},
    "My Weekends": {"likes": 16, "photo":"dinner.jpeg"},
    "My Holidays": {"likes": 16, "photo":"dessert.jpeg"},
    "My Hobbies": {"likes":160, "photo":"cuisines.jpeg"},
    "My Home": {"likes":160, "photo":"cuisines.jpeg"},
    "Other": {"likes":160, "photo":"spec_occ.jpeg"},}
    #My Courses and My Home have subcategories

    print(" -Initializing admins . . .")
    for admin, admin_data in admins.items():
        u = add_user(admin,admin_data)
        admin_objects[admin] = u

    print(" -Creating Categories . . .")
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["likes"], 'CAT', None, cat_data["photo"])
        cat_objects[cat] = c

    print(" -Creating Subcategories . . .")
    for course, course_data in My_Courses.items():
        c = add_cat(course,course_data["likes"], 'CRS', cat_objects["My Courses"], course_data["photo"])
        cat_objects[course] = c

    for homeent, homeent_data in My_Home.items():
        c = add_cat(homeent,homeent_data["likes"], 'HOM', cat_objects["My Home"], homeent_data["photo"])
        cat_objects[homeent] = c

    print(" -Adding entries . . .")
    for entry in entries:
        add_entry(entry)

    print(" -Adding reviews . . .")
    for review, review_data in reviews.items():
        r = add_review(review,review_data)

def add_entry(entry):
    chef = entry["chef"]
    name=entry['name']
    r = Entry.objects.get_or_create(chef=admin_objects[chef], name=name)[0]
    r.name = entry['name']
    r.photo = "food_pics/"+entry["photo"]
    r.content = entry['content']
    r.importance = entry['importance']
    r.key_info = entry['key_info']
    r.to_do = entry['to_do']

    cats_lst = entry["cats"].split(", ")
    print("   ",name,cats_lst)
    for c in cats_lst:
        r.categories.add(cat_objects[c])
    r.save()
    return r

def add_cat(name, likes, type, supercat, photo):
    print("   ",name, type)
    if type == 'CRS' or type == 'HOM':
        c = Category.objects.get_or_create(name=name, type=type, supercat=supercat)[0]
    else:
        c = Category.objects.get_or_create(name=name, type=type)[0]
    c.likes=likes
    c.photo = "cat_pics/"+photo
    c.save()
    return c

def add_user(username, user_data):
	user = User.objects.get_or_create(username=username)[0]
	user.email = user_data["email"]
	user.set_password(user_data["password"])
	user.first_name = user_data["fname"]
	user.last_name = user_data["lname"]
	user.is_staff = True
	user.save()
	if(user_data["chef"]):
		add_chef(user,user_data)
	return user

def add_chef(user,user_data):
	chef = Chef.objects.get_or_create(user=user)[0]
	chef.photo = user_data["photo"]
	chef.bio = bio
	chef.save()
	return chef

def add_review(title,review_data):
	entry_chef = review_data["chef"]
	entry_name = review_data["entry"]
	author = review_data["author"]
	rating = review_data["rating"]

	entry = Entry.objects.get(chef=admin_objects[entry_chef], name=entry_name)
	review = Review.objects.get_or_create(entry=entry, author=admin_objects[author])[0]
	review.title = title
	review.rating = review_data["rating"]
	review.comment = review_data["comment"]
	review.save()
	return review

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
	print("Population complete.")
