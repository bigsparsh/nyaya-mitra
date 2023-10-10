import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "bigproject-d6846",
    "private_key_id": "7cd3894d881207574a125fda3a7f8e469e13df22",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBmhms6TNhHBiU\nN/Fa57t25EuCia6o+UYPlhKji55VXTbKg9YqV8yWSdOt9xSot7R5ZHYzc4enp30d\nlQ+KN85KxT31SLJu6nYv8YumIwbTvb4N58qViqxVfU8Qw80vYEjXVB3v3OsmUt3N\nI/3wJ8+iVfYlnr/2xMsK/tq6oytMF310QQS5gaRRLNoJHghNZRdVfZjN1GUU9x99\nx9avjXBnU1Dh128v1fJEvblnsaCzVPSgOu2S+bpWGkxch1oH8fNaAGh/NJxb3iTQ\nyA4wpNrHEXqv08+9Kop0gBEo5y6AnhQEHGsGIxxSGcUErilJamDPEb/WmHe65swL\nfzkU+kfzAgMBAAECggEAH+WxeJaiG3bTPzW0Xe4zfxQqs2LXKbSK7C3P+61uNHxQ\nzFmfozGnXdTjZmnWDTIvLuz0DegT9UsYHGlJun5qo6ZkXeb7VwuUK16toSgWNjQF\n0ylZwaersG4ej7w4MH0O+JiS/MkLiTCP+1OEbC6dprkTqVZteaJ/ctv90lA95aGT\nw2nSvkaRVdUGoGTnXir36hFXce+g4iOEBQgtu3Nv2CvV22xJlF7LnMcwNZALXrwi\naUKRmDNepj0L9nbfhKy8n0kDlhtfKUxXcqNlT5qfYWgLMsLhxQTa/RbCKNpYzOh5\nBE6MLjnXKQvNrzZwH9FV9Yqt/M/TmWYCjm2ZPQMM8QKBgQDju04HZSL8NCi2JeI0\niKQ26q5P3QgUQbttLDiu/hLxfXANEWYo1ZNTTthO9nJcPwKli0/KTTFuLwDtVZQs\nMaLZJ/aF5lE6Z0YBevV0g3sR1efAyWX6fN/TOlIfA+YsHIkb3oM8yt8Z8xxpTR3X\nbjh8ZPMpsJi6jTsr3KgtGwKx2wKBgQDZoj708zoxn3ou9ysMCStLsuTvSnyid9F8\nM7qSTgooBayXd/k4nhMLrvrZT40GqqBg7NPNyLYXt9U4KAEAcAPiC2bfy/VAsyVg\npZEqRsxJHHwZmflc2CHPVyhcSk9Du/zd/Ea7w0RS+dEr4VHrBF/GLEGDS9Gns2W/\nvKeW8W7ZyQKBgB92/rX43FeaYVGhdFqr0nyf+kugj4A1AM95v681/aoOGdBEaigU\nMlHdX/exB2YFcrkqwXCDL+Q4bFlebKWaihSU9/PSOcDnCf4kXgumKvfw5R929Dci\nz84gjb4pTMElhDAsk1dv9FlihLdr50afvQA69nn5I3ELGHTb/QSWac3nAoGBAMOr\njyUWhgzVkLonOgnROJ8P0aufcd11EuCzdZxTE+iV6W4pzOXtobwQb7LwRiBnSli6\ntVfAjI9YlhiuRvBIxgT3MWAndXLdXs69LX4wNz3IoX83I68pF4TenQgVO5zvqNNB\nHat1Tbm4qCrmo4tE3INFiQVuJqq7rdCs4pTgr0SZAoGBANKg83I2QqnErmvzpuNt\n6NDBo90CPePuhQadhekCeRcVmY/3V3SoZ0J5/IHRodGb59p9YX6m+it18uXfWd8u\ndhgVRzzbWbcYvTNKm9eM8gmdaU4veCeCV1L/Qy6ijGfT90S7SDGRYhUBducyKhau\nW7M4riTJeASkulFSv5s2+k76\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-r6qtg@bigproject-d6846.iam.gserviceaccount.com",
    "client_id": "111907533834759119723",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-r6qtg%40bigproject-d6846.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
)
firebase_admin.initialize_app(cred)