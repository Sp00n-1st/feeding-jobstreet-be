import unittest
from unittest.mock import patch, MagicMock

from src.services.job_service import edit_job

class UpdateJobTest(unittest.TestCase):

    @patch('src.utils.util.get_connection')
    def test_edit_job_success(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        
        job_data = {
            'tag_id': 1,
            'company_name': 'Updated Company',
            'job_location': 'Updated Location',
            'title': 'Updated Title',
            'classification': 'Updated Classification',
            'subclassification': 'Updated Subclassification',
            'salary': '120000',
            'work_type': 'Part-time',
            'teaser': 'Updated job opportunity!',
            'work_arrangements': 'Hybrid',
            'other_info': 'Updated other info',
            'date': '2023-10-08'
        }
        job_id = 1 

        result = edit_job(job_id, job_data)

        self.assertIsNone(result)
    
    @patch('src.utils.util.get_connection')
    def test_edit_job_failure(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.commit.side_effect = Exception("Database Error")
        
        job_data = {
            'tag_id': 1,
            'company_name': 'Updated Company',
            'job_location': 'Updated Location',
            'title': 'Updated Title',
            'classification': 'Updated Classification',
            'subclassification': 'Updated Subclassification',
            'salary': '120000',
            'work_type': 'Part-time',
            'teaser': 'Updated job opportunity!',
            'work_arrangements': 'Hybrid',
            'other_info': 'Updated other info',
            'date': '2023-10-08'
        }
        job_id = 1 

        result = edit_job(job_id, job_data)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
