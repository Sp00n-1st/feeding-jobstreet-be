import unittest
from unittest.mock import patch, MagicMock

from src.services.job_service import del_job

class DeleteJobTest(unittest.TestCase):

    @patch('src.utils.util.get_connection')
    def test_del_job_success(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        
        job_id = 1 

        result = del_job(job_id)

        self.assertIsNone(result)

    
    @patch('src.utils.util.get_connection')
    def test_del_job_failure(self, mock_get_connection):
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_conn.commit.side_effect = Exception("Database Error")
        
        job_id = 1 

        result = del_job(job_id)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
