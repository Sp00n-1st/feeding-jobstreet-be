import unittest
from unittest.mock import patch, MagicMock

from src.services.job_service import create_job

class InsertJobTest(unittest.TestCase):

    @patch('src.utils.util.get_connection')
    def test_create_job_success(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        
        job_data = {
            'tag_id': 1,
            'company_name': 'Test Company',
            'job_location': 'Test Location',
            'title': 'Test Title',
            'classification': 'Test Classification',
            'subclassification': 'Test Subclassification',
            'salary': '100000',
            'work_type': 'Full-time',
            'teaser': 'Great job opportunity!',
            'work_arrangements': 'Remote',
            'other_info': 'Some other info',
            'date': '2023-10-08'
        }

        result = create_job(job_data)

        self.assertIsNone(result)

    @patch('src.utils.util.get_connection')
    def test_create_job_failure(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.commit.side_effect = Exception("Database Error")
        
        job_data = {
            'tag_id': 1,
            'company_name': 'Test Company',
            'job_location': 'Test Location',
            'title': 'Test Title',
            'classification': 'Test Classification',
            'subclassification': 'Test Subclassification',
            'salary': '100000',
            'work_type': 'Full-time',
            'teaser': 'Great job opportunity!',
            'work_arrangements': 'Remote',
            'other_info': 'Some other info',
            'date': '2023-10-08'
        }

        result = create_job(job_data)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
