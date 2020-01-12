## author: Hongfei Li, https://www.hongfei-business.com/


from bs4 import BeautifulSoup
## original html codes, notice every faculty's information is organized in a div whose class is "faculty-listing"
html_content = '<div class="faculty-listing"> ' \
               '    <div class="faculty-listing-name"> ' \
               '        <a href="https://www.chicagobooth.edu/faculty/directory/g/veronica-guerrieri" id="13"> Veronica Guerrieri</a> ' \
               '    </div> ' \
               '    <div class="faculty-listing-title"> ' \
               '    Ronald E. Tarrson Professor of Economics and Willard Graham Faculty Scholar </div> ' \
               '</div> ' \
               '<div class="faculty-listing"> ' \
               '    <div class="faculty-listing-name"> ' \
               '        <a href="https://www.chicagobooth.edu/faculty/directory/g/varun-gupta" id="14"> Varun Gupta </a> ' \
               '    </div> ' \
               '    <div class="faculty-listing-title"> ' \
               '        Associate Professor of Operations Management ' \
                    '</div> ' \
               '</div> '
### convert html codes to BeautifulSoup Object
bs = BeautifulSoup(html_content, 'html.parser')
### Find all div's whose class is "faculty-listing"
faculty_list = bs.find_all('div', {'class': 'faculty-listing'})
### Find name and link from each faculty's div
for ele in faculty_list:
    name = ele.find('a').text.strip()
    link = ele.find('a').attrs['href']
    print(name, link)