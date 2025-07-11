from bs4 import BeautifulSoup

with open("Day 45/bs4-start/bs4-start/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)

# mengeluarkan nama dari tagnya
print(soup.title.name)

#mengeluarkan string di dalam tag title
print(soup.title.string)

# mengeluarkan semua httml
print(soup.prettify())

#mengeluarkkan tag anchor pertama dari html
print(soup.a)

# # kalo mau mengeluarkan semua elemen dengan anchor tag tertentu ya
# # pake .find_all()

all_anchor_tags = soup.find_all(name = "a")
print(all_anchor_tags) # mmenghasilkan list yang berisi kumpulan tags anchor type
print("\n")
for tag in all_anchor_tags:
    print(tag.getText()) # mengeluarkan semua yang ada di dalem anchor tags <a>
    
for tag in all_anchor_tags:
    print(tag.get("href")) # mengeluarkan semua value yang ditampung di dalam atribut href
    
    
heading = soup.find(name= "h1", id = "bday") # mencari semua yang tags h1 dan memiliki id bday
print(heading)

section_heading = soup.find(name = "h1", class_ = "pro") # mencari semua yang tags h1 dan memiliki class pro
print(section_heading)

wordle_url = soup.select_one(selector = "p a")
print(wordle_url)

wordle_url = soup.select_one(selector = "#wordle")
print(wordle_url)

fav_site = soup.select(selector= ".fav_web")
print(fav_site)