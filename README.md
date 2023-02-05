# team-management-app - Instawork take-home

## Steps to run:
1. Clone the repo `git clone https://github.com/Aidan-Simard/team-management-app.git`
2. Enter the project directory `cd .\team-management-app\`
3. Setup a virtual environment `python -m venv venv`
4. Active the virtual environment; Windows: `.\venv\Scripts\activate`, UNIX: `source venv/bin/activate`
5. Install required packages `pip install -r requirements.txt`
6. Run database migration `python manage.py migrate`
7. Run local dev server `python manage.py runserver`
- List page: [http://127.0.0.1:8000/team/list/](http://127.0.0.1:8000/team/list/)
- Add member page: [http://127.0.0.1:8000/team/add/](http://127.0.0.1:8000/team/add/)
- Edit member page: [http://127.0.0.1:8000/team/edit/1](http://127.0.0.1:8000/team/edit/1) (requires existing members)

Note: This app has only been tested on python version 3.10.9
