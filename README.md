#Basic Heroku Setup with database
```bash
git clone https://github.com/zeerorg/basic-heroku.git
heroku login
heroku create
heroku addons:add heroku-postgresql:dev
git push heroku master
```

## After creating run python terminal
```python
from deploy import db
db.create_all()
```