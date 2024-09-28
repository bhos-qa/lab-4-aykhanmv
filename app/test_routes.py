# test_app.py
import unittest
import json
from app import app, db
from models import User, Class, Enrollment
import random
import string

class FlaskAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university_pms.db'  # Use existing database
        cls.client = cls.app.test_client()
        
        with cls.app.app_context():

            # Create testuser1
            if not User.query.filter_by(username='testuser1').first():
                test_user = User(username='testuser1', password='testuser1', email='testuser1@example.com')
                db.session.add(test_user)
                db.session.commit()
            
            # Create testuser2
            if not User.query.filter_by(username='testuser2').first():
                test_user = User(username='testuser2', password='testuser2', email='testuser2@example.com')
                db.session.add(test_user)
                db.session.commit()
        
    @classmethod
    def tearDownClass(cls):
        pass  # Do not drop the tables, keep data intact

    def test_get_profile(self):
        # Test with valid user ID
        response = self.client.get('/profile/2')  # Assuming the test user has ID 1
        self.assertEqual(response.status_code, 200)
        self.assertIn('2', response.get_data(as_text=True))

        # Test with invalid user ID
        response = self.client.get('/profile/999')  # Non-existing user ID
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found!', response.get_data(as_text=True))

        # Test with a zero ID (invalid)
        response = self.client.get('/profile/0')  # Invalid user ID
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found!', response.get_data(as_text=True))

    def test_register(self):
        new_user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        new_email = new_user + '@example.com'


        response = self.client.post('/register', json={
            'username': new_user,
            'password': 'password123',
            'email': new_email
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully!', response.get_data(as_text=True))

    def test_login(self):
        response = self.client.post('/login', json={
            'username': 'testuser1',
            'password': 'testuser1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful!', response.get_data(as_text=True))

    def test_password_reset(self):
        response = self.client.post('/password-reset', json={
            'email': 'testuser2@example.com',
            'new_password': 'testuser2_newpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Password reset successfully!', response.get_data(as_text=True))  # Check for correct message

    def test_update_profile(self):
        # Generate a new random email
        new_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@example.com'
        
        # Update email only
        response = self.client.put('/profile/1', json={
            'email': new_email
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Profile updated successfully!', response.get_data(as_text=True))

        # Verify that the email has been updated by calling the get_profile endpoint
        response = self.client.get('/profile/1')  # Fetch the updated profile
        self.assertEqual(response.status_code, 200)
        user_data = response.get_json()
        self.assertEqual(user_data['email'], new_email)  # Check if the email is updated correctly


if __name__ == '__main__':
    unittest.main()
