# Simple chat with React-Native and Django

## React-Native

Create a new file `.env` in the root of your React Native app:
```
API_URL=http://example.com
```

Then use this commands to start app:
```
yarn install
react-native run-ios
react-native run-android
```

## Django

Use this commands to start app:
```
virtualenv venv -p python3
source venv/bin/activate
pip install -r backend/requirements.txt
cd backend
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
