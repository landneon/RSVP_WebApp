## RSVP Web App by De Lan

![alt text](https://github.com/Alanlande/RSVP_WebApp/blob/master/sample2_pending_page.png "The main pending page")


### Description:

This is a toy proxy server software built in Django framework that helps people manage their RSVP events. People can create events and invite others as guests, vendors and share owner\
s with different level of privileges.

- Play with it by visiting: YOURSERVER:8000 after you launch it on your onw server.

## Usage:
```sh
cd /docker-deploy
sudo docker-compose up
```
### If you met ERROR like: PermissionError: [Errno 13] Permission denied: '/code/RSVP/migrations/0006_auto_20180223_1640.py’

### TRY:
From your web-app dir  (assuming that your app is called RSVP, if not replace RSVP below)
```sh
chmod o+w RSVP/migrations
cd ..
```
### now you are in the directory with docker-compose.yml
```sh
sudo docker-compose run web python3 manage.py makemigrations
```

### Then:
```sh
cd /docker-deploy
sudo docker-compose up
```
## More examples:
![alt text](https://github.com/Alanlande/RSVP_WebApp/blob/master/sample1_owner_page.png "The main owner page")

