import unittest
from unittest.mock import patch, MagicMock
from src.services.job_service import scrape_job_data

class ScrapeJobDataTest(unittest.TestCase):

    @patch('src.utils.util.get_connection')
    @patch('requests.get')
    @patch('src.repository.tag_repository.get_by_id')
    @patch('src.repository.job_repository.delete_by_tag_id')
    @patch('src.repository.job_repository.insert_datas')
    def test_scrape_job_data_success(self, mock_insert_datas, mock_delete_by_tag_id, mock_get_by_id, mock_requests_get, mock_get_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_get_connection.return_value = mock_conn
        mock_get_by_id.return_value = 'Java'

        # Mock the HTTP response
        mock_response = MagicMock()
        mock_response.text = '<script>window.SEEK_REDUX_DATA = {"results": {"results": {"jobs": []}}};</script>'
        mock_response.raise_for_status = MagicMock()
        mock_requests_get.return_value = mock_response

        tag_id = 1

        result = scrape_job_data(tag_id)

        mock_requests_get.assert_called_once_with('https://id.jobstreet.com/id/Java-jobs')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
