# Salt and hash a password in python
import hashlib
import base64
import uuid

password = 'spacemonkey'
salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)


t_sha = hashlib.sha512()
t_sha.update(password+salt)
hashed_password = base64.urlsafe_b64encode(t_sha.digest())
print hashed_password


salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password + salt).hexdigest()
print hashed_password